while True:            
    notas = input("Digite as notas separadas por espaço: ").split()
    
    if not all(nota.isdigit() for nota in notas):
        print("Valor invalido encontrado")
        print("tente novamente")
        continue
    
    if len(notas) == 0:
        print("Nenhuma nota foi informada.")
        print("tente novamente")
        continue

    notas_list = list(map(float, notas))

    if any(nota < 0 or nota > 10 for nota in notas_list):
        print("As notas devem estar entre 0 e 10")
        print("tente novamente")
        continue

    break
media = sum(notas_list) / len(notas_list)

if media >= 7:
    status = "aprovado"
elif media >= 5:
    status = "em recuperação"
else: 
    status = "reprovado"

print(f"A média é {media:.2f} e o aluno está {status}.")
