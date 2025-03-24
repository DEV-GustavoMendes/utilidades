def Fibonacci(termos):
    a = 1
    b = 1
    for _ in range(termos):
        print(a, end= ' ')
        a, b = b, a +b

Fibonacci(10)