# This script is used to calculate the GPA of a student 

# gpa_limit = int(input("What is your GPA Max ( 4 / 5 )? " ))
no_of_courses = int(input("WHat is the number of courses you have? "))

courses = []
credits = [] 
score = []
grade_point= []



# Getting the Courses, Credits  and the Score   

while len(courses) < no_of_courses:
    _ = input("Write your COURSES accordingly. ")
    courses.append(_)
    print(courses)
while len(credits) < no_of_courses:
    _ = int(input("Write your COURSE CREDITS accordingly. "))
    credits.append(_)
    print(courses)
    print(credits)
while len(score) < no_of_courses:
    _ = input("Write your COURSE SCORE accordingly. ").upper()
    score.append(_)
    print(courses)
    print(credits)
    print(score)


# Using the Credits and the score to calculate the GPA
A, B, C, D, E, F= 5, 4, 3, 2 , 1, 0

# for i in credits:
#     for j in courses:
#         print(credits[i])
#         print(score[j])
#         if credits[i] == courses[j]:
#             _ = i*j
#             grade_point.append(_)
#         else:
#             pass

for i in score:
    if i == 'A':
        i.replace('A', '5')
    if i == 'B':
        i.replace('B', "5")
    if i == 'C':
        i.replace('C', "5")
    if i == 'D':
        i.replace('D', "5")
    if i == 'E':
        i.replace('E', "5")
    if i == 'F':
        i.replace('F', '5')



for i in range(len(courses) + 1 ):
    _ = credits[i]
    s = score[i]
    if _ == s :
        _ = _ * s 
        grade_point.append(_)
    else:
        pass

        
for _ in tnsahe 
