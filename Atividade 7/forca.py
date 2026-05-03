import random as rd

palavras = ["python", "computador", "programa", "teclado", "internet"]

forca = [
"""
  -----
  |   |
      |
      |
      |
      |
=========
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

palavra = rd.choice(palavras)
letras_descobertas = ["_"] * len(palavra)
letras_erradas = []
erros = 0

while erros < 6 and "_" in letras_descobertas:
    print(forca[erros])
    print("Palavra:", " ".join(letras_descobertas))
    print("Letras erradas:", letras_erradas)

    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
    else:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
            erros += 1

if "_" not in letras_descobertas:
    print("Você venceu!")
    print("Palavra:", palavra)
else:
    print(forca[erros])
    print("Você perdeu!")
    print("A palavra era:", palavra)