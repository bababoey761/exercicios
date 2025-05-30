valor_compra = float(input("Digite o valor de compra do produto: R$ ")) #Se é aplicando float em valor com (.) ou (,)

def calcular_valor_venda(valor_compra):
    if valor_compra <= 0: #Verifica se o valor é valido
        print("Digite um valor valido!")
        exit()

    #Verifica as condições para a aplicação das porcentagens
    if valor_compra < 10.00:  
        lucro = 1.70 
    elif 10.00 <= valor_compra < 30.00:
        lucro = 1.50  
    elif 30.00 <= valor_compra < 50.00:
        lucro = 1.40 
    else:  # valor_compra >= 50.00
        lucro = 1.30 
    valor_venda = valor_compra * (lucro)
    return valor_venda

valor_venda = calcular_valor_venda(valor_compra) #Calcula o valor de venda após o lucro ser aplicado
valor_renda = (valor_venda) - (valor_compra) #Calcula o lucro em comparação com valor antigo

print(f"O valor de venda do produto é: R$ {valor_venda:.2f}") 
print(f"tendo como renda o valor: R$ {valor_renda:.2f}")
