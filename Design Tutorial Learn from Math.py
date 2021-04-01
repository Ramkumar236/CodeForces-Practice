# import math
# def isPrime(num):
#     for i in range(2, int(math.sqrt(num))+1):
#         if num%i==0:
#             return True
#     return False
#
# n = int(input())
# i = 4
# for i in range(2,n//2):
#     if isPrime(n-i) and isPrime(i)==1:
#         print(f"{i} {n-i}")
#         break
x = int(input())
if x%2 == 0:
    print(f"{4} {x-4}")
else:
    print(f"{9} {x-9}")