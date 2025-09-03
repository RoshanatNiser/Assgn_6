# Assignment 6: Bisection and Regular Falsi
# Name: Roshan Yadav
# Roll No: 2311144

import math

def abs(d):

    """" This function returns the absoulute value of the input."""
    if d<0:
        return (-1)*d
    if d>=0:
        return d

def f(x,f=0):

    """This function defines the functions."""
    
    if f==0: # for question 1
        a=math.log(x/2)
        b=math.sin(5*x/2)
        return a-b
    
    if f==1: # for question 2
        a=-float(x)
        b=math.cos(x)
        return a-b


def Bisection(a=1.5,b=3.0,f=0,e=10*-6,d=10*-6):

    """This function utilises sthe bisection method to find roots."""

    if f(a)*f(b) <=0:
        if abs(b-a) < e:
            if abs(f(a,f)) < d:
                return a
            if abs(f(b,f)) < d:
                return b
    
    else:
        c=(a + b)/2
        if f(c,f)*f(a,f)<0:
            return Bisection(a=a,b=c,f=f)
        if f(c,f)*f(b,f) <0:
            return Bisection(a=c,b=b,f=f)
        
def regular_falsi(a=1.5,b=3.0,c=0,f=0,e=10*-6,d=10*-6):

    """This function utilises sthe Regular Falsi method to find roots."""

    if f(a)*f(b) <=0:
        if abs(b-a) < e:
            if abs(f(a,f)) < d:
                return a
            if abs(f(b,f)) < d:
                return b
    else:
        c_new = (b - (((b -a)*f(b,f))/(f(b)-f(a))))
        if f(a,f)*f(c_new,f) <= 0:
            if abs(c_new - c) < e: 
                return c
            else:
                return regular_falsi(a=a,b=c_new,c=c_new,f=f)
        
        if f(b,f)*f(c,f) <= 0:
            if abs(c_new - c) < e: 
                return c
            else:
                return regular_falsi(a=c_new,b=b,c=c_new,f=f)
            
def bracketing(a,b,f=0,beta=0.2):

    """This function find the bracket contain the root of the function."""

    if a > b:
        a,b=b,a

    if f(a,f)*f(b,f)<=0:
        l=[a,b]
        return l
    
    else:
        if abs(f(a,f)) < abs(f(b,f)):
            a_new=a-beta*(b-a)
            return bracketing(a=a_new,b=b,f=0,beta=0.5)
        if abs(f(a,f)) >= abs(f(b,f)):
            b_new=b+beta*(b-a)
            return bracketing(a=a,b=b_new,f=0,beta=0.5)
            
