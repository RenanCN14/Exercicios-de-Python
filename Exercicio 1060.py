a = float(input())
contador = 0
contPositivo = 1
while(a == 0):
    a = float(input())
while(a != 0):
    if(contador == 5):
        break
    if(a != 0 and a >0):
            contador += 1
            contPositivo += 1
    else:
        contador += 1
    a = float(input())
print(contPositivo,'valores positivos')