fra = int(input('Digite a quantidade de frangos'))
ali = float(input('Digite o valor do chipe de alimentação'))
ide = float(input('Digite o valor do chipe de identificação'))

valorIde = fra* ide
valorAli = fra* (ali*2)

if(valorIde>valorAli and (valorIde-valorAli) <= valorIde/100*20):
    print('O valor total para identificar os frangos é:')
    print(f'Chip Alimentação = R$ {valorAli:.2f}')
    print(f'Chip Identificação = R$ {valorIde:.2f}')
    print(f' Adicional 20% = R$ {valorAli/100*20:.2f}')
    print(f'Valor total = R$ {valorAli+valorIde+(valorAli/100*20):.2f}')
elif(valorIde>valorAli and (valorIde-valorAli) > valorIde/100*20):
    print('O valor total para identificar os frangos é:')
    print(f'Chip Alimentação = R$ {valorAli:.2f}')
    print(f'Chip Identificação = R$ {valorIde:.2f}')
    print(f'Valor total = R$ {valorAli+valorIde:.2f}')
elif(valorIde<valorAli and (valorAli-valorIde) <= valorAli/100*20):
    print('O valor total para identificar os frangos é:')
    print(f'Chip Alimentação = R$ {valorAli:.2f}')
    print(f'Chip Identificação = R$ {valorIde:.2f}')
    print(f' Adicional 20% = R$ {valorIde/100*20:.2f}')
    print(f'Valor total = R$ {valorAli+valorIde+(valorIde/100*20):.2f}')
elif(valorIde<valorAli and (valorAli-valorIde) > valorAli/100*20):
    print('O valor total para identificar os frangos é:')
    print(f'Chip Alimentação = R$ {valorAli:.2f}')
    print(f'Chip Identificação = R$ {valorIde:.2f}')
    print(f'Valor total = R$ {valorAli+valorIde:.2f}')
