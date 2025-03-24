# Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.
# OBS: Considere todos os anos possuindo 365 dias.

def calcular(idade):
    anos = idade
    meses = idade * 12
    dias = idade * 365

    print(f"Anos: {anos}\nMeses: {meses}\nDias: {dias}")

calcular(23)