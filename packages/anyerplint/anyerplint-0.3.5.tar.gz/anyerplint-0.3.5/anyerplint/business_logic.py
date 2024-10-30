import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import yaml

from anyerplint import preprocessor
from anyerplint.library import Library
from anyerplint.translate import Translator

from . import __version__, tnex, util

ROOT = Path(__file__).absolute().parent


ReportData = TypedDict(
    "ReportData",
    {
        "Unknown variables": list[str],
        "Unknown calls": list[str],
        "Unknown jumps": list[str],
        "Unknown tags": list[str],
        "Other errors": list[str],
        "Expression errors": list[dict[str, str | list[str]]],
        "Unknown loop variables": list[str],
    },
    total=False,
)


# ruff lead this alone man
emit = print


def do_check(
    libs: list[str],
    targets: list[str],
    teaching: bool,
    *,
    nostdlib: bool = False,
) -> dict[str, str | ReportData]:
    emit(f"AnyErpLintVersion: {__version__.strip()}")

    lib_vars = Library(
        variables=set(),
        calls=set(),
        jumps=set(),
        tags=set(),
        teaching=teaching,
        loopvariables=set(),
    )

    # always feed the "standard library, except when unit testing (nostdlib)

    if not nostdlib:
        local_app_data = util.get_app_local_dir()
        lib_vars.load_from_disk(local_app_data)

    for lib in libs:
        lib_vars.load_from_disk(Path(lib))

    has_errors = False
    all_errors: dict[str, str | ReportData] = {}
    for target in targets:
        files = util.glob_plus(target)
        errs = check_files(lib_vars, files)
        if errs:
            all_errors.update(errs)
            has_errors = True

    if lib_vars.teaching:
        stdlib_path = util.get_app_local_dir()
        lib_vars.save_to_disk(stdlib_path, emit)

    if has_errors:
        emit("Errors found: >")
        error_counts = {
            f: (
                sum(len(prop) for prop in e.values() if isinstance(prop, list))
                if not isinstance(e, str)
                else -1
            )
            for f, e in all_errors.items()
        }
        rep = sorted((k, v) for (k, v) in error_counts.items())
        for line in rep:
            emit("  ", line[0], ";", line[1])

    return all_errors


def report_fatal(fname: Path, ex: Exception) -> str:
    message = f"FATAL, {ex}"
    emit(f"{fname}: {message}")
    return message


def should_skip_file(fpath: Path) -> bool:
    if fpath.suffix != ".xml":
        return True
    text = util.read_text_file(fpath)
    return not ("<erpConnector" in text or "<section" in text)


def check_file(lib_vars: Library, file: Path) -> str | ReportData | None:
    try:
        if should_skip_file(file):
            emit(f"{file}: SKIP nontemplate")
            return None
        r = parse_file(file, teaching=lib_vars.teaching)
    except (
        ElementTree.ParseError,
        PermissionError,
        UnicodeDecodeError,
        preprocessor.PreprocessError,
    ) as e:
        return report_fatal(file, e)

    return report(lib_vars, str(file), r)


def check_files(
    lib_vars: Library, files: Iterable[Path]
) -> dict[str, str | ReportData]:
    errs: dict[str, str | ReportData] = {}
    for f in files:
        errlist = check_file(lib_vars, f)
        if errlist:
            errs[str(f)] = errlist

    return errs


@dataclass
class ExprError:
    """Represents an error in an expression."""

    summary: str
    translated: str
    messages: list[str]

    def render(self) -> dict[str, str | list[str]]:
        """Render yaml compatible object."""
        return {"Error": self.summary, "Simple": self.translated, "Msg": self.messages}


@dataclass
class Parsed:
    """The things found while parsing a file."""

    var_decl: set[str]
    var_used: set[str]
    alltags: set[str]
    calls: set[str]
    jumps: set[str]
    syntax_errors: list[str]
    loop_var_decl: set[str]
    loop_var_use: set[str]
    expression_errors: list[ExprError]
    full_content: str


def report(lib_vars: Library, fname: str, p: Parsed) -> ReportData:
    undeclared_vars = p.var_used - p.var_decl
    undeclared_vars.difference_update(lib_vars.variables)
    unknown_loop_variables = {
        lv
        for lv in p.loop_var_use
        if lv.lower() not in p.loop_var_decl
        and lv.lower() not in lib_vars.loopvariables
    }

    if lib_vars.teaching:
        lib_vars.calls.update(p.calls)
        lib_vars.jumps.update(p.jumps)
        lib_vars.tags.update(p.alltags)
        lib_vars.variables.update(undeclared_vars)
        lib_vars.loopvariables.update(lv.lower() for lv in unknown_loop_variables)

    errors: ReportData = {}

    if undeclared_vars:
        errors["Unknown variables"] = util.add_linenumbers(
            p.full_content,
            sorted(undeclared_vars),
        )

    unknown_calls = p.calls
    unknown_calls.difference_update(lib_vars.calls)
    if unknown_calls:
        errors["Unknown calls"] = sorted(unknown_calls)

    unknown_jumps = p.jumps
    unknown_jumps.difference_update(lib_vars.jumps)
    if unknown_jumps:
        errors["Unknown jumps"] = sorted(unknown_jumps)

    unknown_tags = p.alltags
    unknown_tags.difference_update(lib_vars.tags)
    if unknown_tags:
        errors["Unknown tags"] = sorted(unknown_tags)

    if p.syntax_errors:
        errors["Other errors"] = list(p.syntax_errors)

    if p.expression_errors:
        errors["Expression errors"] = [e.render() for e in p.expression_errors]

    if unknown_loop_variables:
        errors["Unknown loop variables"] = sorted(unknown_loop_variables)

    if errors:
        emit(yaml.dump({fname: errors}, width=200, sort_keys=False).strip())

    return errors


key_params: dict[str, str] = {
    "bw_exec": "command",
    "bw_file_functions": "command",
    "bw_table_method": "command",
    "bw_string_functions": "operation",
    "bw_ws_function": "method",
}


def summarize_call(node: Element) -> str:
    name = node.attrib.get("name", "NONAME").lower()
    full = name
    # What should we do when there's multiple params with the same name?
    params = {
        p.attrib.get("name", "NONAME"): (p.text or "TEXTMISSING")
        for p in node.iter("parameter")
    }
    suboperation_param_name = key_params.get(name)
    if suboperation_param_name:
        suboperation = params.get(suboperation_param_name, "UNK")
        full += "." + suboperation

    return (full + " - " + ",".join(sorted(params))).strip()


def summarize_output(node: Element) -> str:
    output_type = node.attrib.get("type", "NOTYPE")
    params = {p.attrib.get("name", "NONAME") for p in node.iter("parameter")}

    return ("Output " + output_type + " - " + ",".join(sorted(params))).strip()


def summarize_tag(node: Element) -> str:
    at = " " + " ".join(sorted(node.attrib.keys())) if node.attrib else ""
    return "<" + node.tag + at + ">"


def brace_check(s: str) -> list[str]:
    stack: list[tuple[str, int]] = []
    lines = s.splitlines()
    closers = {"{": "}", "[": "]", "(": ")"}
    errors: list[str] = []
    for lnum, line in enumerate(lines, 1):
        flush_stack = False
        in_quote = False
        for cnum, ch in enumerate(line, 1):
            if ch == '"':
                # only care about quotes if we are in some nested operation already, top level quotes are not considered
                if stack:
                    in_quote = not in_quote

            if in_quote:
                continue

            if ch in "{([":
                stack.append((ch, lnum))
            if ch in "})]":
                try:
                    from_stack, _ = stack.pop()
                except IndexError:
                    errors.append(
                        f"Too many closing braces at line {lnum}, looking at '{ch}' on col {cnum}: ==> {line[cnum-10:cnum]} <==: {line.strip()}",
                    )
                    flush_stack = True
                    break

                expected = closers[from_stack]
                if expected != ch:
                    errors.append(
                        f"Expected brace {expected}, got {ch} at line {lnum} col {cnum}: {line.strip()}",
                    )
                    flush_stack = True
                    break
        if flush_stack:
            stack = []
    if stack:
        pretty_stack = ", ".join(f"{ch} {lnum}" for ch, lnum in stack)
        errors.append(
            f"File ended with mismatched braces, remaining in stack (char, linenum): {pretty_stack}",
        )
    return errors


def describe_node(n: Element) -> str:
    return "<" + n.tag + str(n.attrib) + ">"


def describe_jump(n: Element) -> str:
    params = sorted(
        child.attrib.get("name", "NONAME").strip() for child in n.iter("parameter")
    )
    target = n.attrib.get("jumpToXPath", "NOXPATH")
    prefix = "//section[@name='"
    if target.startswith(prefix):
        target = "..." + target[len(prefix) :].rstrip("]'")

    desc = (
        "Jump "
        + n.attrib.get("jumpToXmlFile", "NOFILE")
        + " -- "
        + target
        + " -- "
        + " ".join(params)
    )
    return desc.strip()


def is_illegal_password(name: str, value: str) -> bool:
    if "passw" not in name.lower():
        return False
    stripped = (value or "").strip()
    if not stripped:
        return False
    if stripped.startswith("{"):
        # password should always be references to variables or expressions, never literal values
        return False
    return True


XMLWRITER_COMMAND_PAIRS = {
    "startattribute": "endattribute",
    "startdocument": "enddocument",
    "startelement": "endelement",
}

XMLWRITER_COMMAND_SINGLE = {"write", "writeraw"}


def check_single_outputresource(elem: Element, output_location: str) -> str | None:
    cmd_stack = []
    for ind, cmd in enumerate(elem.iter("command"), 1):
        cmd_type = cmd.attrib.get("type")
        if not cmd_type:
            return f"Command missing 'type' attribute in OutputResource ({output_location}, command {ind})"
        elif cmd_type in XMLWRITER_COMMAND_SINGLE:
            continue
        elif cmd_type in XMLWRITER_COMMAND_PAIRS:
            cmd_stack.append(cmd_type)
        elif cmd_type in XMLWRITER_COMMAND_PAIRS.values():
            try:
                prev = cmd_stack.pop()
            except IndexError:
                return f"Invalid command '{cmd_type}' in OutputResource, no matching starting tag ({output_location}, command {ind})"
            expected = XMLWRITER_COMMAND_PAIRS.get(prev)
            if cmd_type != expected:
                return f"Invalid command type '{cmd_type}' in OutputResource, expected '{expected}' ({output_location}, command {ind})"
        else:
            return f"Unknown command type '{cmd_type}' in OutputResource ({output_location}, command {ind})"

    if cmd_stack:
        return f"Did not end all started items in OutputResource, unterminated: {','.join(cmd_stack)} ({output_location})"
    return None


def check_outputresources(root: Element) -> list[str]:
    errors = []
    for outputresource in root.iter("output"):
        if outputresource.get("type", "").split(".")[-1] == "XmlWriterOutputResource":
            description = util.format_xml_tag(outputresource)
            cmd_error = check_single_outputresource(outputresource, description)
            if cmd_error:
                errors.append(cmd_error)
    return errors


def full_parse_expression(expr: str) -> tuple[str, list[str]]:
    try:
        parsed = tnex.parse(expr, expand_entities=True)
        if not parsed:
            return "", [f"Empty parse result from: {expr}"]
        translator = Translator()
        translated = translator.translate(parsed)
    except tnex.ParseError as e:
        return "", [f"Fatal parse error: {e}"]
    else:
        return translated, translator.errors


MAX_EXPRESSION_LINES = 500


def find_invalid_expressions(expressions: list[tuple[str, int]]) -> list[ExprError]:
    res: list[ExprError] = []
    for expr, linenum in expressions:
        if expr and expr[0].isalpha() and "," not in expr:
            res.append(
                ExprError(
                    summary=f"Line {linenum}, expression contains no comma: {{{expr}}}",
                    translated="N/A",
                    messages=[],
                )
            )
            continue
        if expr.count("\n") > MAX_EXPRESSION_LINES:
            res.append(
                ExprError(
                    summary=f"Line {linenum}, expression too long, likely unterminated: {{{expr[:200]}}}",
                    translated="N/A",
                    messages=[],
                )
            )
            continue

        translated, errors = full_parse_expression(expr)

        if errors:
            res.append(
                ExprError(
                    summary=f"Line {linenum}, expression: {{{expr}}}",
                    translated=translated,
                    messages=errors,
                )
            )
    return res


def find_invalid_text_in_tags(tree: ElementTree.ElementTree) -> list[str]:
    no_text_allowed_tags = [
        "sections",
        "section",
        "method",
        "output",
        "outputCommands",
        "builtInMethodParameterList",
    ]

    errors: list[str] = []
    for notext in no_text_allowed_tags:
        nodes = tree.iter(notext)
        errors.extend(
            f"Node should not contain text: {describe_node(n)} -- {n.text.strip()}"
            for n in nodes
            if n.text and n.text.strip()
        )
    return errors


def parse_file(fname: Path, *, teaching: bool = False) -> Parsed:
    tree = ElementTree.parse(fname)
    raw_cont = util.read_text_file(fname)
    comments_removed = util.replace_commented_xml_with_empty_lines(raw_cont)

    vardecl = {
        v.attrib.get("name", "unknown_var"): (v.text or "")
        for v in tree.iter("variable")
    }
    all_params = {
        v.attrib.get("name", "unknown_var"): (v.text or "")
        for v in tree.iter("parameter")
    }

    expressions = preprocessor.get_expressions(comments_removed)

    prop_regex = r"([a-zA-Z_][a-zA-Z0-9_.]*),(\w+)"

    propaccess = {
        (match.group(1), match.group(2))
        for expr, line in expressions
        for match in re.finditer(prop_regex, expr)
    }
    varuse = {name for expr_type, name in propaccess if expr_type.lower() == "v"}

    # what to do with p params?
    otherpropaccess = {k for k, v in propaccess if k.lower() not in ["v", "f", "p"]}
    calls = {summarize_call(v) for v in tree.iter("builtInMethodParameterList")}
    outputs = {summarize_output(v) for v in tree.iter("output")}
    calls.update(outputs)
    alltags = {summarize_tag(t) for t in tree.iter()}
    loop_data_source_attribs = {n.attrib.get("loopDataSource") for n in tree.iter()}
    loop_data_sources = {
        ls.split(";")[0].lower() for ls in loop_data_source_attribs if ls
    }
    return_names = {
        n.attrib.get("name", "UNNAMED_RETURN").lower() for n in tree.iter("return")
    }
    loop_data_sources.update(return_names)

    jumps = {
        describe_jump(n) for n in tree.iter("method") if n.attrib.get("jumpToXmlFile")
    }

    errors = []
    expr_errors = []
    if not teaching:
        cdata_removed = util.replace_cdata_with_empty_lines(comments_removed)
        errors.extend(brace_check(cdata_removed))

        errors.extend(find_invalid_text_in_tags(tree))

        var_passwords = {v for v in vardecl if is_illegal_password(v, vardecl[v])}
        param_passwords = {
            p for p in all_params if is_illegal_password(p, all_params[p])
        }
        passwords = var_passwords | param_passwords
        if passwords:
            errors.append("Passwords contains literal text: " + ",".join(passwords))

        outputresource_errors = check_outputresources(tree.getroot())
        errors.extend(outputresource_errors)

        expr_errors = find_invalid_expressions(expressions)

    return Parsed(
        var_decl=set(vardecl),
        var_used=varuse,
        alltags=alltags,
        calls=calls,
        jumps=jumps,
        syntax_errors=errors,
        loop_var_decl=loop_data_sources,
        loop_var_use=otherpropaccess,
        full_content=comments_removed,
        expression_errors=expr_errors,
    )
