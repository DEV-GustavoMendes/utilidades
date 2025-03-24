class Simbolo:
    def __init__(self):
        while True: # Enquanto houver mais de um caracter no input, vai chamar o input de novo.
            self.caracter = input('Informe um caracter: ')
            if len(self.caracter) > 1:
                print('Digite apenas um caracter!')
            else:
                break

    def verificar_caracter(self):
        if self.caracter.isalpha(): # Verifica se o input é uma letra
            if self.caracter.lower() in 'aeiou':
                return 'Vogal' 
            else: 
                return 'Consoante'

        elif self.caracter.isdigit(): # Verifica se o input é um número
            return 'Número'
            
        else: 
            return 'Símbolo'

    def exibir(self):
        print(f'Caracter: {self.caracter}')
        print(f'Classificação: {self.verificar_caracter()}')


symbol = Simbolo()
symbol.exibir()