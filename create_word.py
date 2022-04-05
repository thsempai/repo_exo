from random import choice

def give_word(number):
    possibilities = ["a", "h", "k", "o", "n", "s", "t"]
    word = ""
    for n in range(number):
        word = word + choice(possibilities)

    return word

#partie principale

number = input("Nombre de lettres: ")
number = int(number)

print(give_word(number))