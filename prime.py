#!/usr/bin/env python3
import eratosthenes

def prime_check(Num, primeList):
    """checking if Num is a prime by divided the element in previous primelist"""
    for primeNum in primeList:
        if Num % primeNum == 0:
            return False
        return True


def gen_eratosthenes():
    """
    generate prime number
    """
    primeList = []
    num = 2
    while True:
        primeList.append(num)
        yield num
        num = num + 1
        while prime_check(num, primeList) == False:
            num = num + 1

    

def main(local_argv):
    """
    local_argv is the argument list, progrom name is first arugment
    this function prints the fibonacci list calcuated by the command line argument n 
    
    """
   
    if len(local_argv) != 2:
        print("must add one and only one command argument, , exit ")
        return

        
    argument_n = int(local_argv[1]) #remember, this is the 2nd argument in command line
    
    if argument_n <= 0:
        print("please input an pistive interger number, exit")
        return

    retList =eratosthenes.eratosthenes(argument_n)

    return retList

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
    
    
