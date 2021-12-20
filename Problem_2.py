# 204. Count Primes. Given an integer n, return the number of prime numbers that are strictly less than n.
#  where  0 <= n <= 5*10^6
from  math import isqrt

def get_primes (numbers):

    primes = []

    if numbers <= 2:

        return []



    prime_list = [True]*numbers
    prime_list[0] = False
    prime_list[1] = False

    #print(prime_list)


    for num in range (2, isqrt(numbers)+1):


            if  prime_list[num]:

                for value in range(num*num,numbers,num):

                    prime_list[value] = False

    return [num for num in range(numbers) if prime_list[num]]




#for numbers in range(2,501):
numbers = 500000


primes = get_primes(numbers)
print("primes list is: " + str(primes))


