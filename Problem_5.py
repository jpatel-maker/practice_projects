# Largest prime factor of any number
# problem: what is the largest prime factor of 600851475143?
# 1st create prime numbers
import math

prime_numbers = []
prime_factors = []
number = 0

def get_factors (number_solved):
    factor = []
    all_factors = [*range(2, int(math.sqrt(number_solved)) + 1)]
    for potential_factor in all_factors:
        if number_solved % potential_factor == 0:
            factor.append(potential_factor)

    return factor


def determine_prime_numbers (number_list, prime_list):

    not_prime = False
    for items in number_list:

        copy_all_numbers = number_list[:]
        copy_all_numbers.remove(items)

        #print(copy_all_numbers)
        for item in copy_all_numbers:

            if items % item == 0:
                not_prime = True
                break
            else:
                not_prime = False
                continue

        if not_prime == True:
            continue
        else:
            prime_list.append(items)

    return prime_list


# next step we want all prime factors




# finally we want the largest prime factor of the number to be solved

def largest_prime_factor (prime_factors_list):

    sorted_list =  sorted( prime_factors_list, reverse=True)
    largest_prime = sorted_list[0]

    return largest_prime


print ("please input the number for which you want the prime factors and the largest prime factor:")
number = int(input("input number:"))
number_factors = get_factors(number)
print ("The number you are trying to solve is: " + str(number))
print ("The factors of this number are: " + str(number_factors))


prime_numbers = determine_prime_numbers(number_factors, prime_numbers)

print("The prime factors of " + str(number) + " are: " + str(prime_numbers))
 

largest_factor = largest_prime_factor(prime_numbers)

print("The largest prime factor of " +str(number) + " is: " + str(largest_factor))

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

