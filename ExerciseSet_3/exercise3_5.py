# just implement a grade:
grade = 0

# input
points = int(input("Exam points:\n"))

# if points between 0 - 50:
if 0 <= points <= 50:
    grade = 0
    print(f"Grade: {grade}")
# if points between 51 - 60:
elif 51 <= points <= 60:
    grade = 1
    print(f"Grade: {grade}")
# if points between 61 - 70:
elif 61 <= points <= 70:
    grade = 2
    print(f"Grade: {grade}")
# if points between 71 - 80:
elif 71 <= points <= 80:
    grade = 3
    print(f"Grade: {grade}")
# if points between 81 - 90:
elif 81 <= points <= 90:
    grade = 4
    print(f"Grade: {grade}")
# if points between 91 - 100:
elif 91 <= points <= 100:
    grade = 5
    print(f"Grade: {grade}")
else:
    print("Invalid points value.")


