# Assignment 6: Bisection and Regular Falsi
# Name: Roshan Yadav
# Roll No: 2311144

import math


def f(x,f):

    """This function defines the functions."""

    if f==0: # for question 1
        a=math.log(x/2)
        b=math.sin(5*x/2)
        return a-b
    
    if f==1: # for question 2
        a=-float(x)
        b=math.cos(x)
        return a-b


def Bisection(a=1.5,b=3.0,t=0,e=10**-6,d=10**-6):

    """This function utilises sthe bisection method to find roots."""

    if f(a,t) * f(b,t) <=0:
        if abs(b-a) < e:
            if abs(f(a,t)) < d:
                return a
            if abs(f(b,t)) < d:
                return b
    
        else:
            c=(a + b)/2
            if f(c,t)*f(a,t)<0:
                return Bisection(a=a,b=c,t=t)
            if f(c,t)*f(b,t) <0:
                return Bisection(a=c,b=b,t=t)
    else:
        return 'No root found in the given interval'
    
def regular_falsi(a=1.5,b=3.0,c=None,t=0,e=10**-6,d=10**-6):

    """This function utilises sthe Regular Falsi method to find roots."""

    if f(a,t)*f(b,t) <=0:
        if abs(b-a) < e:
            if abs(f(a,t)) < d:
                return a
            if abs(f(b,t)) < d:
                return b
        else:
            c=a
            c_new = (b - (((b -a)*f(b,t))/(f(b,t)-f(a,t))))
            if f(a,t)*f(c_new,t) <= 0:
                if abs(c_new - c) < e: 
                    return c
                else:
                    return regular_falsi(a=a,b=c_new,c=c_new,t=t)
            
            if f(b,t)*f(c,t) <= 0:
                if abs(c_new - c) < e: 
                    return c
                else:
                    return regular_falsi(a=c_new,b=b,c=c_new,t=t)
    else:
        return 'No root found in the given interval'
            
def bracketing(a,b,t=0,beta=0.2):

    """This function find the bracket contain the root of the function."""

    if a > b:
        a,b=b,a

    if f(a,t)*f(b,t)<=0:
        l=[a,b]
        return l
    
    else:
        if abs(f(a,t)) < abs(f(b,t)):
            a_new=a-beta*(b-a)
            return bracketing(a=a_new,b=b,t=0,beta=0.5)
        if abs(f(a,t)) >= abs(f(b,t)):
            b_new=b+beta*(b-a)
            return bracketing(a=a,b=b_new,t=0,beta=0.5)
            
