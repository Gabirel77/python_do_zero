print('******************************')
print('* Jogo da adivinhacao *')
print('******************************')

numero_secreto=42
total_tentativas=20
rodada=1
nivel=1
pontos=1000
print("Escolha um nivel pra jogar:\n1(facil),\n2,\n3(dificil)\n")
x = int(input())
if x == 2:
    total_tentativas =10
    nivel=2
elif x ==3:
    total_tentativas=5
    nivel=3

print("Nivel:{}\n".format(nivel))
for rodada in range(1,total_tentativas+1):
    chute = int(input("Digite um valor\n"))
    print("Voce digitou: ", chute)
    acertou=chute==numero_secreto
    maior=chute>numero_secreto
    menor=chute<numero_secreto
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    if acertou:
        print("\nVoce acertou!\n")
        break
    elif maior:
        print("Numero maior que o secreto\n")
        pontos=pontos-abs(chute-numero_secreto)
    elif menor:
        print("Numero menor que o secreto\n")
        pontos=pontos-abs(chute-numero_secreto)
    
print("Vc fez {} pontos!".format(pontos))
print("Fim de jogo!")