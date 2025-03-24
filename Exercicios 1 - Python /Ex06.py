# Ler dois números inteiros e exibir o quociente e o resto da divisão inteira entre eles.

def divisao(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor

    print(f"Quociente: {quociente}")
    print(f"Resto: {resto}")

divisao(7,4)
