# For loop

# for i in range (1,20,1):
#     print(i)

# for i in range(20,51):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

# for i in range (-5,-15,-1):
#     print(i)


# for i in range(5,51,5):
    # print(i)

# n = int(input("which table u want ? "))

# for i in range(n,(n*10)+1 , n):
#     print(i) 

# a = 'sheryians teacher what industry needs'
# print(len(a))

# for i in range(len(a)) :
#     print(a[i])

# a = 'sheryians is cool'

# for i in a :
#     print(i)

# for i in range (1,21):
#     if (i == 10):
#         break
#     else: 
#         print(i)


# for i in range (1,21):
#     if (i == 10):
#         continue
#     print(i)


# for i in range (1,21):
#     if (i == 30):
#         print("break statement executed")
#         break
#     print(i)

# else :                                         # if break statement is not executed then else is executed and vice versa
#     print("break statement is not executed")


# n = int (input("Enter a number"))
# for i in range(n) : 
#     print("Hello World")


# n = int(input("Enter a numberb : "))
# for i in range(1,n+1):
#     print(i)


# n = int(input("Enter a number : "))
# for i in range (n, 0 , -1):
#     print(i)


# num = int(input("which table u want to have : "))
# for i in range(num , (num*10)+1 , num):
#     print(i)

# n = int(input("which table u want to have : "))
# for i in range (1,11):
#     print(f"{n} * {i} = {n*i}")


# num = int(input("Enter number to find sum of : "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(f"Sum is {sum}")


# n = int(input("Enter the number of Factorial : "))
# mul = 1
# for i in range (1, n+1):
#     mul *= i
# print(f"Factorial is {mul}")


# n = int(input("Enter a number : "))
# odd_sum = 0
# even_sum = 0
# for i in range (1,n+1):
#     if (i % 2 == 0):
#         even_sum += i
#     else : 
#         odd_sum += i

# print(f"Odd sum is {odd_sum}")
# print(f"Even sum is {even_sum}")


# n = int(input("Enter number to find factor of : "))
# for i in range(1,n+1):
#     if(n % i == 0):
#         print(i)


# n = int(input("Enter number to check it is perfect number or not : "))
# sum = 0
# for i in range(1,n):
#     if(n % i == 0):
#         sum += i

# if (sum == n):
#     print(f"{n} is a perfect number")
# else :
#     print(f"{n} is not a perfect number")
    

# num = int(input("Enter a number : "))
# for i in range (2, num):
#     if (num % i == 0):
#         print(f"{num} is not a prime number")
#         break
#     else : 
#         print(f"{num} is a perfect number")
#         break


# a = input("Enter a string : ")
# b = ""
# for i in range (len(a)-1 , -1 , -1):
#     b += a[i]

# if (a == b):
#     print(f"{a} is Palindrome")
# else :
#     print(f"{a} is not a palindrome")


# a = "Pna89#*afj$*943"

# char = 0
# digit = 0
# specialChar = 0

# for i in a:
#     if  i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else :
#         specialChar += 1

# print(f"Char are {char}\nDigits are {digit}\nSpecial Char are {specialChar}")


# print(dir(str))


 # while loops 

# a = 1
# while (a <= 30):
#     print(a)
#     a += 1


# num = int(input("Enter you number : "))
# while (num > 0):
#     print(num % 10)
#     num //= 10


# num = int(input("Enter you number : "))
# newNum = 0
# while (num > 0):
#     rem = num % 10
#     newNum = newNum * 10 + rem
#     num //= 10

# print(newNum)


# num = int(input("Enter you number : "))
# newNum = 0
# dubNum = num
# while (dubNum > 0):
#     rem = dubNum % 10
#     newNum = newNum * 10 + rem
#     dubNum //= 10

# if (newNum == num ):
#     print(f"{num} is Palindrome")
# else : 
#     print(f"{num} is not Palindrome")


import random

num = random.randint(1,10)

tries = 0

while(True):
    guess = int(input("Please guess the number between 1 t0 10 : "))

    if (num == guess):
        tries += 1
        print(f"You guessed it correctly in {tries} tries")
        break

    elif ( num < guess):
        tries += 1
        print("Guess a little lower value")

    elif ( num > guess):
        tries += 1
        print("Guess a little higher value")
    else :
        tries += 1
        print("try again")

