df = int(input('Digite o dia final:'))
mf = int(input('Digite o mês final:'))

if(mf == 1 and df>=1 and df<=31):
    print('Quantiade de dias:',df)
elif(mf==2 and df>=1 and df<=28):
    print('Quantiade de dias:',df+31)
elif(mf==3 and df>=1 and df<=31):
    print('Quantiade de dias:',df+59)
elif(mf==4 and df>=1 and df<=30):
    print('Quantiade de dias:',df+83)
elif(mf==5 and df>=1 and df<=31):
    print('Quantiade de dias:',df+120)
elif(mf==6 and df>=1 and df<=30):
    print('Quantiade de dias:',df+150)
elif(mf==7 and df>=1 and df<=31):
    print('Quantiade de dias:',df+181)
elif(mf==8 and df>=1 and df<=31):
    print('Quantiade de dias:',df+212)
elif(mf==9 and df>=1 and df<=30):
    print('Quantiade de dias:',df+242)
elif(mf==10 and df>=1 and df<=31):
    print('Quantiade de dias:',df+273)
elif(mf==11 and df>=1 and df<=30):
    print('Quantiade de dias:',df+304)
elif(mf==12 and df>=1 and df<=31):
    print('Quantiade de dias:',df+334)
else:
    print('Impossivel realizar  calculo. Anos e Meses inconsistentes' )
