print('Área do trapézio')
bmai = int(input('Informe a base maior do trapézio'))
bmen = int(input('Informe a base menor do trapézio'))
altTRA = int(input('Informe a altura'))

print('Área do quadrado')
lad = int(input('Informe o valor de un dos lados'))

print('Área do Retângulo')
larg = int(input('Informe a largura'))
altRET = int(input('Informe a altura'))

print('Área circulo')
rai = int(input('Infome o raio'))

print('Área do Triângulo')
base = int(input('Informe a base do triângulo'))
altTRI = int(input('Informe a altura do triângulo'))

atrapezio = (bmen+bmai)*altTRA/2
aquadrado = lad**2
aret = larg*altRET
acir = 3.14*rai*rai
atri = base*altTRI/2

print(f'Área do trapézio : {atrapezio:.2f}')
print(f'Área do quadrado : {aquadrado:.2f}')
print(f'Área do retangulo : {aret:.2f}')
print(f'Área do circulo : {acir:.2f}')
print(f'Área do trângulo : {atri:.2f}')

if(atrapezio > aquadrado and atrapezio > aret and atrapezio > acir and atrapezio > atri):
    print(f'O objeto com maior Área e o trapezio com {atrapezio:.2f} de area.')
elif(aquadrado > atrapezio and aquadrado > aret and aquadrado > acir and aquadrado > atri):
    print(f'O objeto com maior Área e o quadrado com {aquadrado:.2f} de area.')
elif(aret > atrapezio and aret > aquadrado and aret > acir and aret > atri):
    print(f'O objeto com maior Área e o retangulo com {areto:.2f} de area.')
elif(acir > atrapezio and acir > aquadrado and acir > aret and acir > atri):
    print(f'O objeto com maior Área e o circulo com {acir:.2f} de area.')
elif(atri > atrapezio and atri > aquadrado and atri > aret and atri > acir):
    print(f'O objeto com maior Área e o triangulo com {atri:.2f} de area.')
