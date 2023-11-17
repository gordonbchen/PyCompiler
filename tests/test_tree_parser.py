from src.tree_parser import Parser, Int, BinOp
from src.tokenizer import Token, TokenType


def test_parsing_add():
    tokens = [
        Token(TokenType.INT, 1),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF)
    ]
    
    tree = Parser(tokens).parse()
    assert tree == BinOp("+", Int(1), Int(2))

def test_parsing_subtract():
    tokens = [
        Token(TokenType.INT, 1),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF)
    ]
    
    tree = Parser(tokens).parse()
    assert tree == BinOp("-", Int(1), Int(2))
