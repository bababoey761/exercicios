numero = list(map(int, input("Digite dez numeros: ").split()))
if len(numero) != 10:
    print("Você deve digitar exatamente 10 números.")
    exit()
numero.sort(reverse=True)
print("Os números em ordem decrescente são:", numero,)