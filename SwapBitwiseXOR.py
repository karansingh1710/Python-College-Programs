# 44. Write a program to Swap the Contents of two Numbers using Bitwise XOR Operation
a=5
b=3
print("Before Swap : ")
print("a :",a)
print("b :",b)

a=a^b
b=a^b
a=a^b
print("After Swap : ")
print("a :",a)
print("b :",b)