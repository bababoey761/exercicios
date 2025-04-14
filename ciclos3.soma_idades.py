soma_idades = 0
quantidade = 0

print("Digite as idades (digite 0 para finalizar):")

while True:
    idade = int(input("Idade: "))
    if idade == 0:  # Condição de parada
        break
    soma_idades += idade  # Soma as idades
    quantidade += 1  # Conta a quantidade de idades

# Verifica se alguma idade foi digitada
if quantidade > 0:
    media = soma_idades / quantidade
    print(f"A média das idades é: {media:.2f}")
else:
    print("Nenhuma idade válida foi digitada.")