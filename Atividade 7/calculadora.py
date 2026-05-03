memoria = False

while True:
    if memoria == False:
        n1 = int(input("Digite o primeiro número: "))
    else:
        n1 = memoria
        print(f"Ultimo numero: {memoria}")

    operador = input("Digite a operação (+, -, x, /): ")

    n2 = int(input("Digite o segundo número: "))

    if operador == "+":
        resultado = n1 + n2
    elif operador == "-":
        resultado = n1 - n2
    elif operador == "x":
        resultado = n1 * n2
    elif operador == "/":
        resultado = n1 / n2

    print(f"Resultado: {resultado}\n")

    continuar = input("Deseja continuar? (s/n): ").lower()

    if continuar == "n":
        break

    memoria = resultado