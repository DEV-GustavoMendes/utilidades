array = [int(input(f'Elemento {i + 1}: ')) for i in range(10)]

contador = sum(1 for num in array if num % 2 == 0)

print(f'A quantidade de números pares no array: {contador}')