import random as rr

def isItPerfect():
    pass

def randomGenerator(s, e, a):
    numbers = []
    for i in range(a):
        numbers.append(rr.randint(s, e))
    return numbers

def makeNumber(text):
    while True:
        n =  input(text)
        try:
            n = int(n)
            return n
        except ValueError:
            print("Helytelen érték!")

startMessage = "kezdőérték: "
endMessage = "Végérték: "
amountMessage = "Értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)

randomGenerator(start, end, amount)