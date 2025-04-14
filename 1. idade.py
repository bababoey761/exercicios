idade = int(input("Digite sua idade: ")) # Se é aplicado int em valores inteiros


if idade <= 4:
      print("Idade abaixa da cartegoria minima permitida")
      exit()
if idade >= 5 and idade <= 7:
     print("Sua categoria é: infantil")
elif idade >= 8 and idade <= 10:
     print("Sua categoria é: iniciado")
elif idade >= 11 and idade <= 13:
     print("Sua categoria é: juvenil")
elif idade >= 14 and idade <= 17:
     print("Sua categoria é: junior")
elif idade >= 18:
     print("Sua categoria é: senior")