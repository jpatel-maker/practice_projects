# Leetcode 14. Longest Common Prefix:

strs = ["flower", "flow", "flight"]


string_1 = strs[0]
is_prefix = True
prefix = ""

for index_1, value in enumerate(string_1):

    if index_1 +1 < len(string_1):

        for index_2, item in enumerate(strs):

            if index_2 + 1 <= len(strs) :

                if index_1 +1 <= len(strs[index_2]):

                    if string_1[index_1] == strs[index_2][index_1]:

                        is_prefix = True


                    else:
                        is_prefix = False



    if is_prefix:
            prefix += value

    elif len(prefix) == 0:
            prefix = ""


    else: continue

print(prefix)
