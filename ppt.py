import random

opcoes = ["Pedra", "Papel", "Tesoura"]

ppt_bot = random.choice(opcoes)

print("""PEDRA, PAPEL OU TESOURA
> Digite qual deseja escolher""")
ppt_usuario = input("Escolha: ").capitalize()

while ppt_usuario not in opcoes:
    print("Opção inválida.")
    ppt_usuario = input("Escolha novamente: ").capitalize()

print(f"""{ppt_usuario}   x   {ppt_bot}""")

if ppt_usuario == ppt_bot:
    print("Empate")
elif ppt_usuario == "Pedra" and ppt_bot == "Papel":
    print("Bot ganhou")
elif ppt_usuario == "Papel" and ppt_bot == "Tesoura":
    print("Bot ganhou")
elif ppt_usuario == "Tesoura" and ppt_bot == "Pedra":
    print("Bot ganhou")

elif ppt_bot == "Pedra" and ppt_usuario == "Papel":
    print("Usuário ganhou")
elif ppt_bot == "Papel" and ppt_usuario == "Tesoura":
    print("Usuário ganhou")
elif ppt_bot == "Tesoura" and ppt_usuario == "Pedra":
    print("Usuário ganhou")