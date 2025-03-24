def verificar_desconto(salario):
    print(f"O seu salário é de {salario}")

    desconto = 0.11 * salario
    if desconto > 334.29:
        print("O valor máximo de desconto é R$ 334,29")
    else:
        print(f"O desconto é de R${desconto}")

verificar_desconto(12000)