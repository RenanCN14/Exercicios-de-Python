print('�rea do trap�zio')
bmai = int(input('Informe a base maior do trap�zio'))
bmen = int(input('Informe a base menor do trap�zio'))
altTRA = int(input('Informe a altura'))

print('�rea do quadrado')
lad = int(input('Informe o valor de un dos lados'))

print('�rea do Ret�ngulo')
larg = int(input('Informe a largura'))
altRET = int(input('Informe a altura'))

print('�rea circulo')
rai = int(input('Infome o raio'))

print('�rea do Tri�ngulo')
base = int(input('Informe a base do tri�ngulo'))
altTRI = int(input('Informe a altura do tri�ngulo'))

atrapezio = (bmen+bmai)*altTRA/2
aquadrado = lad**2
aret = larg*altRET
acir = 3.14*rai*rai
atri = base*altTRI/2

print(f'�rea do trap�zio : {atrapezio:.2f}')
print(f'�rea do quadrado : {aquadrado:.2f}')
print(f'�rea do retangulo : {aret:.2f}')
print(f'�rea do circulo : {acir:.2f}')
print(f'�rea do tr�ngulo : {atri:.2f}')

if(atrapezio > aquadrado and atrapezio > aret and atrapezio > acir and atrapezio > atri):
    print(f'O objeto com maior �rea e o trapezio com {atrapezio:.2f} de area.')
elif(aquadrado > atrapezio and aquadrado > aret and aquadrado > acir and aquadrado > atri):
    print(f'O objeto com maior �rea e o quadrado com {aquadrado:.2f} de area.')
elif(aret > atrapezio and aret > aquadrado and aret > acir and aret > atri):
    print(f'O objeto com maior �rea e o retangulo com {areto:.2f} de area.')
elif(acir > atrapezio and acir > aquadrado and acir > aret and acir > atri):
    print(f'O objeto com maior �rea e o circulo com {acir:.2f} de area.')
elif(atri > atrapezio and atri > aquadrado and atri > aret and atri > acir):
    print(f'O objeto com maior �rea e o triangulo com {atri:.2f} de area.')
