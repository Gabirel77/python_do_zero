notas = input("Digite as notas separadas por espaço: ").split()
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
print("A média das notas é: {}".format(media))
