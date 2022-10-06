#Leia quatro valores inteiros A, B, C e D. 
#A seguir, calcule e mostre a diferença do produto de A e B 
#pelo produto de C e D segundo a fórmula:
# DIFERENCA = (A * B - C * D).

a = int(input())
b = int(input())
c = int(input())
d = int(input())

ab=a*b
cd=c*d

diferenca=ab-cd

print('DIFERENCA =',diferenca)