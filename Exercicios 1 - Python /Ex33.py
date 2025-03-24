class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordernada = [x,y]

    def verificar_quadrante(self):
       
            if self.x > 0 and self.y > 0: return '1° Quadrante'

            elif self.x < 0 and self.y > 0: return '2° Quadrante'

            elif self.x < 0 and self.y < 0: return '3° Quadrante'

            elif self.x > 0 and self.y < 0: return '4° Quadrante'

            elif self.x == 0 and self.y == 0: return 'Você está na Origem'

            elif self.x == 0: return 'Você está sobre o eixo y'

            elif self.y == 0: return 'Você está sobre o eixo X'

            else: return 'Cordenada inválida'

    def exibir(self):
         print(f'Coordenada: {self.coordernada}')
         print(f'Posição: {self.verificar_quadrante()}')

cartesiano = Coordenadas(1,0)
cartesiano.exibir()