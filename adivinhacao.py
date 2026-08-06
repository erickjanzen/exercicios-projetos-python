import random

numero = random.randint(1,10)

adivinhacao: int = int(input("Adivinhe o número escolhido entre 1 até 10: "))
while adivinhacao != numero:
    if adivinhacao < numero:
        print(f"O número é maior que {adivinhacao}")
    else:
        print(f"O número é menor que {adivinhacao}")
    adivinhacao = int(input("Tente novamente: "))
print("Parabéns! você acertou o número.")