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

#Nested Lists

def nestedList(students):
    
    # Ordina gli studenti per voto (dal piu basso) e poi per nome
    students_sorted = sorted(students, key=lambda x: x[1])
    
    # Trova il secondo voto piu basso
    lowest_score = students_sorted[0][1]
    second_lowest_score = None
    
    for student in students_sorted:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break
    
    # Trova tutti gli studenti con il secondo voto piu basso
    second_lowest_students = [student[0] for student in students_sorted if student[1] == second_lowest_score]
    
    # Ordina i nomi in ordine alfabetico
    second_lowest_students.sort()
    
    # Stampa i nomi
    for student in second_lowest_students:
        print(student)

if __name__ == '__main__':
    n = int(input())  # Numero di studenti
    
    students = []
        
    # Raccolta dei nomi e dei voti degli studenti
    for _ in range(n):
        name = input()  # Nome dello studente
        score = float(input())  # Voto dello studente
        students.append((name, score))
    nestedList(students)

#--------------------------------------------------------
#List Comprehensions
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i_z, i_y, i_x] for i_z in range(x + 1)
                               for i_y in range(y + 1)
                               for i_x in range(z + 1)
                               if i_x + i_y + i_z != n]
    
    print(result)

'''
#--------------------------------------------------------
#Find the Runner-Up Score!
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_values = set(arr)
    sorted_vals= list(unique_values)
    sorted_vals.sort(reverse=True)


    print(sorted_vals[1])
'''
#--------------------------------------------------------
#Find the percentage
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = (sum(student_marks[query_name])/len(line))
    print("%.2f" % result)
'''
#--------------------------------------------------------
#Lists
'''
if __name__ == '__main__':
    N = int(input())
    res = []
    for _ in range(N):
        _input = input().split()
        
        match _input[0]:
            case "insert":
                res.insert(int(_input[1]), int(_input[2]))
            case "print":
                print(res)
            case "remove":
                res.remove(int(_input[1]))
            case "append":
                res.append(int(_input[1]))
            case "sort":
                res.sort()
            case "pop":
                res.pop()
            case "reverse":
                res.reverse()
'''
#--------------------------------------------------------
#Tuples
'''

if __name__ == '__main__':
    n = int(input())
    val = input().strip()
    val = list(map(int, val.split()))
    print(hash(tuple(val)))
    
'''
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
