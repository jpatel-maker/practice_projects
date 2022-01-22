# Find the sum of all the primes below two million
# will attempt sieve of eratosthenes here
# iteratively mark as a composite the multiples of each prime, then the remaining numbers are primes also sqrt is sufficient for primeness

import math

ceiling = 2000000
numbers = [*range(2,ceiling+1)]
prime = 2
prime_numbers =[]

def get_primes (numb):

    primes = []

    for number in range(0, int(math.sqrt(len(numb)))):
        prime = numb[number]

        for num in numb:
            if num % prime == 0 and num != prime:
                numb.remove(num)

    primes = numb [:]
    return primes


def get_sum_of_primes (prime_num):

    prime_sum = 0

    for all_prime_numbers in prime_num:

        prime_sum += all_prime_numbers

    return prime_sum



prime_numbers = get_primes(numbers)
print(prime_numbers)

sum = get_sum_of_primes(prime_numbers)
print (sum)
