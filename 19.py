def jogo_adivinhacao(secreto):
    while True:
        palpite = int(input("Digite seu palpite: "))
        if palpite == secreto:
            print("Você acertou!")
            break
        elif palpite > secreto:
            print("Maior que o número secreto")
        else:
            print("Menor que o número secreto")
jogo_adivinhacao(42)
