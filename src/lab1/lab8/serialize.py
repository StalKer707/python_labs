import json
from models import Student

def students_to_json(students: list[Student], path: str):
    data = [student.to_dict() for student in students]

    with open (path, "w", encoding= "utf-8") as f:
        json.dump(data,f, ensure_ascii=False, indent=2)

def students_from_json(path:str) -> list [Student]:
    with open (path, "r", encoding = "utf-8") as f:
        data = json.load(f)
    students = []
    for item in data:
        try: 
            student = Student.from_dict(item)
            students.append(student)
        except(ValueError, KeyError) as e:
            print(f"ошиька при создании студента: {e}")
    return students