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
'''

if __name__ == '__main__':
    n = int(input())  # Numero di studenti
    
    students = []
        
    # Raccolta dei nomi e dei voti degli studenti
    for _ in range(n):
        name = input()  # Nome dello studente
        score = float(input())  # Voto dello studente
        students.append((name, score))
    nestedList(students)
'''
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
#STRING SPLIT AND JOIN
def split_and_join(line):
    # split the string
    words = line.split(" ")
    
    # merge strings
    return "-".join(words)
#--------------------------------------------------------
#sWAP cASE
def swap_case(s):    
    return s.swapcase()

#--------------------------------------------------------
#What's Your Name?
def print_full_name(first, last):
    print(
        "Hello "+first+" "+last+"! You just delved into python."
    )

#--------------------------------------------------------
#Mutations
def mutate_string(string, position, character):
    str_lst = list(string)
    str_lst[position] = character
    return ''.join(str_lst)


#--------------------------------------------------------
#Find a string
def count_substring(string, sub_string):
    cnt = 0
    i = 0
    while i < len(string):
        
        pos = string.find(sub_string, i)

        if pos != -1:
            cnt += 1
            i = pos + 1
        else:
            break

    return cnt
#--------------------------------------------------------
#String Validators
'''
if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
''' 


#--------------------------------------------------------
#Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness-1) + c + (c * i).ljust(thickness))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#--------------------------------------------------------
#Text Wrap
def wrap(string, max_width):
    
    return textwrap.fill(string, max_width)

#--------------------------------------------------------
#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
def design_door_mat(n,m):
    # parte superiore
    for i in range(n // 2):
        pattern = ('.|.' * (2 * i + 1)).center(m, '-')
        print(pattern)
    
    # riga centrale
    welcome_line = "WELCOME".center(m, '-')
    print(welcome_line)
    
    # parte inferiore
    for i in range(n // 2 - 1, -1, -1):
        pattern = ('.|.' * (2 * i + 1)).center(m, '-')
        print(pattern)

if __name__ == '__main__':
    # Input: N and M
    input_ = input().strip()
    n,m = map(int, input_.split())
    design_door_mat(n,m)


#--------------------------------------------------------
#String Formatting
def print_formatted(number):
    #max witdh :=
    width = len(bin(number)) - 2  # minus 2 for '0b'
    
    for i in range(1, number + 1):
        # Format the output
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)  # minus '0o'
        hexadecimal = hex(i)[2:].upper().rjust(width)  # minus '0x' 
        binary = bin(i)[2:].rjust(width)  # minus '0b'

        print(f"{decimal} {octal} {hexadecimal} {binary}")


#--------------------------------------------------------
#Alphabet Rangoli
import string
def print_rangoli(size):
    c = string.ascii_lowercase[:size]

    rows = []
    
    # Create the lower part
    for i in range(size - 1, 0, -1):
        core_string = '-'.join(c[size-1:i:-1] + c[i:size])
        rows.append(core_string.center(size * 4 - 3, '-'))


    # Create the upper part including the middle row
    for i in range(size):
        core_string = '-'.join(c[size-1:i:-1] + c[i:size])
        rows.append(core_string.center(size * 4 - 3, '-'))

    print('\n'.join(rows))
    return '\n'.join(rows)

#--------------------------------------------------------
#Capitalize!

# Complete the solve function below.
def solve(s):
    res = s.split(' ')
    res = [ i.capitalize() for i in res ]
    return ' '.join(res)


#--------------------------------------------------------
#The Minion Game
def minion_game(string):

    kScore = 0
    sScore = 0

    for i in range(len(string)):

        if string[i] in 'AEIOU':  # "Kevin has to make words starting with vowels. "
        
            # you'll have one subtring as string[i:] in string
            # plus, you have to count all substring of "string" definend as:
            #   string[i:x] where x goes from i to len(string) -1 
            #
            #consideration about multiple occurrence of a substring:
            #   considering the example "BANANA", we notice that "AN" occours 2 times,
            #       first : starting on index 1, second : starting on index 3
            #   it is counted individually, each time the index "i" of the for goes in 1 and then in 3
            kScore += len(string) - i  
        else:  #" Stuart has to make words starting with consonants."
            sScore += len(string) - i  # 
    
    # Determine the winner
    if sScore > kScore :
        print("Stuart "+str(sScore))
    elif sScore < kScore:
        print("Kevin "+str(kScore))
    else:
        print("Draw")



#--------------------------------------------------------
#Merge the Tools!
def merge_the_tools(string, k):
    substrs = [ string[i:i+k] for i in range(0,len(string) -k + 1,k) ]
    res = []
    tmp_word = "" 
    for substr in substrs:
        tmp_word = "" 
        for i,c in enumerate(substr):
            if i> 0 and c in substr[0:i]:
                continue
            tmp_word += c
        print(tmp_word)
        res.append(tmp_word)
                
        
    

###################################################################
#• Sets (all – total: 13 - max points: 170)
#https://www.hackerrank.com/domains/python/py-sets
###################################################################
#• Collections (all – total: 8 - max points: 220)
#https://www.hackerrank.com/domains/python/py-collections
###################################################################
#• Date and Time (all – total: 2 - max points: 40)
#https://www.hackerrank.com/domains/python/py-date-time

#Calendar Module
import calendar

def getDay(date):
    mm, dd, yyyy = map(int, date.split())
    
    day_index = calendar.weekday(yyyy, mm, dd)
    
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    
    print(days[day_index])

'''
if __name__ == '__main__':
    date_ = input() 
    getDay(date_)
'''
#--------------------------------------------------------
#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):    
    dt1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    dt2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    delta = abs(int((dt1 - dt2).total_seconds()))
    
    return str(delta)
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write((delta) + '\n')

    fptr.close()
'''
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
