#Escreva um programa que leia o número de um funcionário,
# seu número de horas trabalhadas,
# o valor que recebe por hora e calcula o salário desse funcionário.
# A seguir, mostre o número e o salário do funcionário,
# com duas casas decimais.

cod = int(input())
hor = int(input())
salH  = float(input())

salario=salH*hor

print('NUMBER =',cod)
print(f'SALARY = U$ {salario:.2f}')