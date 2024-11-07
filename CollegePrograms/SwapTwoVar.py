# 24. Write a program to swap the values of two variables.

a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

print("Before Swap : ")
print("a : ",a)
print("b : ",b)

temp=a
a=b
b=temp

print("After Swap : ")
print("a : ",a)
print("b : ",b)