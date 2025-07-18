# Student Grade Calculator

print("Welcome to Student Grade Calculator")

# Input student name
name = input("Enter student name: ")

# Input marks for 5 subjects
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []

for subject in subjects:
    score = int(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(score)

# Calculate total, percentage and grade
total = sum(marks)
percentage = total / len(subjects)

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display report
print("\n--- Student Report ---")
print("Name:", name)
print("Marks:", marks)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
