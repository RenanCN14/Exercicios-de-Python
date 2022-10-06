N1 = float(input('Informe o valor da primeira nota'))

N2 = float(input('Informe o valor da segunda nota'))

N3 = float(input('Informe o valor da terceira nota'))

no1 = N1

no2 = N2*2

no3 = N3*3


no1 = float(no1)

no2 = float(no2)

no3 = float(no3)


med = (no1+no2+no3)/6

print(f'A média ponderada das notas {N1:.2f}, {N2:.2f} e {N3:.2f} é {med:.2f}')


if(no1>no2 and no1>no3):

    print(f'A nota 1({N1:.2f}) é a maior nota apos o cauculo de peso ({no1:.2f})')

elif(no2>no1 and no2>no3):

    print(f'A nota 2({N2:.2f}) é a maior nota apos o cauculo de peso ({no2:.2f})')

elif(no3>no1 and no3>no2):

    print(f'A nota 3({N3:.2f}) é a maior nota apos o cauculo de peso ({no3:.2f})')

elif(no1==no2 and no2==no3):

    print(f'As notas são iguais')

elif(no2==no1 and no2>no3):

    print(f'As notas 1 e 2({N1:.2f},{N2:.2f}) são as maiores notas apos calculo de peso ({no1:.2f},{no2:.2f})')

elif(no2==no3 and no3>no1):

    print(f'As notas 2 e 3({N2:.2f},{N3:.2f}) são as maiores notas apos calculo de peso ({no2:.2f},{no3:.2f})')

elif(no1==no3 and no3>no2):

    print(f'As notas 1 e 3({N1:.2f},{N3:.2f}) são as maiores notas apos calculo de peso ({no1:.2f},{no3:.2f})')