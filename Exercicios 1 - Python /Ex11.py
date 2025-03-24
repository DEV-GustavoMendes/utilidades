# Faça um algoritmo para calcular a nota semestral de um aluno.
# A nota semestral é obtida pela média aritmética entre a nota de 2 bimestres.
# Cada nota de bimestre é composta por 2 notas de provas.

def calcular_media(prova1, prova2, prova3, prova4):
    fBimestre = (prova1 + prova2) / 2
    sBimestre = (prova3 + prova4) / 2

    nota_semestral = (fBimestre + sBimestre) / 2 
    print(f"Nota semestral: {nota_semestral}")

calcular_media(50, 80, 70, 90)
