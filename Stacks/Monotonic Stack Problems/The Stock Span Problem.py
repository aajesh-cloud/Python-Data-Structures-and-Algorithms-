def stock_span(prices):
    n = len(prices)
    spans = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        spans[i] = (i + 1) if not stack else (i - stack[-1])
        stack.append(i)

    return spans
prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))