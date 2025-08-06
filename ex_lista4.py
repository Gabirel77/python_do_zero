nome = input ("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
dicionario = dict(nome = nome, idade = idade, cidade = cidade)

for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")