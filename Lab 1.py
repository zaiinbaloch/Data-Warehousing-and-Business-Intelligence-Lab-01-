def point_cal(marks):
    if  marks >=85:
        return 4
    elif marks >= 80:
        return 3.7
    elif marks > 75:
        return 3.3
    elif marks>= 70 :
        return 3.0
    elif marks >=  65:
        return 2.7
    elif marks >= 60 :
        return 2.3
    elif marks >= 55 :
        return 2.0
    elif marks >= 50 :
        return 1.7
    else :
        return 0
no_of_courses = int(input("Enter number of courses you have registered "))
T_point =0
T_crhr= 0 
print("Enter Credit hours and marks of each course one by one :")
for x in range (no_of_courses):
    crhr= float(input("Enter Credit hours of your course "))
    T_crhr += crhr
    marks= float(input("Enter obtained marks "))
    grade_point = point_cal(marks) *crhr
    T_point +=grade_point
Gpa =T_point/T_crhr
print(round(Gpa,2))
