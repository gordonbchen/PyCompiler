import pytest

from src.tokenizer import Token, TokenType, Tokenizer


def test_tokenizer_add():
    tokens = list(Tokenizer("1 + 2"))
    assert tokens == [
        Token(TokenType.INT, 1),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF)
    ]

def test_tokenizer_subtract():
    tokens = list(Tokenizer("5 - 7"))
    assert tokens == [
        Token(TokenType.INT, 5),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 7),
        Token(TokenType.EOF)
    ]

def test_tokenizer_add_subtract():
    tokens = list(Tokenizer("4 + 3 - 9"))
    assert tokens == [
        Token(TokenType.INT, 4),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 3),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 9),
        Token(TokenType.EOF)
    ]

def test_tokenizer_whitespace():
    tokens = list(Tokenizer("1    +  2"))
    assert tokens == [
        Token(TokenType.INT, 1),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF)
    ]

def test_tokenizer_raises_error_on_unrecognized():
    with pytest.raises(RuntimeError):
        list(Tokenizer("$"))

@pytest.mark.parametrize(
    argnames=["code", "token"],
    argvalues=[
        ("1", Token(TokenType.INT, 1)),
        ("+", Token(TokenType.PLUS)),
        ("-", Token(TokenType.MINUS))
    ]
)
def test_tokenizer_recognizes_tokens(code: str, token: Token):
    tokens = list(Tokenizer(code))
    assert tokens == [token, Token(TokenType.EOF)]
