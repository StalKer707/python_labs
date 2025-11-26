from models import Student
from serialize import students_to_json, students_from_json

def test_student():
    print("=== Тестим класс Student ===")
    student1 = Student(
        fio = "Горьковой Владислав",
        birthdate = "2005-07-27",
        group = "SE-01",
        gpa = 4.5
    )
    print("Студент создан")
    print(student1)
    print(f'Возраст: {student1.age()} лет')
    print(f'словарь:{student1.to_dict()}')
    print()


def test_serialization():
    print("===Чекаем сериализации===")
    students = [
        Student("Горьковой Владислав","2005-07-27", "SE-01", 4.5),
        Student("Королева Дарья", "2006-09-27", "SE-02", 3.8),
        Student("Старостина Полина Дьяволица", "2008-01-18", "SE-03", 5)
    ]
    students_to_json(students,"src/lab1/lab8/students_output.json")
    print("Студенты сохранены в students_output.json")

    loaded_students = students_from_json("src/lab1/lab8/students_input.json")
    print("Студенты загружены")
    for student in loaded_students:
        print(f" - {student}")
    print()

def test_validation():
    print("===Чекаем валидации===")
    try:
        Student('Тест', "2020-13-45", "SE-01", 3.0)
    except ValueError as e:
        print(f"Чувак рил ошибка валидации: {e} ")

    
    try:
        Student("Тест", "2020-01-01", "SE-02", 6)
    except ValueError as e:
        print(f"Кореш ошибка при валидации GPA: {e} ")
if __name__ == "__main__":
    test_student()
    test_validation()
    test_serialization()
    print("S.W.A.T.")