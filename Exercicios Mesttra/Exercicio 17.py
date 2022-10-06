hn = int(input('Digite a quantidade total de horas normal:'))

he = int(input('Digite a quantidade total de horas extra:'))

dep = int(input('Digite a quantidade total de dependentes:'))


hn = (hn*10)

he = (he*15)

depe = (dep*90)

dif = dep - 3


if(dep<=3 and dep>=0):

    print(f'Horas normais: R$ {hn:.2f}')

    print(f'Adicional Horas extra: R$ {he:.2f}')

    print(f'Adicional de Dependente R$ {depe:.2f}')

    print(f'Salario liquido (Hrs normal - Desconto): R$ {hn-(hn/100*11):.2f}')

    print(f'Salrio final: R$ {hn-(hn/100*11) + he + depe}')

elif(dep>3):

    print(f'Horas normais: R$ {hn:.2f}')

    print(f'Adicional Horas extra: R$ {he:.2f}')

    print(f'Adicional de Dependente R$ {depe - (90*dif):.2f}')

    print(f'Salario liquido (Hrs normal - Desconto: R$ {hn-(hn/100*11):.2f}')

    print(f'Salrio final: R$ {hn-(hn/100*11) + he + depe - (90*dif)}')

    print('Salario calculado paa apenas 3 dependentes.')

    print(f'Os demais {dif:.0f} dependentes não receberão o auxilio')