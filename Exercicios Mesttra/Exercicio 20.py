pao = int(input('Digite á quantidade de paes vendidos'))

broa = int(input('Digite á quantidade de broa vendidos'))

ref = float(input('Digite o valor da reforma'))


valorpao = pao*0.12

valorbroa = broa*1.50

lucro= valorbroa+valorpao

print(f'Faturamento com a venda de broas: {valorbroa:.2f}')

print(f'Faturamento com a venda de pães: {valorpao:.2f}')

print(f'Faturmento diario (paes + broas): {lucro:.2f}')

print(f'Valor do deposito da poupança: {lucro/100*10:.2f}')

print(f'Para pagar a reforma serão necessarios: {round(ref/(lucro/100*10)):.2f} dias')


dias = round(ref/(lucro/100*10))


if(dias>120):

    print(f'Para realizar a reforma em 120 dias sera necessario depositar diariamente R$: {round(ref/120):.2f}')