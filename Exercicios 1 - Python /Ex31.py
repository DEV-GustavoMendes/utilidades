class QuaterbackRating:
    def __init__(self, passes_completos, passes_tentados, jardas_passadas, touchdows, interceptacoes):
            self.passes_completos = int(passes_completos)
            self.passes_tentados = int(passes_tentados)
            self.jardas_passadas = float(jardas_passadas)
            self.touchdowns = int(touchdows)
            self.interceptacoes = int(interceptacoes)

    def ajustar_valor(self, valor):
            return max(0, min(valor, 2.375)) # Função para dizer que o valor está entre 0 e 2.375
        
    def calcular_rating(self):
        a = ((self.passes_completos / self.passes_tentados) - 0.3) / 0.2
        a = self.ajustar_valor(a)

        b = ((self.jardas_passadas / self.passes_tentados) - 3) / 4
        b = self.ajustar_valor(b)
        
        c = (self.touchdowns / self.passes_tentados) / 0.05
        c = self.ajustar_valor(c)

        d = ((self.interceptacoes / self.passes_tentados) - 0.095) / 0.04
        d = self.ajustar_valor(d)

        rating = ((a + b + c + d) * 100) / 6
        return rating

    def exibir(self):
            print(f'Passes Completos: {self.passes_completos}')
            print(f'Passes Tentados: {self.passes_tentados}')
            print(f'Jardas Passadas: {self.jardas_passadas}')
            print(f'Touchdowns: {self.touchdowns}')
            print(f'Interceptações: {self.interceptacoes}')
            print(f'QUARTERBACK RATING: {self.calcular_rating():.2f}')

rating = QuaterbackRating(20, 30, 250, 3, 1)
rating.exibir()