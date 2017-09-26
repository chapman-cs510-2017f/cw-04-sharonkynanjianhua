import primes
def test_primes():
    '''
        test if the eratosthenes function can return a list matches with expected one
    '''
    primeList19=[2, 3, 5, 7, 11, 13, 17]  #expected prime list   
    retList = primes.eratosthenes(19)
    print(retList)
    assert primeList19==retList

    
test_primes()