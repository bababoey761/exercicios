list = []
especiais = ["gestante", "pcd"]
prioridade = False
esp1 = []

def add():
   contador = 0
   while True:
      especial = False
      n = input('qual seu nome: ')
      idade = int(input("digite sua idade: "))
      if idade <= 59:
         prioridade = False
      elif idade >= 60:
         prioridade = True

      ness = input('você possui alguma necessidade? (escreva "n" para não e "s" para sim): ').lower()
      if ness == "n":
         especial = False
         esp = "normal"
      elif ness == "s":
         especial = True

      if especial:
         contador += 1
         while True:
               esp = input('qual tipo de necessidade você tem? (gestante, pcd): ').lower()
               if esp in especiais:
                  prioridade = True
                  break
               else:
                  print("Tipo de necessidade inválido. Tente novamente.")
      list.append((n, idade, esp))
      break
def mostrar():
   print("\nFila de pessoas: \n")
   print(list, "\n")

def menu():
   while True:
      print(f"MENU\n")
      print("1 - Adicionar pessoa na fila")
      print("2 - mostrar fila")
      print("3 - Sair")
      op = (input("\nEscolha uma opção: "))
      opções = {'1' : add, '2' : mostrar, '3' : exit}
      if op in opções:
         opções[op]()
      else:
         print("Opção inválida. Tente novamente.")
         continue
menu()
