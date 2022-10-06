texto = input('Digite sua frase :').upper()
textocifrado = ""

alfabeto ="ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"

for letra in texto:
    localizacao = alfabeto.find(letra)
    if localizacao >= 0:
        novalocalizacao = localizacao+3
        textocifrado += alfabeto[novalocalizacao]
    else:
        textocifrado += letra
print(textocifrado)