# leetcode #1 Two sum


indices = []

nums = [2,7,11,15,17,27]
target = 18


class Solution:

   def __init__(self, num, trgt):

       self.num = num
       self.trgt = trgt


   def twoSum(self):

     for flag,value in enumerate(self.num):

        for index,item in enumerate(self.num):


            if index+1 < len(self.num):

                if (value + self.num[index+1]) == self.trgt:

                    indices.append(flag)
                    indices.append(index+1)
                    return indices
                

                else : continue

output = Solution (nums,target)
final_output =output.twoSum()
print(final_output)
