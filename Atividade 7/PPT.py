import random as rd

escolhas = ["Pedra", "Papel", "Tesoura"]
pontuacao = 0

while True:
    escolha_computador = rd.randint(0,2)

    print("Pedra[0], Papel[1], Tesoura[2]")
    escolha_jogador = int(input("Digite sua escolha: "))

    print(f"Voce: {escolhas[escolha_jogador]}")
    print(f"Computador: {escolhas[escolha_computador]}")

    if escolha_jogador == 0 and escolha_computador == 1:
        print("Computador venceu!")
    elif escolha_jogador == 1 and escolha_computador == 2:
        print("Computador venceu!")
    elif escolha_jogador == 2 and escolha_computador == 3:
        print("Computador venceu!")
    elif escolha_jogador == 3 and escolha_computador == 1:
        print("Computador venceu!")
    else:
        print("Empate!")

    pontuacao += 1

    continuar = input("Deseja continuar? (s/n) ")

    if continuar in "Nn":
        print(f"A sua pontuaçao foi de {pontuacao}")
        break
        
