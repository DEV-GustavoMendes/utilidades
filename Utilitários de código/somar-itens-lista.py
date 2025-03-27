def somar_lista():
    lista = [1,2,3,4,5]
    soma = 0

    for numero in lista:
        soma += numero
    print(soma)


# ou

def somar_lista2():
    lista = [1,2,3,4,5]
    soma = sum(lista)
    print(soma)

somar_lista2()

