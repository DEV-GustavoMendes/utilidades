def calcular(valor_mercadoria):
    prestacao = valor_mercadoria // 3 
    entrada = valor_mercadoria - (prestacao * 2)

    print(f"Valor da Mercadoria: R$ {valor_mercadoria}")
    print(f"Valor da Entrada: R$ {entrada:.2f}")
    print(f"Valor da Prestação: 2x R$ {prestacao:.2f}")

calcular(200)