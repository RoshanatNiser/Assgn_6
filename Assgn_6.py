# Assignment 6: Bisection and Regular Falsi
# Name: Roshan Yadav
# Roll No: 2311144

from Func_lib_for_assgn_6 import *

#Question-1: Finding Roots
print('Root by Bisection method', Bisection(a=1.5,b=3.0,t=0)) # Output: 2.623140335083008
print('\nRoot by Regular Falsi method', regular_falsi(a=1.5,b=3.0,t=0)) #Output: 2.6231403354363083

#Question-2: Bracketing
print('\nBracketing of f(x)=-x-cos(x)',bracketing(a=2,b=4,t=0,beta=0.2)) # output: [0.40000000000000013, 4]

