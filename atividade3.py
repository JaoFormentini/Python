
x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
z = float(input("Digite a terceira nota: "))
a = float(input("Digite a quarta nota: "))

media = (x+y+z+a)/4

if (media >= 7):
    print("Sua media é {:.2f} Aprovado".format(media))
else:
    print("Sua media é {:.2f} Reprovado".format(media))