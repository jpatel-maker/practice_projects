#Find the sum of even numbers in a fibonacci sequence that are of value < 4 million
# we know the first two terms of the fibonacci sequence we want the next n terms where  the value of the nth term < 4million
# we then want the even terms to sum up
fibonacci_sequence = [1,2]
even_terms = []

# we need to know the last term and the previous term and the next_term to add to the sequence
last_term = fibonacci_sequence[-1]
previous_term = fibonacci_sequence[-2]
next_term = 0

# for each term in the sequence , while the last_term < 4 million the next_term must be the sum of the previous two terms and we must add this to the sequence

def create_sequence(fibonacci, last , previous ,next):
    for term in fibonacci_sequence[1:]:


        while last < 4000000:


            next = last + previous
            if next >= 4000000:
                break
            else:

                fibonacci_sequence.append(next)
                last = fibonacci_sequence[-1]
                previous = fibonacci_sequence[-2]



    return fibonacci_sequence

def sum_of_even_terms (even,fibonacci):

    # for each number in the fibonacci sequence if that number is even or divisible by two exactly add this number to the even terms list
    sum_evens_in_sequence = 0
    for item in fibonacci_sequence:
        if (item % 2) == 0:
            even_terms.append(item)

    for term in even_terms:
        sum_evens_in_sequence += term
    return sum_evens_in_sequence



completed_sequence = create_sequence(fibonacci_sequence, last_term,previous_term,next_term)
print(completed_sequence)
evens_in_sequence_sum = sum_of_even_terms(even_terms,fibonacci_sequence)
print(evens_in_sequence_sum)
