val1 =int(input('informe o valor 1:'))
val2 = int(input('informe o valor 2:'))

if(val2 == 0 or val1==0):
    print('A opera��o nao pode ser realizada')
elif(val1>val2):
    print(f'A divis�o de {val1} por {val2} � de {(val1/val2)}')
elif(val1<val2):
    print(f'A divis�o de {val2} por {val1} � de {(val2/val1)}')
