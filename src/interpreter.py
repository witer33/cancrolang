import io
import main


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


class BrainfuckInterpreter:

    def __init__(self, data: io.BufferedReader):
        self.data: io.BufferedReader = data
        self.cells = [0]
        self.cell_index = 0
        self.block_stack = Stack()

    def set_cell(self, index: int):
        if len(self.cells) <= index:
            self.cells += [0] * (index - len(self.cells) + 1)
        self.cell_index = index

    def run(self):
        self.data.seek(0)
        skip = False
        while (char := self.data.read(1)) != b"":
            if char == b">" and not skip:
                self.set_cell(self.cell_index + 1)
            elif char == b"<" and not skip:
                self.set_cell(self.cell_index - 1)
            elif char == b"+" and not skip:
                self.cells[self.cell_index] += 1
            elif char == b"-" and not skip:
                self.cells[self.cell_index] -= 1
            elif char == b"." and not skip:
                print(chr(self.cells[self.cell_index]), end="")
            elif char == b"," and not skip:
                self.cells[self.cell_index] = ord(input())
            elif char == b"[" and not skip:
                if self.cells[self.cell_index] == 0:
                    skip = True
                else:
                    self.block_stack.push(self.data.tell())
            elif char == b"]":
                if skip:
                    skip = False
                elif self.cells[self.cell_index] != 0:
                    self.data.seek(self.block_stack.peek())
                else:
                    self.block_stack.pop()


class CancroReader(io.BufferedReader):

    def read(self, __size: int = ...) -> bytes:
        return main.decode(super().read(__size * 6).decode()).encode()
