students = {
    1: {"name": "EEE", "age": 23},
    2: {"name": "HHH", "age": 20},
    3: {"name": "KKK", "age": 19},
}

for student_id, details in students.items():  # Corrected 'student' to 'students'
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")  # Fixed the missing bracket
