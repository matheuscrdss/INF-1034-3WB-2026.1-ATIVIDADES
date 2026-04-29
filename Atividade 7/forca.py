import random as rd

palavras = ["computador", "janela", "mistério", "oceano", "futebol", "biblioteca", "relâmpago", "caderno", "viagem", "chocolate"]

def forca():
    vidas = 6
    while True:
        escolha = rd.choice(palavras)

        letra = input("Digite uma letra: ")

        if letra.upper() in escolha:
            print(f"Letra {letra} correta!")
        else:
            print(f"Letra {letra} invalida!")
            vidas -= 1
            if vidas == 0:
                print("Vidas zeradas, voce perdeu!\n")
                continuar = input("Deseja continuar? (s/n) ").lower()
                if continuar == "n":
                    break
                

forca()