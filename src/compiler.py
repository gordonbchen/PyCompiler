from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Generator

from tree_parser import BinOp


class BytecodeType(StrEnum):
    PUSH = auto()
    BIN_OP = auto()

@dataclass
class Bytecode:
    type: BytecodeType
    value: Any = None


class Compiler:
    """An AST compiler."""

    def __init__(self, tree: BinOp) -> None:
        """Initialize compiler."""
        self.tree = tree

    def compile(self) -> Generator[Bytecode, None, None]:
        """Compile the AST into bytecode."""
        left = self.tree.left
        yield Bytecode(BytecodeType.PUSH, left.value)
        
        right = self.tree.right
        yield Bytecode(BytecodeType.PUSH, right.value)

        yield Bytecode(BytecodeType.BIN_OP, self.tree.op)
