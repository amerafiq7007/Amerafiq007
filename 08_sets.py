# fruits = {apple, banana, orange}
# numbers = {1, 2, 3, 4, 5}



# fruits.add("kiwi")
# fruits.remove("banana")
# fruits.discard("grape")

# print(fruits)


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))




grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95),
    ("Charlie", "English", 85),
    ("David", "Math", 60),
    ("Eve", "Science", 91)
]

# 1️⃣ Unique Students & Subjects
students = set()
subjects = set()

for name, subject, mark in grades:
    students.add(name)
    subjects.add(subject)

print("Unique Students:", students)
print("Unique Subjects:", subjects)


# 2️⃣ High Performers (>= 90)
top_students = set()

for name, subject, mark in grades:
    if mark >= 90:
        top_students.add(name)

print("Top Students:", top_students)


# 3️⃣ Consistent Students (ambil lebih dari 1 subject)
student_subjects = {}

for name, subject, mark in grades:
    if name not in student_subjects:
        student_subjects[name] = set()
    student_subjects[name].add(subject)

consistent_students = set()

for name in student_subjects:
    if len(student_subjects[name]) > 1:
        consistent_students.add(name)

print("Consistent Students:", consistent_students)


# 4️⃣ Subject Topper
topper = {}

for name, subject, mark in grades:
    if subject not in topper or mark > topper[subject][1]:
        topper[subject] = (name, mark)

print("Topper by Subject:", topper)


# 5️⃣ Students Fail (< 70)
fail_students = set()

for name, subject, mark in grades:
    if mark < 70:
        fail_students.add(name)

print("Fail Students:", fail_students)


# 6️⃣ Common Subjects (Alice & Bob)
alice_subjects = set()
bob_subjects = set()

for name, subject, mark in grades:
    if name == "Alice":
        alice_subjects.add(subject)
    if name == "Bob":
        bob_subjects.add(subject)

common = alice_subjects.intersection(bob_subjects)

print("Common Subjects (Alice & Bob):", common)


# 7️⃣ Bonus: Average Function
def get_student_average(name):
    total = 0
    count = 0
    
    for student, subject, mark in grades:
        if student == name:
            total += mark
            count += 1
    
    if count == 0:
        return 0
    
    return total / count


print("Average Alice:", get_student_average("Alice"))
print("Average Bob:", get_student_average("Bob"))


