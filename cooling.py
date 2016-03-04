
"""
File: cooling.py

Copyright (c) 2016 Lauren Graziani

License: MIT

<brief description of the code>


T_tea = float(raw_input ("Enter Temperature of the tea: "))
T_air = float(raw_input ("Enter Temperature of the air: "))
num_minutes = int(raw_input ("Enter number of minutes: "))
t = 0
k = .055
print "Temperature of the Tea:%.0f" % T_tea
print "Temperature of the air:%.0f" % T_air
print "Number of minutes:%d" % num_minutes
print "Minute Temperature"
while t<=19:
    print " %2d      %.1f" % (t, T_tea)
    T_tea -= .055 * (T_tea - T_air)
    t=  t + 1
