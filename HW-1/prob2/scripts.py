#SOLUTIONS OF PROBLEM 2 

#EX_1
#https://www.hackerrank.com/challenges/birthday-cake-candles
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)


#EX_2
#https://www.hackerrank.com/challenges/kangaroo
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) * (v1 - v2) > 0:
        return "YES"
    else:
        return "NO"

#EX_3
#https://www.hackerrank.com/challenges/strange-advertising
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    liked = [2]
    reached = 6
    for i in range(n-1):
        liked.append(math.floor(reached/2))
        reached = liked[-1]*3
        
    return sum(liked)

#EX_4
#https://www.hackerrank.com/challenges/recursive-digit-sum#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    
    initial_sum = sum(int(d) for d in n) 
    total_sum = initial_sum * k
    
    if len(str(total_sum)) == 1:
        return int(total_sum)
        
    return superDigit(str(total_sum), 1)


#EX_5
#https://www.hackerrank.com/challenges/insertionsort1#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    unsorted_value = arr[-1]
    i = n - 2
    
    while i >= 0 and arr[i] > unsorted_value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    
    arr[i + 1] = unsorted_value
    print(*arr)


#EX_6
#https://www.hackerrank.com/challenges/insertionsort2
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    
    def insertionSort1(n, arr):
        unsorted_value = arr[-1]
        i = n - 2
        while i >= 0 and arr[i] > unsorted_value:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = unsorted_value
        return arr
        
    for i in range(2, n+1, 1):
        arr[:i] = insertionSort1(len(arr[:i]), arr[:i])
        print(*arr)
    return
