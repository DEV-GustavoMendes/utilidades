def verificar_letra():
    letra = input("Informe uma letra: ").lower()

    vogal = ['a','e','i','o','u']
    
    if letra in vogal:
        print("A letra é VOGAL")
    else:
        print("A letra é CONSOANTE")

verificar_letra()