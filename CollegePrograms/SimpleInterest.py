# 21. Write a program to Compute Simple Interest.
p=float(input("Enter Principal Amount : "))
rate=float(input("Enter rate : "))
time=int(input("Enter time in years : "))

si=(p*rate*time)/100
print("Simple Interest : ",si," Rs.")
print("Total Amount : ",si+p," Rs.")