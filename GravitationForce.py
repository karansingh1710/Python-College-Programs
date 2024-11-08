# 23. Write a program to Find the Gravitational Force Acting Between Two Objects
# F=(G*m1*m2)/r^2
m1=float(input("Enter the mass of First Object : "))
m2=float(input("Enter the mass of Second Object : "))
r=float(input("Enter the distance between the centers of the two objects : "))

G=6.674*10**-11 #Nm^2kg^-2

F=(G*m1*m2)/r**2

print("Gravitational force : ",F," N")