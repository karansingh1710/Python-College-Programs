# 20. Write a program to find the perimeter of a circle, rectangle and triangle
# Circle
r=float(input("Enter radius of Circle : "))
periCircle=2*3.14*r
print("Perimeter of Circle : ",periCircle)

# Rectangle
l=float(input("Enter length of Rectangle : "))
w=float(input("Enter width of Rectangle : "))
periRect=2*(l+w)
print("Perimeter of Rectangle : ",periRect)

# Triangle
a=float(input("Enter length of side a : "))
b=float(input("Enter length of side b : "))
c=float(input("Enter length of side c : "))
periTri=a+b+c
print("Perimeter of Triangle : ",periTri)