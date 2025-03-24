import math

def second_degree_equation(a,b,c):
    delta = (b**2) - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a

    if delta > 0:
        print(f"A equação possui duas raízes inteiras: {x1} e {x2}")
    
    elif delta == 0:
        print(f"A equação possui duas raízes igual: {x2}")
    
    elif delta < 0:
        print("A equação não possui raízes reais!")
    else:
        print("Erro!")


second_degree_equation(1, 14, 49)