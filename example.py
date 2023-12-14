import random as rr

def isItPerfect(n):
    if n == 1 or n == 0:
        return False
    else:  
        divNumber = [1]
        for i in range(2, n, 1):
            if n % i == 0:
                divNumber.append(i)
        return sum(divNumber) == n
            
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

perfectNumbers = []            
pnf = dict()

startMessage = "kezdőérték: "
endMessage = "Végérték: "
amountMessage = "Értékek száma: "

start = makeNumber(startMessage)
end = makeNumber(endMessage)
amount = makeNumber(amountMessage)

randomNumber = randomGenerator(start, end, amount)

for num in randomNumber:
    if isItPerfect(num):
        perfectNumbers.append(num)


for num in perfectNumbers:
    if num in pnf.keys():
        pnf[num] += 1
    else:
        pnf[num] = 1
        
for key in pnf.keys():
    print(f"{key}: {pnf[key]} db")