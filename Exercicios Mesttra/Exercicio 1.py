frente = float(input('Quantos metros o terreno possui de frente?'))

lateral = float(input('Quantos metros o terreno possui de lateral?'))

valor = float(input('Informe o valor do metro quadrado'))


A = float(frente * lateral)

R = float(A * valor)

if(abs(frente-lateral)<(frente/100*10)):

    print(f'Area total do terreno de {frente:.2f} mts de frente com {lateral:.2f} mts de lateral e: {A:.2f}')

    print(f'O terreno recebeu um acrecimo e 22% e custara R$ {R+(R/100*22):.2f}')

elif(frente<(lateral/100*40)):

    print(f'Area total do terreno de {frente:.2f} mts de frente com {lateral:.2f} mts de lateral e: {A:.2f}')

    print(f'O terreno recebeu um desconto de 12% e cutara R$ {R-(R/100*12)}')

elif(frente>(lateral/100*70)):

    print(f'Area total do terreno de {frente:.2f} mts de frente com {lateral:.2f} mts de lateral e: {A:.2f}')

    print(f'O terreno recebeu um desconto de 15% e custara R$ {R-(R/100*15)}')

else:
    
    print(f'Area total do terreno de {frente:.2f} mts de frente com {lateral:.2f} mts de lateral e: {A:.2f}')

    print(f'O terreno não recebeu nenhuma alteração e custra: R$ {R:.2f}')