import random as rd

escolha_computador = rd.randint(1, 1023)

escolha = int(input("Digite seu chute: "))


while(True):
    if escolha > escolha_computador:
        print(("-1"))
    if escolha < escolha_computador:
        print(("1"))
    if escolha == escolha_computador:
        print(("0, acertou parabens!"))
        break
