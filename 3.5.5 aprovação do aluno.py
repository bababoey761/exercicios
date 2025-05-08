
def media_notas():
    quantidade = 0
    soma_notas = 0
    while True:
        print("Digite as notas (digite 0 para finalizar):")
        nota = input("nota: ")
        print()

        try: nota = float(nota)
        except ValueError:
            print("VALOR INVALIDO ENCONTRADO")
            print("tente novamente\n")
            continue

        if nota == 0:
            if quantidade == 0:
                print("NENHUMA NOTA FOI INFORMADA")
                print("tente novamente")
                continue
            break

        if nota < 0 or nota > 10:
            print("AS NOTAS DEVEM ESTAR ENTRE 0 E 10")
            print("tente novamente\n")
            continue
        soma_notas += nota
        quantidade += 1
        
    return soma_notas / quantidade

media = media_notas()


if media >= 7:
    status = "aprovado"
elif media >= 5:
    status = "em recuperação"
else: 
    status = "reprovado"

print(f"A média é {media:.2f} e o aluno está {status}.")
