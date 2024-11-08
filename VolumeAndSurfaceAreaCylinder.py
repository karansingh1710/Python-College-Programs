# 17. Write a program to find the volume and surface area of cylinder.
r=float(input("Enter the radius of Cylinder : "))
h=float(input("Enter the height of Cylinder : "))
# vol=pi*r^2*h
volume=3.14*r*r*h
surfaceArea=2*3.14*r*r + 2*3.14*r*h
print("Volume of Cylinder : ",volume)
print("Surface Area of Cylinder : ",surfaceArea)
