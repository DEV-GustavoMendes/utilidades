# Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, dado seu raio e sua altura.

def calcular_Volume(raio, altura):
    pi = 3.14
    volume = pi * altura * (raio ** 2)
    print(f"O volume do cilíndro é {volume:.2f}")

calcular_Volume(4,10)
