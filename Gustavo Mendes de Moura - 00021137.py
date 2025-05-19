print('\033[35mGustavo Mendes de Moura\033[0m')


def array_function():
    array = []
    print("\33[32mDigite os valores da matriz 3x3\033[0m: ")
    for i in range(3):
        line = []
        for j in range(3):
            value = int(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            line.append(value)
        array.append(line)

    print(f"\nMatriz 3x3: ")

    for line in array: 
        for value in line:
            print(f"\33[32m[{value:^5}]\033[0m:", end=" ")
        print()

    
    column_sum = sum(array[i][2] for i in range(3))
    even_sum = sum(value
                    for line in array
                      for value in line if value % 2 == 0)
    highest_value = max(array[1])

    print(f"\n\033[33mSoma dos Números Pares: {even_sum}\033[0m")
    print(f"\033[33mMaior Número da Segunda Linha: {highest_value}\033[0m")
    print(f"\033[33mSoma de Todos os Números da Terceira Coluna: {column_sum}\033[0m")


array_function()