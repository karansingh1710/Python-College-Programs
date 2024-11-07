# 16. Write a program to find the volume and surface area of cuboids.
l=float(input("Enter the length of Cuboid : "))
w=float(input("Enter the width of Cuboid : "))
h=float(input("Enter the height of Cuboid : "))

volume=l*w*h
surfaceArea=2*l*w + 2*l*h +2*w*h

print("Volume of Cuboid : ",volume)
print("Surface Area of Cuboid : ",surfaceArea)