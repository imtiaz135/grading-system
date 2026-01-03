def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep up the good work"
    elif marks >= 80:
        return "B", "Great job! You are doing very well "
    elif marks >= 70:
        return "C", "Good effort! You can do even better "
    elif marks >= 60:
        return "D", "Don't give up! Keep practicing "
    else:
        return "F", "Failure is the first step to success. Try again "



student_name = input("Enter student name: ")


while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

grade, message = calculate_grade(marks)


print("\n Student Result")
print("Name   :", student_name)
print("Marks :", marks)
print("Grade :", grade)
print("Message:", message)
