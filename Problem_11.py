# a pythagorean triplet is a set of three natural numbers for which a < b < c where a*2 + b*2 = c*2
# there is only one pythagorean triplet for which the following condition is true: a+ b+ c = 1000
# Find product abc for this triplet

# first check it triplet for all numbers meets criteria of a+b+c =1000, a<b<c:
# c must be triple digit at least from 997-100



def pythagorean_triplets ():

        
       number_a = 1
       number_b = 2
       number_c = 997
       product = 1


       for c in range(number_a,99,-1):
              for b in range (number_b, 995):
                     for a in range (number_c,994):




                            if a < b < c and a + b + c == 1000 and
(a**2)+(b**2) == c**2:
                                   product = a* b * c
       
       return product  


pythgorean_product = pythagorean_triplets()

print(pythgorean_product)
