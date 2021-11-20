# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#   print(student_heights)

  total_height += int(student_heights[n])
  print(total_height)

average_height = total_height / len(student_heights)

print(average_height )

#Write your code below this row 👇