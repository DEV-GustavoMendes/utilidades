def serie_fetuccine(primeiro_termo, segundo_termo, quantidade_termos):

  serie = [primeiro_termo, segundo_termo]

  if quantidade_termos < 3:
    return "A quantidade de termos deve ser no mínimo 3."

  for i in range(2, quantidade_termos):
    if i % 2 == 1:  # Se o índice for ímpar
      proximo_termo = serie[i - 1] + serie[i - 2]
    else:  # Se o índice for par
      proximo_termo = serie[i - 1] - serie[i - 2]
    serie.append(proximo_termo)

  return serie

# Exemplo de uso
primeiro_termo = int(input("Digite o primeiro termo: "))
segundo_termo = int(input("Digite o segundo termo: "))
quantidade_termos = int(input("Digite a quantidade de termos: "))

resultado = serie_fetuccine(primeiro_termo, segundo_termo, quantidade_termos)
print(f"Série de Fetuccine: {resultado}")