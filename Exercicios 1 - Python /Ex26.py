def calcular(n1,n2,n3):
    
    numeros = [n1, n2, n3]
    numeros.sort(reverse = True)
    soma = numeros[0] + numeros[1]

    print(f"{numeros[0]} + {numeros[1]} = {soma}")

calcular(20,31,7)
