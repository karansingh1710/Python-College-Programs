# 4. Write a program to Calculate Sum of 5 Subjects and Find Percentage (Max Mark in each subject
# is 100).
s1=float(input())
s2=int(input("Enter marks of Second Subject : "))
s3=int(input("Enter marks of Third Subject : "))
s4=int(input("Enter marks of Fourth Subject : "))
s5=int(input("Enter marks of Fifth Subject : "))

totalMarks=s1+s2+s3+s4+s5

percent=totalMarks/5

print("Total Marks ",totalMarks," out of 500")
print("Percentage is ",percent,"%")