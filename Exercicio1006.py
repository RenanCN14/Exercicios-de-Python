#Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
#A seguir, calcule a média do aluno,
# sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. 
#Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

a=float(input())
b=float(input())
c=float(input())

a=a*2
b=b*3
c=c*5

a
med=(a+b+c)/10

print(f'MEDIA = {med:.1f}')