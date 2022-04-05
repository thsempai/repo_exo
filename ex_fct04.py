from random import randint

def list_integers(n):

    intergers = []

    for _ in range(n):
        rnd = randint(1, 6)
        intergers.append(rnd)

    return intergers

# main
# testing
print(list_integers(5))
print(list_integers(1))
print(list_integers(0))
print(list_integers(10))

