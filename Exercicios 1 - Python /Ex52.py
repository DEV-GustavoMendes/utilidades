def Fetuccine(a1,a2,termos):
    
    serie = [a1, a2]
             
    if termos < 3:
        print("A quantidade de termos deve ser no mínimo 3.")
    else:
        pass

    for i in range(2, termos):
        if i % 2 == 1:  # Se o índice for ímpar
            proximo_termo = serie[i - 1] + serie[i - 2]
        else:  # Se o índice for par
            proximo_termo = serie[i - 1] - serie[i - 2]

        serie.append(proximo_termo)

    print(f"Série de Fetuccine: {serie}")

Fetuccine(3,4,11)
