print("SHARK AI")
print("Ola! Eu sou sua IA.")
print("Digite sair para encerrar.")

nome = ""

while True:
    mensagem = input("Voce: ")
    texto = mensagem.lower().strip()

    if texto == "sair":
        print("Shark AI: Ate mais!")
        break

    elif "quem" in texto:
        print("Shark AI: Eu sou a Shark AI, uma IA criada por voce!")

    elif "meu nome" in texto:
        partes = mensagem.split()

        if len(partes) >= 4:
            nome = partes[-1]
            print("Shark AI: Prazer em te conhecer, " + nome + "!")
        else:
            print("Shark AI: Qual e o seu nome?")

    elif "qual" in texto and "nome" in texto:
        if nome != "":
            print("Shark AI: Seu nome e " + nome + "!")
        else:
            print("Shark AI: Voce ainda nao me contou seu nome.")

    elif "oi" in texto or "ola" in texto:
        print("Shark AI: Oi! Tudo bem?")

    elif "tudo bem" in texto:
        print("Shark AI: Tudo otimo!")

    elif "minecraft" in texto:
        print("Shark AI: Minecraft e um jogo de construcao e sobrevivencia!")

    elif "roblox" in texto:
        print("Shark AI: Roblox tem milhares de experiencias!")

    elif "matematica" in texto:
        print("Shark AI: Posso tentar ajudar com matematica!")

    elif "obrigado" in texto or "valeu" in texto:
        print("Shark AI: De nada!")

    else:
        print("Shark AI: Ainda estou aprendendo!")
