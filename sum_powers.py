
"""
File: sum_powers.py

Copyright (c) 2016 Lauren Graziani

License: MIT

<brief description of the code>

"""
#`1 + b + b^2 + ... + b^n`.
#`b^(n+1)/(b-1)`.
b= raw_input ("Enter a floating number: ")
b_float = float (b)
n = raw_input ("Enter a natural number: ")
n_int = int (n)
print
total_sum = 0
i = 1
count = 0
while (count <= n_int):
    total_sum = total_sum + b_float ** count
    count = count + 1

print "sum of powers from while loop: %f " %total_sum
print "sum of powers from equation: %f " %b_float**((n_int+1)/(b_float-1))
