# 25. Write a program to swap the values of two variables without using third variable.

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

print("Before Swap : ")
print("a : ",a)
print("b : ",b)

a=a+b
b=a-b
a=a-b

print("After Swap : ")
print("a : ",a)
print("b : ",b)