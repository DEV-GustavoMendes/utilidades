class WeekDay:
    def __init__(self):
        self.day = int(input('Informe um número de 1 a 7: '))

    def verificar(self):
        match self.day:
            case 1: return 'Domingo'
            case 2: return 'Segunda'
            case 3: return 'Terça'
            case 4: return 'Quarta'
            case 5: return 'Quinta'
            case 6: return 'Sexta'
            case 7: return 'Sábado'
            case _: return 'ERRO!!!'
    
    def exibir(self):
        print(f'Dia da semana: {self.day} corresponde a {self.verificar()}')

dia = WeekDay()
dia.exibir()
            