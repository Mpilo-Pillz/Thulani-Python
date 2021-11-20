# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

print(f"the maximum socre is {max(student_scores)}")
print(f"the minimum score is {min(student_scores)}")

#Write your code below this row 👇