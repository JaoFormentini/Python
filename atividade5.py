

y = int(input("Digite a quantidade de notas: "))
media = 0
for x in range (y):
    nota = float(input("Digite a nota: "))

    media += nota

notatotal = media/y 
if (notatotal >= 7):
    print("Sua media é {:.2f} Aprovado".format(notatotal))
else:
    print("Sua media é {:.2f} Reprovado".format(notatotal))