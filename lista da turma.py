lista = []
sair = 0
nome = ()
def aula():
    print(f"lista da turma: {lista}")
    nome = input("Digite o nome que deseja adicionar a lista:")
    lista.append(nome)
    return lista
    
def excluir():
    print(f"lista da turma: {lista}")
    nome = input("Digite o nome que deseja remover da lista:")
    lista.remove(nome)
    return lista
def main():
    if len(lista) == 0:
        aula()

    print("Estamos em aula")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("Digite 0 para sair\n")
    sair = (input("Digite uma opção: "))

    try: sair = float(sair)
    except ValueError:
        print("\nVALOR INVALIDO ENCONTRADO")
        print("tente novamente\n")
        
    if sair == 2:
            excluir()
    if sair == 1:
            aula()
    if sair == 0:
        exit(f"A lista da turma é : {lista}")
           

while True:
    main()
    
