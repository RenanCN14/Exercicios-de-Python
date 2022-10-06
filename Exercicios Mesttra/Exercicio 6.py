cav = int(input('Informe a quantidade de cavalos'))
fer = float(input('Informe o valor de cada ferradura'))

qferr = cav*4
print(qferr)
valor = qferr*fer
print(valor)
if(valor>=15000.01 and valor<= 20000):
    print(f'A quantidade de ferraduras necessárias: {qferr}')
    print(f'Valor total para a compra de ferraduras: R$ {valor - valor/100*10:.2f}')
elif(valor>=20000.01 and valor<= 25000.00):
    print(f'A quantidade de ferraduras necessárias: {qferr}')
    print(f'Valor total para a compra de ferraduras: R$ {valor - valor/100*12:.2f}')
elif(valor>=25000.01 and valor<= 30000):
    print(f'A quantidade de ferraduras necessárias: {qferr}')
    print(f'Valor total para a compra de ferraduras: R$ {valor - valor/100*15:.2f}')
elif(valor>30000):
    print(f'A quantidade de ferraduras necessárias: {qferr}')
    print(f'Valor total para a compra de ferraduras: R$ {valor - valor/100*20:.2f}')
else:
     print(f'A quantidade de ferraduras necessárias: {qferr}')
     print(f'Valor total para a compra de ferraduras: R$ {valor:.2f}')
