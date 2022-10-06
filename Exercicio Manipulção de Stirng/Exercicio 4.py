frase = input("Digite a frase :").strip()
qtdFrase = 1
qtdCarac = 0
for i in frase:
    if i == " ":
        qtdFrase += 1
    qtdCarac += 1
print(f"A quantidade de caracteres é {qtdCarac}")
print(f"A quantidade de Frases é {qtdFrase}")