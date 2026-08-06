import random
import questionary
import time

verde = "\033[42m"
vermelho = "\033[41m"
reset = "\033[0m"
amarelo = "\033[33m"

pontuacao = 0

def atraso():
    print("Girando moeda...")
    time.sleep(0.5)

modo_jogo = questionary.select(
    "Selecione o modo de jogo:",
    choices=["MÉDIA DE SORTE", "ATÉ O LIMITE"]
).ask()

if modo_jogo == "MÉDIA DE SORTE":
    for _ in range (10):
        opcoes = ["CARA", "COROA"]

        moeda = random.choice(opcoes)

        escolha_usuario = questionary.select(
            "Selecione qual lado da moeda vai cair:",
            choices=["CARA", "COROA"]
        ).ask()

        print(f"Caiu: {amarelo}{moeda}{reset}")
        atraso()

        if escolha_usuario == moeda:
            print(f"{verde}Você acertou!{reset}")
            pontuacao += 1
        else:
            print(f"{vermelho}Você errou! ;({reset}")
    media = (f"{((pontuacao / 10) * 100):.0f} %")
    print(f"""Nível de sorte: {media}""")
else:
    escolha_usuario = ""
    moeda = ""

    while escolha_usuario == moeda:
        opcoes = ["CARA", "COROA"]

        moeda = random.choice(opcoes)

        escolha_usuario = questionary.select(
            "Selecione qual lado da moeda vai cair:",
            choices=["CARA", "COROA"]
        ).ask()
        atraso()
        if escolha_usuario == moeda:
            print(f"{verde}Você acertou!{reset}")
            pontuacao += 1
    print(f"""{vermelho}Você errou!{reset}
    Pontuação máxima: {pontuacao}""")

