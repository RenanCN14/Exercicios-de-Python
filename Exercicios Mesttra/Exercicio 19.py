fat = float(input('Digita o valor do faturmento anterior'))
prod = int(input('Digite o c�digo do produto que deseja bater meta'))
if(prod == 101):
    pro = 1
    prec = 150
elif(prod == 122):
    pro = 2
    prec = 220
elif(prod == 163):
    pro = 3
    prec = 97

if(prod == 101 or prod == 122 or prod == 163):
   print(f'A meta do proximo m�s � : R$ {fat + (fat/100*20):.2f}') 
   print(f'Um aumento de : R$ {fat/100*20:.2f}')
   print('Quantidade de pe�as a serem vendidas para atingirmos a meta:')
   print(f'Produto {pro}: {(fat/100*20)/prec:.2f} pe�as')
else:
    print('C�dio do produto n�o encontrado')
