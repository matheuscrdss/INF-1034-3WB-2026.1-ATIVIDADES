import random 
#parte A
def usuario_adivinha():
    print("===============O Jogo da Adivinhaçâo!===============\n")
    
    numero_secreto = random.randint(1, 1023)
    tentativas = 0
    
    while(True):  
        chute = int(input("Digite um chute entre 1 e 1023: "))
        tentativas += 1
        
        if chute < numero_secreto:
            print("1, o número é \033[31mMaior\033[0m!\n") #perguntei a IA como mudar a cor 
        elif chute > numero_secreto:
            print("-1, o número é \033[31mMenor\033[0m!\n")
        else:
            print(f"0, Parabéns, você conseguiu acertar em {tentativas} tentativas\n")
            break
#parte B
def computador_adivinha():
    print("===============O Jogo da Adivinhaçâo!===============\n")
    print("Pense em número para ocomputador adivinhar!")
    input("Pressione ENTER para começar: ")
    
    alto = 1023
    baixo = 1 
    tentativas = 0
    
    while baixo <= alto:
        palpite = (baixo + alto) // 2 
        tentativas += 1 
        print(f"Computador tentou: {palpite}")
        
        resposta = input("Digite -1 (Se for menor), 1 (Se for maior), 0 (Acertou!): \n")
        if resposta == "0":
            print("Acertou!")
        if resposta == "-1" :
            alto = palpite - 1 
        elif resposta == "1":
            baixo = palpite + 1 
        else:
            print("Resposta inválida, use -1, 1 e 0")
           
def jogo():
    print("Escolha quem vai adivinhar: ")
    print("1 - Você tenta adivinhar o número do computador")
    print("2 - O computador tenta adivinhar o seu número")

    escolha = input("Qual a sua escolha: ") 

    if escolha == "1":
        usuario_adivinha()
    elif escolha == "2":
        computador_adivinha()
        
if __name__ == "__main__":
    jogo()
