
student_hights=input("Please enter the hights").split()

for n in range(0,len(student_hights)):
    student_hights[n]=int(student_hights[n])
print(student_hights)

total_hight=sum(student_hights)
number_Of_Students=len(student_hights)
average_height=round(total_hight/number_Of_Students)