def evaluate_postfix(expression):
    values = []
    tokens = expression.split()

    for token in tokens:
        if token in ('+', '-', '*', '/'):
            right = values.pop()
            left = values.pop()

            if token == '+':
                values.append(left + right)
            elif token == '-':
                values.append(left - right)
            elif token == '*':
                values.append(left * right)
            elif token == '/':
                values.append(left / right)
        else:
            values.append(int(token))

    return values[-1]


expression = "5 3 4 * +"
print(f"{expression} =", evaluate_postfix(expression))