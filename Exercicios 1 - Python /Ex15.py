
def altura_predio(altura_pessoa, sombra_pessoa, sombra_predio):
    altura = (altura_pessoa * sombra_predio) / sombra_pessoa
    print(f"Altura do prédio: {altura} metros")

altura_predio(2,4,40)