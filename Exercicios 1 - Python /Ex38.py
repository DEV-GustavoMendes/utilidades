
# São bissextos os anos: 1600, 1996, 2000, 2004, 2008, 2012, 2016, 2400, 2800, ... 
# Não são bissextos: 1500, 1974, 1982, 1983, 1990, 2018, 2022, 2030, 2038, ... 

def verificar_ano(ano):
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    if bissexto:
        print(f"O ano {ano} é Bissexto")
    else:
        print(f"O ano {ano} não é Bissexto")


verificar_ano(1600)