
x = int(input("Digite um valor: "))
y = int(input("Digite um segundo valor: "))

limite_inferior = min(x, y) 
limite_superior = max(x, y) 

soma_pares = 0

print("Números pares no intervalo aberto:")

for numero in range(limite_inferior + 1, limite_superior):
    if numero % 2 == 0:  # Verifica se o número é divisível por 2 (ou seja, par)
        print(numero, end=" ")
        soma_pares += numero
    
        
print(f"\nSomatório dos números pares: {soma_pares}") # \n tem 
