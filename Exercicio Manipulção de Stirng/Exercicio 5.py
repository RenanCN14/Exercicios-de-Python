frase = str(input('Digite uma frase: '))
string = frase[::-1]


if frase.lower() == string.lower():
    print("A frase é um palíndromo")
    print('A frase que você digitou invertida fica: {}'.format(string.lower()))
else:
    print("A frase não é um palíndromo")
    print('A frase que você digitou invertida fica: {}'.format(string.lower()))