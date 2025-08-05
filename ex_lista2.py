informacoes = []
nome = input("Digite seu nome: ")
informacoes.append(nome);
sobrenome = input("Digite seu sobrenome: ")
informacoes.append(sobrenome)
idade = int(input("Digite sua idade: "))
informacoes.append(idade)

for i in informacoes:
    print(i)