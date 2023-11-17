import pytest

from src.tokenizer import Tokenizer
from src.tree_parser import Parser
from src.compiler import Compiler
from src.interpreter import Interpreter


@pytest.mark.parametrize(
    argnames=["code", "result"],
    argvalues=[
        ("1 + 2", 3),
        ("2 + 1", 3),
        ("5 - 3", 2),
        ("3 - 5", -2)
    ]
)
def test_simple_arith(code: str, result: int):
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())

    interpreter = Interpreter(bytecode)
    interpreter.interpret()

    assert interpreter.stack.pop() == result
    