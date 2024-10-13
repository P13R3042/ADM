#• Introduction (all – total: 7 - max points: 75)
#https://www.hackerrank.com/domains/python/py-introduction

#Say "Hello, World!" With Python
'''
if __name__ == '__main__':
    print("Hello, World!")
'''
#--------------------------------------------------------
#Python If-Else
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 :
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        if n >= 6 and n <= 20:
            print("Weird")
        if n > 20:
            print("Not Weird")

'''

#--------------------------------------------------------
#Arithmetic Operators
'''
if __name__ == '__main__':
    try:
        a = int(input())
        b = int(input())
        print(a+b)
        print(a-b)
        print(a*b)
    except:
        print("bad parsing")    
    
'''
#--------------------------------------------------------
#Python: Division
'''
if __name__ == '__main__':
    try:
        a = int(input())
        b = int(input())
        if b != 0:
            print(a//b)
            print(a/b)
    except:
        print("bad arguments")

'''
#--------------------------------------------------------
#Loops
'''
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)
    

'''
#--------------------------------------------------------
#Write a function
def is_leap(year):
    leap = False
    
    if ( year % 4 )== 0 : 
        leap = True
        if ( year % 100 )== 0 : 
            leap = False
            if ( year % 400 )== 0 : 
                leap = True
    
    return leap

#--------------------------------------------------------
#Print Function
'''
if __name__ == '__main__':
    n = int(input())
    res = ""
    for i in range(1,n+1):
        res+=str(i)
    print(res)
    

'''

###################################################################
#• Data types (all – total: 6 - max points: 60)
#https://www.hackerrank.com/domains/python/py-basic-data-types
#--------------------------------------------------------
###################################################################
#• Strings (all – total: 14 - max points: 220)
#https://www.hackerrank.com/domains/python/py-strings
###################################################################
#• Sets (all – total: 13 - max points: 170)
#https://www.hackerrank.com/domains/python/py-sets
###################################################################
#• Collections (all – total: 8 - max points: 220)
#https://www.hackerrank.com/domains/python/py-collections
###################################################################
#• Date and Time (all – total: 2 - max points: 40)
#https://www.hackerrank.com/domains/python/py-date-time
###################################################################
#• Exceptions (only 1 - max points: 10)
#https://www.hackerrank.com/challenges/exceptions
###################################################################
#• Built-ins (only 3 - max points: 80)
#https://www.hackerrank.com/challenges/zipped
#https://www.hackerrank.com/challenges/python-sort-sort
#https://www.hackerrank.com/challenges/ginorts
###################################################################
#• Python Functionals (only 1 - max points: 20)
#https://www.hackerrank.com/challenges/map-and-lambda-expression
###################################################################
#• Regex and Parsing challenges (all – total: 17 - max points: 560)
#https://www.hackerrank.com/domains/python/py-regex
###################################################################
#• XML (all – total: 2 - max points: 40)
#https://www.hackerrank.com/domains/python/xml
###################################################################
#• Closures and Decorations (all – total: 2 - max points: 60)
#https://www.hackerrank.com/domains/python/closures-and-decorators
###################################################################
#Numpy (all – total: 15 - max points: 300)
#https://www.hackerrank.com/domains/python/numpy
