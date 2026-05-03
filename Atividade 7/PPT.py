import random as rd

def ppt():
    vitorias_usuario = 0

    while True:
        escolha_computador = rd.randint(0, 2)

        print("\nPedra [1], Papel [2], Tesoura [3]")
        escolha_usuario = int(input("Faça sua escolha: "))

        if escolha_usuario == escolha_computador:
            print("Empate!")

        elif (
            (escolha_usuario == 0 and escolha_computador == 2) or
            (escolha_usuario == 1 and escolha_computador == 0) or
            (escolha_usuario == 2 and escolha_computador == 1)
        ):
            print("Você venceu!")
            vitorias_usuario += 1

        else:
            print("Computador venceu!")

        print(f"Vitórias do usuário: {vitorias_usuario}")

        continuar = input("\nDeseja continuar? (s/n): ").lower()

        if continuar == "n":
            break

ppt()