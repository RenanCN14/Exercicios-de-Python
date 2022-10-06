num = int(input('Digite um número de até 4 digitos'))

mil = num//1000
cem = num%1000
dez = num%100
uni = num%10

dez = dez //10
cem = cem//100
if(num<=9999 and num>=1000):
    print('Milhares:',mil)
    print ('Centena:',cem)
    print('Dezeana:',dez)
    print('Unidade:',uni)
elif(num<=999 and num>=100):
    print ('Centena:',cem)
    print('Dezeana:',dez)
    print('Unidade:',uni)
elif(num<=99 and num>=10):
    print('Dezeana:',dez)
    print('Unidade:',uni)
elif(num<=9 and num>=0):
    print('Unidade:',uni)
else:
    print('Número invalido!')
