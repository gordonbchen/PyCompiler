from compiler import Bytecode, BytecodeType


class Stack:
    """A list stack."""

    def __init__(self) -> None:
        """Initialize stack."""
        self.stack: list[int] = []

    def push(self, item: int) -> None:
        """Push item to stack."""
        self.stack.append(item)

    def pop(self) -> int:
        """Pop item from stack."""
        return self.stack.pop()
    
    def peek(self) -> int:
        """Peek at first stack item w/out popping."""
        return self.stack[-1]
    
    def __repr__(self) -> str:
        return f"Stack({self.stack})"


class Interpreter:
    """Bytecode interpreter."""

    def __init__(self, bytecode: list[Bytecode]) -> None:
        """Intitialize interpreter and stack."""
        self.bytecode = bytecode
        self.stack = Stack()
        
        self.ind = 0
    
    def interpret(self) -> None:
        """Interpret bytcode into stack instructions."""
        for bc in self.bytecode:
            if bc.type == BytecodeType.PUSH:
                self.stack.push(bc.value)
            elif bc.type == BytecodeType.BIN_OP:
                right = self.stack.pop()
                left = self.stack.pop()

                if bc.value == "+":
                    result = left + right
                elif bc.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unknown operator: {bc.type}")
                
                self.stack.push(result)

        print("Done!")
        print(self.stack)
