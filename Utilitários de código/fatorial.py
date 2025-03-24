def fatorial_iterativo(numero):
    if numero < 0:
        print("Fatorial não definido para números negativos.")

    elif numero == 0:
        print("O fatoral de 0 é 1")

    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial = fatorial * i
        print(f"o fatorial de {numero} é {fatorial}")

fatorial_iterativo(8)

