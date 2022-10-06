val1 =int(input('informe o valor 1:'))
val2 = int(input('informe o valor 2:'))

if(val2 == 0 or val1==0):
    print('A operação nao pode ser realizada')
elif(val1>val2):
    print(f'A divisão de {val1} por {val2} é de {(val1/val2)}')
elif(val1<val2):
    print(f'A divisão de {val2} por {val1} é de {(val2/val1)}')
