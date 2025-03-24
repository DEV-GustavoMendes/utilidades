def Gasolina(valor):
    if valor < 25:
        desconto = 0.02 * valor
        total = (valor * 2.70) - desconto
    elif valor > 25:
        desconto = 0.04 * valor
        total = (valor * 2.70) - desconto
    else:
        return 'Inválido!'
    
    print(f'Combustível: Gasolina')
    print(f'Litros: {valor} Litros')
    print(f'Desconto: R${desconto:.2f}')
    print(f'Total: R${total:.2f}')
    print(f'###################################################################')

    return total

def Alcool(valor):
    if valor < 25:
        desconto = 0.03 * valor
        total = (valor * 2.70) - desconto
    elif valor > 25:
        desconto = 0.05 * valor
        total = (valor * 2.70) - desconto
    else:
        return 'Inválido!'
    
    print(f'Combustível: Álcool')
    print(f'Litros: {valor} Litros')
    print(f'Desconto: R${desconto:.2f}')
    print(f'Total: R${total:.2f}')
