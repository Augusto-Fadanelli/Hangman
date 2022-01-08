#Jogo da forca

import unicodedata
from random import randint

f = open("wordList.txt", "r")
List = f.read().splitlines()

# Número aleatório
ran = randint(0,len(List)-1)

wordSecret = List[ran]

word_tip = wordSecret.split(" ")

secretWord = word_tip[0]
tip = word_tip[1]
lifes = 5

# Tratamento de String
secretWordFormated = unicodedata.normalize("NFD", secretWord)
secretWordFormated = secretWordFormated.encode("ascii", "ignore")
secretWordFormated = secretWordFormated.decode("utf-8")
secretWordFormated = secretWordFormated.lower()

show = "*" * len(secretWord)
typed = []

while True:
    print(f"Dica: {tip}")
    print(show)
    print(f"Vida: {lifes}")
    guess = input("Digite uma letra: ")

    # Tratamento de String
    guess = unicodedata.normalize("NFD", guess)
    guess = guess.encode("ascii", "ignore")
    guess = guess.decode("utf-8")
    guess = guess.lower()

    # Verifica se foi digitado mais de uma letra
    if len(guess) > 1:
        print("Não é possível inserir mais de uma letra!")
        continue

    if guess in secretWordFormated:
        typed.append(guess)
    else:
        lifes -= 1
        if lifes < 1:
            print(f"Vida: {lifes}")
            print("Você perdeu!")
            print(f"A palavra era {secretWord}")
            break

    show = ''
    for letter in secretWordFormated:
        if letter in typed:
            show += letter
        else:
            show += '*'

    if show == secretWordFormated:
        print("Você venceu!")
        print(f"A palavra era {secretWord}!")
        break
