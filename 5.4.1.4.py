from random import randrange

möglicheLottozahlen = []
for a in range(1,50,1):
    möglicheLottozahlen.append(a)

lottozahlen = []
for a in range(0,6,1):
    random = randrange(1, len(möglicheLottozahlen) - 1, 1)
    lottozahlen.append(möglicheLottozahlen[random])
    möglicheLottozahlen.remove(lottozahlen[-1])

print(lottozahlen)
