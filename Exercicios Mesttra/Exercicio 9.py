valor = float(input('informe o valor da conta: R$'))

res = valor/3
resto = res - valor//3 

if(resto>=0.30):
    print(f'Carlos pagara: {res:.2f}')
    print(f'Andr� pagara: {res:.2f}')
    print(f'Felipe pagara: {res:.2f}')
elif(resto<0.30):
    print(f'Carlos pagara: {res - resto:.2f}')
    print(f'Andr� pagara: {res - resto:.2f}')
    print(f'Felipe pagara: {res + resto + resto:.2f}')
