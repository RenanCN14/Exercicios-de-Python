L = int(input('Digite a quantidade de litros de suco necessaria'))
A = int(input('Digite o percentual concentrado de �gua'))
S = int(input('Digite o percentual concentrado de suco'))

PA = L/100*A
PS = L/100*S

if(A + S != 100):
    print('Valor de concentra��o incorreto processo finalizdo')
else:
    print(f'Ser� necessario para fazer {L} litros de suco de maracuja:')
    print(f'{PA:.2f} litros de �gua')
    print(f'{PS:.2f} litros de suco')
