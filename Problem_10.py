""" find the thirteen adjacent digits in the 1000 digit number that have the greatest product. what is the value of the product?
"""
digits_highest = []

number = []
# first we need the 1000 digit number

print ("Enter your 1000 digit number: ")
number_input = input("Enter number: \n")

for digit in number_input:

    number.append(int(digit))


# next for each digit get the next 13 digits including current digit

def get_digit (num):

    digits = []
    for values in num:

        while len(digits) <13:
            digits.append(values)
            break
    return digits

# next get product of these digits

def get_product (digits):

    current_product = 1
    for items in digits:
        current_product = (current_product* items)

    return current_product


# next we want to solve the problem
def get_highest_product (num, digits):

    product_highest = 1


    for values in num:

        digits = get_digit(num)
        num.pop(0)
        current_product_of_digits = get_product(digits)
        if product_highest <= current_product_of_digits:

            product_highest = current_product_of_digits

    print(digits)
    print(product_highest)


get_highest_product(number,digits_highest)
