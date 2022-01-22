# Find the difference between the sum of squares of the first one hundred natural numbers and the square of the sum

numbers = [*range(1,101)]
sum_of_squares_result = 0
square_of_sum_result = 0

# find sum of squares

def sum_of_squares (number):

    result = 0
    for value in number:
        result = result + (value)**2

    return result


# find square of sum

def square_of_sums (number):

    result = 0

    for value in number:
        result = result + value

    result = (result)**2
    return result

# difference

def difference (result_A, result_B):

    answer = result_A - result_B
    return answer


sum_of_squares_result = sum_of_squares(numbers)
square_of_sum_result = square_of_sums(numbers)

difference_of_the_results = difference(square_of_sum_result,sum_of_squares_result)
print(difference_of_the_results)

