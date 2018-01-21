"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
    a^2 + b^2 = c^2

For example:
    3^2 + 4^2 = 5^2
  =   9 +  16 = 25

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""
a = 1
b = 2
c = 3

for a in range(1,1000):
    for b in range(a+1,1000):
        c = (a**2 + b**2)**0.5
        if int(c) == c:
            if a + b + c == 1000:
                print("triplet:",a,b,int(c),"; sum:",int(a+b+c),"; product: ",int(a*b*c))
                break

