
assiduidade = float(input("Digite a assiduidade do aluno (em %): "))
nota = float(input("Digite a nota do aluno (de 0 a 20): "))

if (assiduidade < 0 or assiduidade > 100) and (nota < 0 or nota > 20):
    print("Ambas informações estão inválidas")
    exit()
elif 0 <= assiduidade < 75:
    situacao = "Reprovado"
elif 75 <= assiduidade <= 100:
    if 0 < nota <= 5:
        situacao = "Reprovado"
    elif 5 < nota <= 9.5:
        situacao = "Exame"
    elif 10 <= nota <= 20:
        situacao = "Aprovado"
    else:
        print("Nota inválida")
        exit()
else:
    print("Assiduidade inválida")
    exit()


print(f"A situação do aluno é: {situacao}")