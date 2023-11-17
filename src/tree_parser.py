from dataclasses import dataclass

from tokenizer import Token, TokenType


@dataclass
class TreeNode:
    """An AST node."""
    pass

@dataclass
class Int(TreeNode):
    """An integer node."""
    value: int

@dataclass
class BinOp(TreeNode):
    """A binary op node."""
    op: str
    left: Int
    right: Int


class Parser:
    """AST parser."""

    def __init__(self, tokens: list[Token]) -> None:
        """Initialize parser."""
        self.tokens = tokens
        self.ind = 0

    def parse(self) -> BinOp:
        """Parse the program."""
        left_op = self.eat(TokenType.INT)

        if self.peek() == TokenType.PLUS:
            op = "+"
            self.eat(TokenType.PLUS)
        else:
            op = "-"
            self.eat(TokenType.MINUS)

        right_op = self.eat(TokenType.INT)

        # Expect program finish.
        self.eat(TokenType.EOF)

        bin_op = BinOp(op, Int(left_op.value), Int(right_op.value))
        return bin_op

    def eat(self, expected_token_type: TokenType) -> Token:
        """Returns the next token. Raise an error if unexpected token type."""
        next_token = self.tokens[self.ind]
        self.ind += 1

        if (next_token.type != expected_token_type):
            raise RuntimeError(
                f"Expected token type {repr(expected_token_type)}, " \
                f"ate {repr(next_token.type)}."
            )
        
        return next_token
    
    def peek(self, skip: int = 0) -> TokenType | None:
        """Check the type of an upcoming token w/out consuming it."""
        peek_ind = self.ind + skip

        if peek_ind < len(self.tokens):
            return self.tokens[peek_ind].type
        else:
            return None
