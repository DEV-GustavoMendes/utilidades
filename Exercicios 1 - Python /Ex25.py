def verificar_dias(n):
    dict = {
        1: ["Janeiro", "31 Dias"],
        2: ["Fevereiro", "28 Dias"],
        3: ["Março", "31 Dias"],
        4: ["Abril", "30 Dias"],
        5: ["Maio", "31 Dias"],
        6: ["Junho", "30 Dias"],
        7: ["Julho", "31 Dias"],
        8: ["Agosto", "31 Dias"],
        9: ["Setembro", "30 Dias"],
        10 :["Outubro", "31 Dias"],
        11 :["Novembro", "30 Dias"],
        12: ["Dezembro", "31 Dias"],
    }

    dia = dict.get(n)

    if dia:
        print(dia)
    else:
        print("Entrada Inválida")

verificar_dias(1)
