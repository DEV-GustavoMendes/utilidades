def media(n1,n2,n3):
    numeros = [n1,n2,n3]
    numeros.sort(reverse = True)

    media = ((numeros[0] * 5) + (numeros[1] * 2.5) + (numeros[2] * 2.5)) / 10

    print(f"A média é {media}")

media(8,10,5)