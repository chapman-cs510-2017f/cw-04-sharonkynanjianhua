def prime_check(Num, primeList):
        for primeNum in primeList:
            if Num % primeNum == 0:
                return False
        return True


def gen_eratosthenes():
    primeList = []
    num = 2
    while True:
        primeList.append(num)
        yield num
        num = num + 1
        while prime_check(num, primeList) == False:
            num = num + 1

    
    

p=gen_eratosthenes()
[print(next(p)) for _ in range(9)]
