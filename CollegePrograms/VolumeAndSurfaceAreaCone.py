# 18. Write a program to find the surface area and volume of a cone.

r=float(input("Enter the radius of Cone : "))
h=float(input("Enter the height of Cone : "))
l=float(input("Enter the slant height of Cone: "))

volume=(3.14*r*r*h)/3
surfaceArea=3.14*r*(r+l)
print("Volume of Cone : ",volume)
print("Surface Area of Cone : ",surfaceArea)