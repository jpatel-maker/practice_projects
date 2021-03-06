# find the sum of multiple of 3 or 5 below 1000

numbers = [*range(1,1000)]
multiples = []

def determine_multiples(num):

    for number in numbers:
        if (number % 3) == 0 or (number % 5) == 0:
            multiples.append(number)

    return multiples

def sum_multiples (multiple):

    sum = 0
    for number_is_multiple in multiples:

        sum += number_is_multiple

    return sum



multiple_list = determine_multiples(numbers)
sum_of_numbers = sum_multiples (multiple_list)

print(sum_of_numbers)
