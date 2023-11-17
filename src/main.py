import sys

from pprint import pprint

from tokenizer import Tokenizer
from tree_parser import Parser
from compiler import Compiler
from interpreter import Interpreter


if __name__ == "__main__":
    code = sys.argv[1]
    print(code)

    tokens = list(Tokenizer(code))
    pprint(tokens)

    parser = Parser(tokens)
    bin_op = parser.parse()
    print(bin_op)

    compiler = Compiler(bin_op)
    bytecode = list(compiler.compile())

    interpreter = Interpreter(bytecode)
    interpreter.interpret()
