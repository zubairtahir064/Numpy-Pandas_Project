import numpy as np
import os
import time
# stuid = np.genfromtxt('student_data.csv',delimiter=",", skip_header=1,usecols=0,dtype=str)
def avg_per_stud():
    marks = np.genfromtxt('student_data.csv', delimiter=',',skip_header=1,usecols=(1,2,3))
    avg_s = np.average(marks,axis=1)
    for i , avg in enumerate(avg_s,start=0):
        print(f"S0{i} Average: {avg:.2f}")

def avg_per_sub():
    marks = np.genfromtxt('student_data.csv', delimiter=',',skip_header=1,usecols=(1,2,3))
    avg_sub = np.mean(marks,axis=0)
    subject = ["Math","Physics","CS"]
    for subject , avg in zip(subject,avg_sub):
        print(f"Average Marks in {subject}: {avg:.2f}")

def highest_marks_in_class():
    marks = np.genfromtxt('student_data.csv', delimiter=',',skip_header=1,usecols=(1,2,3))
    sum_stu = np.sum(marks,axis=1)
    total = np.array([])
    for i , sum in enumerate(sum_stu,start=0):
        total_arr = np.append(total,sum_stu)
    maximum = int(np.max(total_arr))
    print(f"Highest number in Class is {maximum}")

def lowest_marks_in_class():
    marks = np.genfromtxt('student_data.csv', delimiter=',',skip_header=1,usecols=(1,2,3))
    sum_stu = np.sum(marks,axis=1)
    total = np.array([])
    for i , sum in enumerate(sum_stu,start=0):
        total_arr = np.append(total,sum_stu)
    minimum = int(np.min(total_arr))
    print(f"Lowest number in Class is {minimum}")

def average_marks_in_class():
    marks = np.genfromtxt('student_data.csv', delimiter=',',skip_header=1,usecols=(1,2,3))
    sum_stu = np.sum(marks,axis=1)
    total = np.array([])
    for i , sum in enumerate(sum_stu,start=0):
        total_arr = np.append(total,sum_stu)
    avg = np.average(total_arr)
    print(f"Average number in Class is {avg:.2f}")

def grade_classification():
    data = np.genfromtxt(
        'student_data.csv',
        delimiter=',',
        names=True,
        dtype=None,
        encoding=None
    )
    # Calculate total marks
    total_marks = data["Math"] + data["Physics"] + data["CS"]
    # Loop and print
    for sid, total in zip(data["StudentID"], total_marks):

        # Grade logic
        if total >= 270:
            grade = "A"
        elif total >= 240:
            grade = "B"
        elif total >= 210:
            grade = "C"
        elif total >= 180:
            grade = "D"
        else:
            grade = "F"
        print(f"{sid}  |  Total: {total}  |  Grade: {grade}")
        print("=============================================")

def count_student_in_grade():

    data = np.genfromtxt(
    'student_data.csv',
    delimiter=',',
    names=True,
    dtype=None,
    encoding=None
    )
    grade_arr = np.array([])
    # Calculate total marks
    total_marks = data["Math"] + data["Physics"] + data["CS"]
    # Loop and print
    for sid, total in zip(data["StudentID"], total_marks):

        # Grade logic
        if total >= 270:
            grade = "A"
            grade_arr = np.append(grade_arr,"A")
        elif total >= 240:
            grade = "B"
            grade_arr = np.append(grade_arr,"B")
        elif total >= 210:
            grade = "C"
            grade_arr = np.append(grade_arr,"C")
        elif total >= 180:
            grade = "D"
            grade_arr = np.append(grade_arr,"D")
        else:
            grade = "F"
            grade_arr = np.append(grade_arr,"F")

    g = ["A","B","C","D","F"]
    for i in range(5):
        mask = grade_arr == g[i]
        count = mask.sum()
        print(f"Total {g[i]} Grade Student: ",count)

def clear_screen():
    # Check the operating system and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # For Windows
    else:
        _ = os.system('clear') # For Linux and macOS
    
while True:
    print()
    print()
    print("=============================================")
    print("1.To Calculate Average mark of per Student")
    print("2.To Calculate the Average mark of per Subject")
    print("3.Highest marks in class")
    print("4.Lowest marks in class")
    print("5.Overall Avergae Marks of Class")
    print("6.View Grade of all student")
    print("7.View how many student in Each Grade")
    print("8.Exits")
    choice = int(input('Select the option: '))
    if choice == 1:
        avg_per_stud()
    elif choice == 2:
        avg_per_sub()
    elif choice == 3:
        highest_marks_in_class()
    elif choice == 4:
        lowest_marks_in_class()
    elif choice == 5:
        average_marks_in_class()
    elif choice == 6:
        grade_classification()
    elif choice == 7:
        count_student_in_grade()
    elif choice == 8:
        print("Thank you for use my Program 😊😘😘")
        break
    else:
        print("Enter correct option!")
    


