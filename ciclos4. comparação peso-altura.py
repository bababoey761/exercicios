# Entrada de dados para a primeira pessoa
nome1 = input("Digite o nome da primeira pessoa: ")
altura1 = float(input("Digite a altura da primeira pessoa (em metros): "))
peso1 = float(input("Digite o peso da primeira pessoa (em kg): "))

# Entrada de dados para a segunda pessoa
nome2 = input("Digite o nome da segunda pessoa: ")
altura2 = float(input("Digite a altura da segunda pessoa (em metros): "))
peso2 = float(input("Digite o peso da segunda pessoa (em kg): "))

# Determina a pessoa mais pesada
if peso1 > peso2:
    mais_pesada = nome1
else:
    mais_pesada = nome2

# Determina a pessoa mais alta
if altura1 > altura2:
    mais_alta = nome1
else:
    mais_alta = nome2

# Exibe os resultados
print(f"A pessoa mais pesada é: {mais_pesada}")
print(f"A pessoa mais alta é: {mais_alta}")