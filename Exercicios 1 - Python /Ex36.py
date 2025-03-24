class Certificacao:
    def __init__(self, notas):
        self.notas = notas

    def calcular_classificacao(self):
        passou = [nota >= 70 for nota in self.notas]

        if all(passou):
            return "A - Passou em todos os exames."
        elif passou[0] and passou[1] and passou[3] and not (passou[2] or passou[4]):
            return "B - Passou em I, II e IV, mas não em III ou V."
        elif passou[0] and passou[1] and (passou[2] or passou[3]) and not passou[4]:
            return "C - Passou em I e II, III ou IV, mas não em V."
        else:
            return "Reprovado - Não atende aos critérios de aprovação."

    def exibir(self):
        print(f'Classificação: {self.calcular_classificacao()}')
    
notas = [float(input(f'Digite a nota do exame {exame}: ')) for exame in ['I','II','III','IV','IV']]
classificacao = Certificacao(notas)
classificacao.exibir()