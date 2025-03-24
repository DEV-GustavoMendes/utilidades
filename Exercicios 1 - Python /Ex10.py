# Converter um inteiro informado menor que 32 para sua representação em binário

def converter(numero):
    toBinary = bin(numero)

    if numero < 0 or numero > 32:
        print("O número precisa estar no seguinte intervalo: 0 < numero < 32")
    else:
        print(f"O número {numero} em binário é {toBinary}")

converter(16)

