palavra = str(input("Digite uma palavra:"))
vogais = "aeiouAEIOU"
quant_vogais = sum(1 for letra in palavra if letra in vogais)
quant_consoantes = sum(1 for letra in palavra if letra not in vogais and letra.isalpha())
print(f"A palavra {palavra} tem {quant_vogais} vogais e {quant_consoantes} consoantes.")
