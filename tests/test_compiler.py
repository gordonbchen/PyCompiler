from src.compiler import Bytecode, BytecodeType, Compiler
from src.tree_parser import BinOp, Int


def test_compiler_add():
    tree = BinOp("+", Int(1), Int(2))

    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        Bytecode(BytecodeType.PUSH, 1),
        Bytecode(BytecodeType.PUSH, 2),
        Bytecode(BytecodeType.BIN_OP, "+")
    ]

def test_compiler_subtract():
    tree = BinOp("-", Int(1), Int(2))

    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        Bytecode(BytecodeType.PUSH, 1),
        Bytecode(BytecodeType.PUSH, 2),
        Bytecode(BytecodeType.BIN_OP, "-")
    ]
