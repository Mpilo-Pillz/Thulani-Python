# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

min_score = 0

for score in student_scores:

    if score > 0 and min_score == 0:
        min_score = score

    if score < min_score:
        min_score = score


print(f"the min score is {min_score}")
#Write your code below this row 👇