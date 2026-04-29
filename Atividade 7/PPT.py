import random as rd

escolhas = ["Pedra", "Papel", "Tesoura"]

def ppt():
    pontuacao = 0
    while True:
        escolha_computador = rd.randint(0,2)

        print("\nPedra[0], Papel[1], Tesoura[2]")
        escolha_jogador = int(input("Digite sua escolha: "))

        print(f"Voce: {escolhas[escolha_jogador]}")
        print(f"Computador: {escolhas[escolha_computador]}\n")

        if escolha_jogador == escolha_computador:
            print("Empate!")

        elif ( 
            (escolha_jogador == 0 and escolha_computador == 2) or 
            (escolha_jogador == 1 and escolha_computador == 0) or
            (escolha_jogador == 2 and escolha_computador == 1)
            ):
            print("Voce venceu!")
            pontuacao += 1
        else: 
            print("Computador venceu!")

        continuar = input("Deseja continuar? (s/n) ")

        if continuar.lower() == "n":
            print("\nJogo encerrado!")
            print(f"A sua pontuaçao foi de {pontuacao}")
            break
            
ppt()