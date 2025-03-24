def paridade(n):
    if n == 0 or n < 0:
        print("Digite outro número")
    elif n % 2 == 0:
        print(f"O número {n} é PAR")
    else:
        print(f"O número {n} é IMPAR")

paridade(2)