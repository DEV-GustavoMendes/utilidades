class Pulverizacao:
    def __init__(self):
        pass
        
    def tipo_area(self):
        tipo = int(input(f'Informe qual tipo de praga: '))
        area = int(input('Informe o a área a ser pulverizada: '))
        
        if tipo == '1':
            return area * 50
        elif tipo == '2':
            return area * 100
        elif tipo == '3':
            return area * 150
        elif tipo == '4':
            return area *  250
        else: return 'Inválido'
