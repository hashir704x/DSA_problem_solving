def countDigitsInNumber(num):
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1
    return count

def reverseNumber(num):
    output = 0
    while num != 0:
        mod = num % 10
        output = output * 10 + mod
        num = num // 10
    return output

def checkPalindrome(num):
    reversedNumber = reverseNumber(num)
    print(reversedNumber)
    if num == reversedNumber:
        return True
    else:
        return False

def getLargestDigitFromNumber(num):
    largest = num % 10
    while num != 0:
        mod = num % 10
        if largest < mod:
            largest = mod
        num = num // 10
    return largest

def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
    return total

def isArmstrongNumber(num):
    length = 0
    num1 = num
    while num1 != 0:
        length = length + 1
        num1 = num1 // 10
    num2 = num
    total = 0
    while num2 != 0:
        mod = num2 % 10
        total = total + mod ** length
        num2 = num2 // 10
    print(total)
    if total == num:
        return True
    else:
        return False

def isPerfectNumber(num):
    total = 0
    for i in range(1, num): 
        if num % i == 0:
            total = total + i
    if total == num:
        return True
    else:
        return False

def isPrimeNumber(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def GCD(num1, num2):
    smaller = None
    if num1 <= num2:
        smaller = num1
    else:
        smaller = num2
    greaterDivisor = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            if greaterDivisor < i:
                greaterDivisor = i
    return greaterDivisor

def LCM(num1, num2):
    greater = None
    if num1 >= num2:
        greater = num1
    else:
        greater = num2
    i = greater
    while True:
        if i % num1 == 0 and i % num2 == 0:  
            return i
        i = i + 1
print(LCM(31, 73))
