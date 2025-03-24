class Saque:
    def __init__(self):
        self.notas = [100, 50, 20, 10, 5, 2, 1]
    
    def calcular_notas(self, valor):
        if valor <= 0:
            print('O valor solicitado deve ser maior que zero!')
        
        distribuicao = {} # Set

        for nota in self.notas:
            quantidade, valor = divmod(valor,nota)
            if quantidade > 0:
                distribuicao[nota] = quantidade
        return distribuicao
    
try:
    valor = int(input('Digite o valor do saque em reais: ')) # Input do valor
    caixa = Saque()
    distribuicao = caixa.calcular_notas(valor)

    print("\nDistribuição de notas:")
    for nota, quantidade in distribuicao.items():
        print(f"R${nota},00: {quantidade} nota(s)")

except ValueError as e:
    print(f"Erro: {e}")
