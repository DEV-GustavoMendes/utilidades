
def verificar():
    pop_a = 5000000
    pop_b = 7000000
    tn_a = 0.03
    tn_b = 0.02
    anos = 0

    while pop_a <= pop_b:
        pop_a += pop_a * tn_a 
        pop_b += pop_b * tn_b
        anos += 1
        
    print(f'Serão necessários {anos} anos.')

verificar()