import string

#email = input("Digite o email: ")
senha = input("Digite uma senha: ")

def valida_email(email):
    if "@puc.com" in email:
        return True
    else:
        return False

def tem_maiuscula(senha):
    for carac in senha:

