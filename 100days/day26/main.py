names=["anurag",'jatin','anshika','shivani','saurabh']
# new=[name.upper() for name in names if len(name)>5 ]
# print(new)


#dictionary comprehension

# import random
#
# scores={
#     student:random.randint(50,100) for student in names
# }
# print(scores)
scores={'anurag': 81, 'jatin': 73, 'anshika': 54, 'shivani': 88, 'saurabh': 74}

passed_student={student:score for (student,score) in scores.items() if score>60}
print(passed_student)