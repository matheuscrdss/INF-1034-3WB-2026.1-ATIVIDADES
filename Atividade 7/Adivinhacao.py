import random as rd

def usuario_joga():
    print("======= Jogo da adivinhaçao =======")

    num = rd.randint(1, 1023)
    tentativas = 0
    while True:
        chute = int(input("Digite um numero de 1 a 1023: "))
        tentativas += 1

        if num == chute:
            print(f"0, Parabens voce acertou em {tentativas} tentativas!")
            break
        elif num > chute:
            print("1, numero maior!")
        elif num < chute:
            print("-1, numero menor!")


def computador_joga():
    menor = 1
    maior = 1023
    tentativas = 0
    
    print("======= Jogo da adivinhaçao =======")
    print("Pense em um número entre 1 e 1023.")

    while True:
        palpite = (menor + maior) // 2
        tentativas += 1

        print(f"O computador chutou: {palpite}")
        resposta = int(input("Digite -1 se seu número é menor, 1 se é maior, ou 0 se acertou: "))

        if resposta == -1:
            maior = palpite - 1
        elif resposta == 1:
            menor = palpite + 1
        elif resposta == 0:
            print(f"O computador acertou em {tentativas} tentativas!")
            break

print("""Quem vai tentar adivinhar?
Usuario [1]
Computador [2]""")

escolha = int(input("\nDigite sua escolha: "))

if escolha == 1:
    usuario_joga()
else:
    computador_joga()