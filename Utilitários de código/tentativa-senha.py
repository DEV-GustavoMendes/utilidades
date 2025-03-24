# Tentativa de Senha
senha_correta = 0000
senha_digitada = int(input('Digite uma senha com 4 numeros inteiros: '))
 
while senha_correta != senha_digitada:
    print('Senha incorreta.')
    senha_digitada = int(input('Digite a senha novamente: '))
else:
    print('Senha correta.')