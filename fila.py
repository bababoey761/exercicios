# uma fila (joaquim)

especiais = ["gestante", "pcd", "outro"]
fila = []

def add(): 
   contador = 0
   contador_esp = 0
   while True:
    especial = False
    prioridade = False
    n = input('qual seu nome: ')
    idade = (input("digite sua idade: "))
    try: 
        idade = int(idade)
    except ValueError:
        print("idade invalida por favor tente novamente")
        continue
    if idade >= 60:
        prioridade = True
        esp = "Acima de 60"
    while True:
        ness = input('você possui alguma necessidade? (escreva "n" para não ou "s" para sim): ').lower()
        if ness == "n":
            especial = False
            break
        elif ness == "s":
            especial = True
            break
        else:
            print('resposta invalida, por favor responda apenas com "n" para não ou "s" para sim: ')
            continue
    if especial:
        contador_esp += 1
        while True:
            esp = input('Porvafor digite qual sua necessidade (gestante, pcd ou outro): ').lower()
            if esp in especiais:
                prioridade = True
                break
            else:
                print("Tipo de necessidade inválido. Tente novamente.")
                continue
    elif not prioridade:
        contador +=1
        esp = "nenhum"
    fila.append((prioridade, len(fila), n, idade, esp))
    break
   
def mostrar():
    fila.sort(reverse=True)
    print("\nFila de pessoas: \n")
    for i, pessoa in enumerate(fila, start=1):
        print(f"{i} - {pessoa[2]} - Idade: {pessoa[3]} - Necessidade: {pessoa[4]} - Prio: {'Sim' if pessoa[0] else 'Não'}")
    
    priori = sum(1 for pessoa in fila if pessoa[0])
    porcentagem = (priori / len(fila)) * 100

    print(f"\n    {porcentagem}% são prioritários")
def m_fila():
    #debug da fila
    fila.sort(reverse=True)
    print (fila)

def menu():
   while True:
      print(f"\n -----------// MENU //-----------\n")
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
