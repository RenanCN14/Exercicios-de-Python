san = int(input('Digite a quantidade de sanduiches:'))

q = 100
p = 50
ham = 120
m = 70

qt = q*san
pt = p*san
ht = ham*san

print(f'Para produzir {san} sanduiches será necessario:')
print(f'{qt/1000:.3f} kgs de mussarela')
print(f'{pt/1000:.3f} kgs de presunto')
print(f'{ht/1000:.3f} kgs de hamburger')

presuntoDisponivel = float(input('Qual a quantidade em kgs disponivel de presunto?'))

if(presuntoDisponivel <= pt):
    print(f'Será  possível produxir apenas {(presuntoDisponivel*1000)/50:.0f} sanduiches com presunto')
    print(f'Será necessario {m/1000*abs((presuntoDisponivel*1000)/50 - san):.3f} kgs de mortadela para produzir {abs((presuntoDisponivel*1000)/50 - san):.0f} sanduiches restantes')
    print(f'Da quantidae de presunto disponivel sobrara 0.000 kgs')
