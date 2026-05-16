from pygame import *
import subprocess # descobri pesquisando !
import sys

def valida_email(email):
    if "@puc.com" in email:
        return True
    else:
        return False

def tem_maiuscula(senha):
    for carac in senha:
        if "A" <= carac <= "Z":
            return True
    return False

def tem_minuscula(senha):
    for carac in senha:
        if "a" <= carac <= "z":
            return True
    return False

def tem_numero(senha):
    for carac in senha:
        if carac.isdigit():
            return True
    return False

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not tem_maiuscula(senha):
        return False
    if not tem_minuscula(senha):
        return False
    if not tem_numero(senha):
        return False
    return True

def criptografa(senha):
    senha_cripto = ""

    for carac in senha:
        if carac.isalpha():
            pos_alpha = ord(carac) - ord('a')
            pos_alpha = (pos_alpha + 3) % 26
            pos_ascii = pos_alpha + ord('a')
            senha_cripto += chr(pos_ascii)
    return senha_cripto


init()
screen = display.set_mode((1280, 720))
running = True

fonte = font.Font(None, 45)
fonte_menor = font.Font(None, 32)

email = ""
senha = ""
campo_atual = "email"

mensagem_email = ""
mensagem_senha = ""
senha_criptografada = ""

while running:
    for evento in event.get():
        if evento.type == QUIT:
            running = False

        if evento.type == KEYDOWN:
            if evento.key == K_BACKSPACE:
                if campo_atual == "email":
                    email = email[:-1]
                else:
                    senha = senha[:-1]

            elif evento.key == K_RETURN:
                if campo_atual == "email":
                    if valida_email(email):
                        mensagem_email = "Parabéns, o seu e-mail é válido!"
                        campo_atual = "senha"
                    else:
                        mensagem_email = "Email inválido!"

                elif campo_atual == "senha":
                    if valida_senha(senha):
                        mensagem_senha = "Senha segura!"
                        senha_criptografada = criptografa(senha)

                        if senha_criptografada != "":
                            texto = fonte_menor.render("Senha criptografada:", True, "black")
                            screen.blit(texto, (100, 470))

                            cripto = fonte.render(senha_criptografada, True, "blue")
                            screen.blit(cripto, (100, 510))

                        display.update()
                        time.delay(1000)

                        running = False
                        subprocess.run([sys.executable, "Atividade 6/casita.py"])

                    else:
                        mensagem_senha = "Senha fraca! Use 8 caracteres, maiúscula, minúscula e número."

            else:
                if campo_atual == "email":
                    email += evento.unicode
                else:
                    senha += evento.unicode

    screen.fill("white")

    texto_email = fonte_menor.render("Digite seu email:", True, "black")
    screen.blit(texto_email, (100, 140))

    draw.rect(screen, "black", (100, 170, 600, 45), 2)
    email_surface = fonte_menor.render(email, True, "black")
    screen.blit(email_surface, (110, 182))

    if mensagem_email != "":
        cor = "green" if valida_email(email) else "red"
        msg = fonte_menor.render(mensagem_email, True, cor)
        screen.blit(msg, (100, 230))

    texto_senha = fonte_menor.render("Digite sua senha:", True, "black")
    screen.blit(texto_senha, (100, 300))

    draw.rect(screen, "black", (100, 330, 600, 45), 2)
    senha_surface = fonte_menor.render(senha, True, "black")
    screen.blit(senha_surface, (110, 342))

    if mensagem_senha != "":
        cor = "green" if valida_senha(senha) else "red"
        msg = fonte_menor.render(mensagem_senha, True, cor)
        screen.blit(msg, (100, 390))

    display.update()

quit()
