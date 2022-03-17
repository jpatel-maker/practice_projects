#Leetcode 13. Roman Integer

class Solution:


    characters = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000
                  }
    value = 0


    def __init__(self, string_value):

        self.string_value = string_value

    def romanToInt (self):


        for index,char in enumerate(self.string_value):

            if char in Solution.characters:

                if index != 0 and char > self.string_value[index-1] :

                    Solution.value = (Solution.characters.get(char) - Solution.characters.get(self.string_value[index-1]))


                else:

                    Solution.value += Solution.characters.get(char)




        return Solution.value







s ="IV"
converted = Solution(s)
converted_numerals = converted.romanToInt()
print(converted_numerals)
