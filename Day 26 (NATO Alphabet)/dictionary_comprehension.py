import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(0, 100) for student in names}

print(students_scores)

# Dictionary Comprehension
