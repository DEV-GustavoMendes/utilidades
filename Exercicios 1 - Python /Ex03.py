# Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma. 

import math

def calcular(raio):
    area = math.pi * (raio ** 2)
    perimetro = 2 * math.pi * raio

    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

calcular(0)