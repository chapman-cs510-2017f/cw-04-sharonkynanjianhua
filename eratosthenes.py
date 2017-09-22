#!/usr/bin/env python3


def gen_ints():
    """Generator for the positive integers."""
    n = 2
    while True:
        yield n
        n += 1
        
def eratosthenes(n):
    #This function will take a positive integer ```n``` and return all prime numbers smaller than ```n```
    #First generate all positive sintegers less than n, starting from the number 2. Then remove all multiples of 2. 
    #Then remove all multiples of the next largest remaining (prime) number. Then repeat the last step until you reach the largest remaining number. Finally, return the set of remaining (prime) numbers. 
    
    
    listRM=[]

    g = gen_ints()
    for _ in range (1,n-2):  #start from 2 to the number less than input
        i=next(g)
        if i%2 != 0: #remove all multiples of 2
            listRM.append(i) 
        
    #print("original list")
    #print(listRM)
  
    idxList = len(listRM)
    lenList = len(listRM) 
    largestNum = listRM[lenList-1]
   
    #remove all multiples of the next largest remaining (prime) number and repeat
    for _ in range(0, lenList-1):
        i = 0
        prime=True,
        while listRM[i] < largestNum:
            if largestNum % listRM[i] == 0:
                prime=False
                break
            else:
                prime=True        
            i += 1
            
        if prime == False:
            listRM.remove(largestNum)
            lenList -= 1
        
        idxList -= 1
        largestNum = listRM[idxList-1]
        #print("largest number ")
        #print(largestNum)
    
    #print("all prime numbers smaller than " +str(n)+" is:")
    #print(listRM)    
    return listRM

