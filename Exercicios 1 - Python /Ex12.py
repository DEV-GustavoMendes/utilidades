# Faça um algoritmo que transforme uma velocidade fornecida em m/s pelo usuário para Km/h. Para tal, multiplique o valor em m/s por 3,6.  

def toKMH(velocidade):
    mhs = velocidade * 3.6
    print(f"A velocidade {velocidade} m/s equivale a {mhs:.2f} Km/H")

toKMH(60)