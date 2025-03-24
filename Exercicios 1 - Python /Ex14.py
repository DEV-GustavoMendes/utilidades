
def calcular_tempo_semaforo(distancia, velocidade, aceleracao, margem):
    t1 = velocidade / aceleracao
    d1 = (velocidade ** 2) / (aceleracao * 2)
    d2 = distancia - d1
    if d2 > 0:
        t2 = d2 / velocidade
    else:
        t2 = 0

    tempo_total = t1 + t2
    tempo_semaforo = tempo_total - margem

    print(f'Distância entre os semáforos: {distancia} metros.')
    print(f'Velocidade permitida na via: {velocidade} m/s.')
    print(f'Aceleracao típica do carro: {aceleracao} m/s².')
    print(f'Margem de antecipação (padrão = 3 segundos): {margem} segundos.')
    print(f'O próximo semáforo deve abrir {tempo_semaforo:.2f} segundos')


calcular_tempo_semaforo(200, 15, 2, 3)
