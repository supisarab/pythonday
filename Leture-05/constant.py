import random
HEAD = 1
TAIL = 2
TOSSES = 10
def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEAD, TAIL) == HEAD:
            print("head")
        else:
            print("tails")
tosses_coin()