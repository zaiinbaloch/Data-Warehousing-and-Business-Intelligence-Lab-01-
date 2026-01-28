import streamlit as st

# Function to calculate grade points
def point_cal(marks):
    if marks >= 85:
        return 4
    elif marks >= 80:
        return 3.7
    elif marks > 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 60:
        return 2.3
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0

st.title("GPA Calculator")

# Number of courses
no_of_courses = st.number_input("Enter number of courses", min_value=1, step=1)

T_point = 0
T_crhr = 0

# Input courses
for i in range(int(no_of_courses)):
    st.write(f"Course {i+1}")
    crhr = st.number_input(f"Credit hours for course {i+1}", min_value=0.0, step=0.5)
    marks = st.number_input(f"Marks obtained for course {i+1}", min_value=0.0, max_value=100.0, step=0.1)
    T_point += point_cal(marks) * crhr
    T_crhr += crhr

# Calculate GPA
if st.button("Calculate GPA"):
    if T_crhr == 0:
        st.error("No courses added!")
    else:
        gpa = T_point / T_crhr
        st.success(f"Your GPA is: {round(gpa, 2)}")
