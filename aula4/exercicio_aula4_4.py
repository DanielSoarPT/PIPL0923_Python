# Peça ao utilizador 10 valores numéricos
# Verifique se o valor e numérico, se não for descarte esse valor
# Adicione a lista os valores numéricos 
# Calcule a media dos valores na lista

valores = []
contador = 0

while contador < 10:
    entrada = input(f"Digite o {contador + 1}º valor numérico: ")
    
    try:
        valor = float(entrada)
        valores.append(valor)
        contador += 1
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

media = sum(valores) / len(valores)
print(f"\nLista de valores válidos: {valores}")
print(f"A média dos valores é: {media}")