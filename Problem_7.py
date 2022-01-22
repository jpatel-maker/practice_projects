# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder what is the smallest positive number that is evenly divisible by all the numbers from 1-20?

numerator = 1
denominator = [*range(1,21)]
# check if number in numerator is the smallest possible number that meets this requirement

def check_smallest_number (number, divisor):

    smallest_number = False

    for numbers in divisor:

        if (number % numbers) == 0:
           smallest_number = True
           continue

        else:

            smallest_number = False
            break

    if smallest_number == True:
        return True

    else:
        return False

# next if it is the smallest possible number return the number or check next number



smallest_possible_number = False
while smallest_possible_number == False:
    numerator = numerator+ 1
    smallest_possible_number = check_smallest_number(numerator, denominator)



print (numerator)
