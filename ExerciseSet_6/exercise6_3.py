# Ask the number of students
number_students = int(input("How many students?\n"))
#  list for calculate the average
grades = []


for i in range(number_students):
    # Ask the exam grade of each student
    grade = int(input("Student grade:\n"))
    grades.append(grade)

# Calculate the average of the grades
grade_average = sum(grades) / len(grades)

# Calculate the median value of the grades:
grade_median = 0.0

if len(grades) % 2 != 0:
    grade_median = grades[len(grades) // 2]
else:
    grade_median = (grades[(len(grades) // 2) - 1] + grades[(len(grades) // 2)]) / 2


# Calculate the most common grade:
def most_frequent(grades):
    counter = 0
    num = grades[0]

    for x in grades:
        curr_frequency = grades.count(x)
        if curr_frequency > counter:
            counter = curr_frequency
            num = x

    return num

print(f"Average grade: {grade_average}")
print(f"Median grade: {grade_median}")
print(f"Most common grade: {most_frequent(grades)}")

# Text description of the average
if 0 <= grade_average < 1:
    print("Bad result")
elif 1 <= grade_average < 2:
    print("Weak result")
elif 2 <= grade_average < 3:
    print("Average result")
elif 3 <= grade_average < 4:
    print("Good result")
elif 4 <= grade_average <= 5:
    print("Excellent result")
