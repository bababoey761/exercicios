list = {'n' ,'idade' ,'esp'}
especiais = ["gestante", "pcd"]
prioridade = False
fila = []
porc = ()

def add():
   contador = 0
   contador_esp = 0
   while True:
    especial = False
    n = input('qual seu nome: ')
    idade = (input("digite sua idade: "))
    try: 
        idade = int(idade)
    except ValueError:
        print("idade invalida porfavor tente novamente")
        continue
    if idade <= 59:
        prioridade = False
    elif idade >= 60:
        prioridade = True
    while True:
        ness = input('você possui alguma necessidade? (escreva "n" para não ou "s" para sim): ').lower()
        if ness == "n":
            especial = False
            esp = "normal"
            break
        elif ness == "s":
            especial = True
            break
        else:
            print('resposta invalida, porfavor responda apenas com "n" para não ou "s" para sim: ')
            continue
    if especial:
        contador_esp += 1
        while True:
            esp = input('qual tipo de necessidade você tem? (gestante, pcd): ').lower()
            if esp in especiais:
                prioridade = True
                break
            else:
                print("Tipo de necessidade inválido. Tente novamente.")
                continue
    else:
        contador +=1
    list.add((n) (idade) (esp))
    if prioridade:
        pos = contador_esp 
        prio = True
        fila.append((prio, pos))
    else:
        pos = contador
        prio= False
        fila.append((prio, pos))
    if contador_esp >=1 and contador >=1:
        porcentagem = 100 / ((contador_esp + contador) / contador_esp)
    elif contador >=1 and contador_esp == 0:
        porcentagem = 100
    elif contador == 0 and contador_esp >=1:
        porcentagem = 100
    global porc 
    porc = porcentagem

    break

def mostrar():
   m_fila()
   print("\nFila de pessoas: \n")
   print(list, "\n")
def m_fila():
    fila.sort(reverse=True)
    print(fila)
    print(f"{porc}%")
def menu():
   while True:
      print(f"MENU\n")
      print("1 - Adicionar pessoa na fila")
      print("2 - mostrar fila")
      print("3 - Sair")
    
      op = (input("\nEscolha uma opção: "))
      opções = {'1' : add, '2' : mostrar, '3' : exit, '4' : m_fila}
      if op in opções:
         opções[op]()
      else:
         print("Opção inválida. Tente novamente.")
         continue
menu()
