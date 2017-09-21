import primes
def test_primes():
        
    primeList19=[3,5,7,11,13,17,19]    
    retList = primes.eratosthenes(19)
    print(retList)
    assert primeList19==retList

    
test_primes()
