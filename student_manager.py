import sys
import os 
from datetime import datetime

sys.path.insert(0, os.path.dirnime(__file__))


from src.lab9.group import Group
from src.lab8.models import Student


def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt'else ' clear')

def print_header(title):
    """Заголовок"""
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def show_all_students(group):
    """Показать всех студентов в виде таблицы"""
    students = group.list()

    if not students:
        print("\n📭 База данных пуста")
        return
    
    print_header("СПИСОК ВСЕХ СТУДЕНТОВ")

    print(f"Всего стуентов: {len(students)}\n")
    print(f"{'№':>3} {"ФИО" : <30} {"Дата родждения":<12} {"Группа" :<12} {"GPA":>6}")   
    print("-" * 70)

    for i, student in enumerate(students,1):
        print(f"{i:>3}. {student.fio:<30} {student.birthdate:<12} {student.group:<12} {student.gpa:>6.2f}")

def add_student_interactive(group):
    """Добавление нового студента"""
    print_header("ДОБАВЛЕНИЕ НОВОГО СТУДЕНТА")
    
    while True:
        fio = input("\nФИО студнента:").strip()
        if fio:
            break
        print("ФИО не может быть пустым чувак принкеси мн")
    
    while True:
        birthdate = input("Дата рождения (ГГГГ-ММ-ДД)").strip()
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
            break
        except ValueError:
            print("❌Неверный формат даты. Пример: 2007-10-10")
    
    group_name = input("Группа:").strip()

    while True:
        try:
            gpa = float(input("Средний балл(GPA,0.0-5.0):").strip())
            if 0.0 <= gpa <= 5.0:
                break
            print("❌ GPA должен быть от 0.0 до 5.0")
        except ValueError:
            print("❌ Введите число (например: 4.3)")
    
    ш9оош п м4уыя