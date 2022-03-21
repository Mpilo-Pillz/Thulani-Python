# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
num_of_students = 0
total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#   print(student_heights)

print(student_heights)
for height in student_heights:
  num_of_students += 1
print(f"num of students is {num_of_students}")

for height in student_heights:
  total_height += height

print(f"total height is {total_height}")
average_height = round(total_height / num_of_students)
print(f"average height is {average_height}")

#Write your code below this row 👇