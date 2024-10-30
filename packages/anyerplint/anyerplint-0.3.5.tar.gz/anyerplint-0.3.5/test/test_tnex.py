import pytest
from anyerplint.ast import FuncCall, SpecialToken
from anyerplint.tnex import ParseError, parse


def test_parser() -> None:
    assert parse("foo") == "foo"
    assert parse("foo()") == FuncCall("foo", [])
    assert parse("foo(),N") == FuncCall(",N", [FuncCall("foo", [])])
    assert parse("foo ()") == FuncCall("foo", [])
    assert parse("foo(1)") == FuncCall("foo", ["1"])
    assert parse("foo(1;1)") == FuncCall("foo", ["1", "1"])

    assert parse("foo(1;;1)") == FuncCall("foo", ["1", SpecialToken.EmptyArgument, "1"])
    assert parse("foo(1; 1)") == FuncCall("foo", ["1", "1"])
    assert parse("foo(1; ;1)") == FuncCall(
        "foo", ["1", SpecialToken.EmptyArgument, "1"]
    )
    assert parse('foo(1; "1")') == FuncCall("foo", ["1", '"1"'])
    assert parse("foo(1;)") == FuncCall("foo", ["1", SpecialToken.EmptyArgument])
    assert parse("foo(;1)") == FuncCall("foo", [SpecialToken.EmptyArgument, "1"])
    assert parse("foo(1; )") == FuncCall("foo", ["1", SpecialToken.EmptyArgument])
    assert parse('foo(1;;"1")') == FuncCall(
        "foo", ["1", SpecialToken.EmptyArgument, '"1"']
    )
    assert parse('foo(1;; "1")') == FuncCall(
        "foo", ["1", SpecialToken.EmptyArgument, '"1"']
    )

    assert parse('"some string"') == '"some string"'

    assert parse('foo("some string";"other string";0)') == FuncCall(
        "foo", ['"some string"', '"other string"', "0"]
    )

    assert parse('foo("some string";"other string")') == FuncCall(
        "foo", ['"some string"', '"other string"']
    )

    # nothing special with ,
    assert parse("a,b(c,d;e,f;1.0)") == FuncCall("a,b", ["c,d", "e,f", "1.0"])

    assert parse(r'" string with \" char"') == '" string with \\" char"'
    assert parse(R'" string with \\\" char"') == '" string with \\\\\\" char"'
    assert (
        parse(r'"some string with ) and ( and \" characters"')
        == '"some string with ) and ( and \\" characters"'
    )

    assert parse(r'foo,"long / () accessor"') == 'foo,"long / () accessor"'
    assert parse(r'foo(F,NOW(),"yyyy")') == FuncCall(
        "foo", [FuncCall(',"yyyy"', [FuncCall("F,NOW", [])])]
    )
    assert parse(r'F,NOW(),"yyyy"') == FuncCall(',"yyyy"', [FuncCall("F,NOW", [])])

    complex_expr = parse(
        r'foo(f1;bar(b1;b2;"b3";"wide string");f2;baz(1;"some string with ) and ( and \" characters"))'
    )
    assert complex_expr == FuncCall(
        "foo",
        [
            "f1",
            FuncCall("bar", ["b1", "b2", '"b3"', '"wide string"']),
            "f2",
            FuncCall("baz", ["1", '"some string with ) and ( and \\" characters"']),
        ],
    )

    with pytest.raises(ParseError, match="Unterminated string"):
        parse('foo("unterminated)')

    with pytest.raises(
        ParseError, match="Invalid token ';' at top level of expression"
    ):
        parse(";")

    with pytest.raises(
        ParseError, match=r"Invalid token '\)' at top level of expression"
    ):
        parse("foo)")

    with pytest.raises(ParseError, match="Empty parse result for expression: ''"):
        parse("")

    with pytest.raises(
        ParseError,
        match="',format' syntax called without preceding expression: ',hello'",
    ):
        parse(",hello")

    with pytest.raises(
        ParseError,
        match="',format' syntax called without preceding expression: ',\"hello\"'",
    ):
        parse(',"hello"')
