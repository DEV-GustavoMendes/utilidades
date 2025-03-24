def verificar():
    soma = int(input('Digite um valor para soma (entre 2 e 12): '))
    for dado1 in range(1,7):
        for dado2 in range(1,7):
            if dado1 + dado2 == soma:
                print(f'{dado1} {dado2}')

verificar()