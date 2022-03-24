# Leetcode 20. Valid parentheses:

str = "(((({{}}))))"
dict = {"(":")", "[":"]","{":"}"}
stack = []

for i, element in enumerate(str):

    if i+1 <=len(str):

        if element in dict.keys():

            stack.append(element)
        # if value is in dictionary and if the key is in the stack


        list_1 = dict.items()
        for index,items in enumerate(list_1):

            if element == items[1] and items[0] ==stack[-1]:

                stack.pop()

            else:continue


if len(stack) == 0:
    output = True

else: output = False


print(output)



