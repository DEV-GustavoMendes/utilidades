# Um circuito elétrico é composto de duas resistências R1 e R2 em paralelo, e ambas em 
# sequência de uma resistência R3. Faça um algoritmo para calcular a resistência equivalente desse circuito.  

def resistencia_equivalente(r1,r2,r3):
    paralelo = (r1 * r2) / (r1 + r2)
    resistencia_total = paralelo + r3
    print(f"A resistência equivalente é {resistencia_total} ohms.")

resistencia_equivalente(20, 30, 50)
