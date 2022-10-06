DNA = input("Digite a serie de DNA :")
'''
A=T
T=A
C=G
G=C
'''
for i in DNA:
    if (i == "A"):
        print("T", end=(""))
    elif(i == "T"):
        print("A", end=(""))
    elif(i == "C"):
        print("G", end=(""))
    elif(i == "G"):
        print("C", end=(""))