#Largest palindrome that is from the product of two three digit numbers:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers

three_digit_numbers_list = [*range(100,1000)]
palindromes = []

# first return palindromes
def return_palindromes (three_digit_number):

    product = ""
    reverse_result = ""
    palindrome = []

    for numbers in three_digit_number:
        next_numbers = three_digit_number [:]
        next_numbers.remove(numbers)

        for remaining_numbers in next_numbers:
            product = str(numbers * remaining_numbers)
            reverse_result = product [::-1]

            if product == reverse_result:
                product = int(product)
                palindrome.append(product)

    return palindrome


# next we want the largest plaindrome of three digit number product

def largest_palindrome (all_palindromes):

    reverse_palindromes = all_palindromes[:]
    reverse_palindromes.sort(reverse = True)
    largest_palindrome = reverse_palindromes [0]

    return largest_palindrome


palindromes = return_palindromes(three_digit_numbers_list)
print("the palindromes for the product of two three digit numbers are: " + str (palindromes))

largest_palindrome_of_product = largest_palindrome(palindromes)

print ("The largest palindrome from of the product of two three digit numbers is: " + str(largest_palindrome_of_product))
