class Emprestimo:
    def __init__(self):
        self.renda_mensal = float(input('Informe sua Renda Mensal: '))
        self.valor_emprestimo = float(input('Valor desejado para empŕestimo: '))
        self.numero_prestacao = int(input('Número de prestações que você deseja: '))

    def verificar_emprestimo(self):
        valor_max_emprestimo = self.renda_mensal * 10
        limite_prestacao = self.renda_mensal * 0.3
        valor_prestacao = self.valor_emprestimo / self.numero_prestacao

        if self.valor_emprestimo > valor_max_emprestimo: 
            return 'Empréstimo NEGADO: o valor solicitado excede o limite permitido.'
        elif valor_prestacao > limite_prestacao: 
            return 'Empréstimo NEGADO: o valor da prestação excede o 30% da renda mensal'
        else: 
            return 'Empréstimo APROVADO!'

    def exibir(self):
        print(f'###########################################################')
        print(f'Renda Mensal: {self.renda_mensal:.2f}')
        print(f'Valor do Empréstimo: {self.valor_emprestimo:.2f}')
        print(f'Número de Prestações: {self.numero_prestacao}')
        print(f'########################################################### \n')
        print(f'Verificar: {self.verificar_emprestimo()}')


gustavo = Emprestimo()
gustavo.exibir()
