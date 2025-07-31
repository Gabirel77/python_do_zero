# Exercicios de lista pag53
# a) imprima o maior elemento
# b) imprima o menor elemento
# c) imprima os números pares
# d) imprima o número de ocorrências do primeiro elemento da lista
# e) imprima a média dos elementos
# f) imprima a soma dos elementos de valor negativo

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
media =0
soma_negativos = 0
print("O maior valor da lista eh",max(lista))
print("O menor valor da lista eh",min(lista))

print("\n Valores pares na lista:")
for valor in lista:
    media = media + valor
    if valor %2 ==0:
        print(valor)
    if valor<0:
        soma_negativos=soma_negativos+valor

print("\nTem {} ocorrencias do primeiro elemento na lista".format(lista.count(lista[0])))

print("\nA media dos elementos eh igual a", media/len(lista))

print("\nA soma dos valores negativos eh igual a", soma_negativos)