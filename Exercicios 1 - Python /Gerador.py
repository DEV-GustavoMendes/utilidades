import os

def criar_arquivos_python(numero_arquivos=100):
    for i in range(1, numero_arquivos + 1):
        nome_arquivo = f"Ex{i:02d}.py"  # Formata o nome para ter dois dígitos
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("# Este é um arquivo de exemplo.")  # Conteúdo do arquivo
        print(f"Arquivo {nome_arquivo} criado com sucesso.")

if __name__ == "__main__":
    criar_arquivos_python()