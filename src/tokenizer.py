from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Generator


class TokenType(StrEnum):
    """Type of token."""
    INT = auto()

    PLUS = auto()
    MINUS = auto()

    EOF = auto()

@dataclass
class Token:
    """Token type and value."""
    type: TokenType
    value: Any = None


class Tokenizer:
    """Code tokenizer."""

    def __init__(self, code: str) -> None:
        """Initialize tokenizer."""
        self.code = code
        self.ind = 0

    def __iter__(self) -> Generator[Token, None, None]:
        """Yield tokens."""
        cont = True
        while cont:
            token = self.next_token()

            if token.type == TokenType.EOF:
                cont = False

            yield token

    def next_token(self) -> Token:
        """Return next token."""
        # Skip whitespace.
        while (self.ind < len(self.code)) and (self.code[self.ind] == " "):
            self.ind += 1

        # Return EOF at the end.
        if (self.ind == len(self.code)):
            return Token(TokenType.EOF)
        
        # Return correct token.
        char = self.code[self.ind]
        self.ind += 1

        if char.isdigit():
            return Token(TokenType.INT, int(char))
        elif char == "+":
            return Token(TokenType.PLUS)
        elif char == "-":
            return Token(TokenType.MINUS)
        else:
            raise RuntimeError(f"Failed to tokenize: {repr(char)}")
