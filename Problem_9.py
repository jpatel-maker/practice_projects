# what is the 10001st prime number
number = 2
prime_numbers = []

prime = False
# check if a number is prime number

def check_prime (current_number):

    previous_number = [*range(2, current_number)]
    is_prime = False

    if previous_number:

        for values in previous_number:

         if current_number % values != 0:
            is_prime = True
            break

         else:
            is_prime = False
            break

    else:
        is_prime = True

    return is_prime


# get all prime numbers

def get_primes (current_number,prime_status):
    all_prime_numbers = []



    while len(all_prime_numbers) <= 10001:
        if prime_status == True:
            all_prime_numbers.append(current_number)
            current_number += 1
            prime_status = check_prime(current_number)


    return all_prime_numbers


# get the last prime number 10001st
prime = check_prime(number)
prime_numbers = get_primes(number, prime)

the_prime_number_is = prime_numbers [-1]
print (the_prime_number_is)
