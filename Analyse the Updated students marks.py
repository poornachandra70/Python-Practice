student_count = int(input())
marks = []

# Read and store all marks using append()
for _ in range(student_count):
    marks.append(int(input()))

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update the mark at the entered student position (converting position to 0-based index)
index = position - 1
marks[index] = corrected_mark

# Calculate the total, average, highest and lowest marks
total_marks = sum(marks)
average_marks = total_marks / student_count
highest_mark = max(marks)
lowest_mark = min(marks)

# Count how many students passed using a loop and a condition
passed_count = 0
for mark in marks:
    if mark >= passing_mark:
        passed_count += 1

# Display the output exactly as required
print(f"Updated Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Students: {passed_count}")