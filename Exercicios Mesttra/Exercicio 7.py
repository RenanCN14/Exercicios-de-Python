peso = float(input("Informe seu peso os KG:"))
peso15 = (peso/100*15)
peso20 = (peso/100*20)

print('Caso a pessoa engorde 15% ficara com;',peso+peso15)
print('Caso a pessoa engorde 20% ficara com;',peso+peso20)

if(abs(peso15-peso20) >= 4.5 ):
    print('Voce deve procurar um nutricionista')
