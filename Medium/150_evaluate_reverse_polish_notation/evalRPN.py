def evalRPN(tokens: list[str]) -> int:
    stack = []
    res = None

    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def divide(a, b):
        if abs(a) < abs(b):
            return 0
        else:
            return int(a / b)
    operations = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": divide,
    }

    for char in tokens:
        if char not in operations.keys():
            stack.append(int(char))
        else:
            stack.append(operations[char](stack.pop(-2), stack.pop()))

    return stack[-1]

stuff = ["0","3","/"]
print(evalRPN(stuff))

