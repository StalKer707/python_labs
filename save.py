# interactive.py - УЛУЧШЕННАЯ ВЕРСИЯ С МЕНЮ
import sys
import os
from datetime import datetime

# Настраиваем пути для импорта
sys.path.insert(0, os.path.dirname(__file__))

from src.lab9.group import Group
from src.lab8.models import Student

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Красивый заголовок"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def show_all_students(group):
    """Показать всех студентов в виде таблицы"""
    students = group.list()
    
    if not students:
        print("\n📭 База данных пуста")
        return
    
    print_header("СПИСОК ВСЕХ СТУДЕНТОВ")
    
    print(f"Всего студентов: {len(students)}\n")
    print(f"{'№':>3} {'ФИО':<30} {'Дата рождения':<12} {'Группа':<12} {'GPA':>6}")
    print("-" * 70)
    
    for i, student in enumerate(students, 1):
        print(f"{i:>3}. {student.fio:<30} {student.birthdate:<12} {student.group:<12} {student.gpa:>6.2f}")

def add_student_interactive(group):
    """Добавление нового студента"""
    print_header("ДОБАВЛЕНИЕ НОВОГО СТУДЕНТА")
    
    while True:
        fio = input("\nФИО студента: ").strip()
        if fio:
            break
        print("❌ ФИО не может быть пустым")
    
    while True:
        birthdate = input("Дата рождения (ГГГГ-ММ-ДД): ").strip()
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Неверный формат даты. Пример: 2003-10-10")
    
    group_name = input("Группа: ").strip()
    
    while True:
        try:
            gpa = float(input("Средний балл (GPA, 0.0-5.0): ").strip())
            if 0.0 <= gpa <= 5.0:
                break
            print("❌ GPA должен быть от 0.0 до 5.0")
        except ValueError:
            print("❌ Введите число (например: 4.3)")
    
    student = Student(fio, birthdate, group_name, gpa)
    
    try:
        group.add(student)
        print(f"\n✅ Студент '{fio}' успешно добавлен!")
    except ValueError as e:
        print(f"\n❌ Ошибка: {e}")
    except Exception as e:
        print(f"\n❌ Неожиданная ошибка: {e}")

def find_student_interactive(group):
    """Поиск студента по ФИО"""
    print_header("ПОИСК СТУДЕНТА")
    
    substr = input("\nВведите часть ФИО для поиска: ").strip()
    if not substr:
        print("❌ Введите текст для поиска")
        return
    
    found = group.find(substr) 
    
    if not found:
        print(f"\n😞 По запросу '{substr}' ничего не найдено")
        return
    
    print(f"\n✅ Найдено {len(found)} студентов:\n")
    for i, student in enumerate(found, 1):
        print(f"{i}. {student.fio}")
        print(f"   📅 Дата рождения: {student.birthdate}")
        print(f"   🏫 Группа: {student.group}")
        print(f"   📊 GPA: {student.gpa:.2f}")
        if i < len(found):
            print("   " + "-" * 40)

def delete_student_interactive(group):
    """Удаление студента"""
    print_header("УДАЛЕНИЕ СТУДЕНТА")
    
    students = group.list()
    if not students:
        print("📭 База данных пуста")
        return
    
    show_all_students(group)
    
    print("\nВыберите способ удаления:")
    print("1. По номеру из списка")
    print("2. По ФИО")
    print("0. Отмена")
    
    method = input("\nВаш выбор (0-2): ").strip()
    
    if method == "0":
        print("❌ Удаление отменено")
        return
    
    if method == "1":
        try:
            num = int(input("\nВведите номер студента: "))
            if 1 <= num <= len(students):
                student = students[num - 1]
                fio = student.fio
            else:
                print("❌ Неверный номер")
                return
        except ValueError:
            print("❌ Введите число")
            return
    
    elif method == "2":
        fio = input("\nВведите ФИО студента: ").strip()
        if not fio:
            print("❌ ФИО не может быть пустым")
            return
    else:
        print("❌ Неверный выбор")
        return
    
    # Подтверждение
    confirm = input(f"\n⚠️  Вы уверены, что хотите удалить студента '{fio}'? (да/НЕТ): ")
    if confirm.lower() == 'да':
        if group.remove(fio):
            print(f"\n✅ Студент '{fio}' успешно удален")
        else:
            print(f"\n❌ Студент с ФИО '{fio}' не найден")
    else:
        print("\n❌ Удаление отменено")

def update_student_interactive(group):
    """Обновление данных студента"""
    print_header("ОБНОВЛЕНИЕ ДАННЫХ СТУДЕНТА")
    
    students = group.list()
    if not students:
        print("📭 База данных пуста")
        return
    
    show_all_students(group)
    
    try:
        num = int(input("\nВведите номер студента для обновления: "))
        if not 1 <= num <= len(students):
            print("❌ Неверный номер")
            return
    except ValueError:
        print("❌ Введите число")
        return
    
    student = students[num - 1]
    print(f"\n📝 Обновление студента: {student.fio}")
    
    fields_to_update = {}
    
    print("\nВыберите поля для обновления (можно несколько через запятую):")
    print("1. ФИО")
    print("2. Дата рождения")
    print("3. Группа")
    print("4. GPA")
    print("0. Отмена")
    
    choices = input("\nВаш выбор: ").strip().split(',')
    
    if '0' in choices or not any(c.strip() in '1234' for c in choices):
        print("❌ Обновление отменено")
        return
    
    if '1' in choices:
        new_fio = input("Новое ФИО: ").strip()
        if new_fio:
            fields_to_update['fio'] = new_fio
    
    if '2' in choices:
        while True:
            new_birthdate = input("Новая дата рождения (ГГГГ-ММ-ДД): ").strip()
            try:
                datetime.strptime(new_birthdate, "%Y-%m-%d")
                fields_to_update['birthdate'] = new_birthdate
                break
            except ValueError:
                print("❌ Неверный формат даты")
    
    if '3' in choices:
        new_group = input("Новая группа: ").strip()
        if new_group:
            fields_to_update['group'] = new_group
    
    if '4' in choices:
        while True:
            try:
                new_gpa = float(input("Новый GPA (0.0-5.0): ").strip())
                if 0.0 <= new_gpa <= 5.0:
                    fields_to_update['gpa'] = str(new_gpa)
                    break
                print("❌ GPA должен быть от 0.0 до 5.0")
            except ValueError:
                print("❌ Введите число")
    
    if fields_to_update:
        try:
            group.update(student.fio, **fields_to_update)
            print("\n✅ Данные успешно обновлены!")
        except Exception as e:
            print(f"\n❌ Ошибка при обновлении: {e}")
    else:
        print("\n❌ Не выбрано ни одного поля для обновления")

def show_statistics(group):
    """Показать статистику"""
    print_header("СТАТИСТИКА")
    
    stats = group.stats()
    
    if stats['count'] == 0:
        print("📭 В базе нет студентов")
        return
    
    print(f"👥 Общее количество студентов: {stats['count']}")
    print(f"📊 Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"⬇️  Минимальный GPA: {stats['min_gpa']:.2f}")
    print(f"⬆️  Максимальный GPA: {stats['max_gpa']:.2f}")
    
    print("\n🏫 Распределение по группам:")
    if stats['groups']:
        for group_name, count in stats['groups'].items():
            print(f"   • {group_name}: {count} студент(ов)")
    else:
        print("   Нет данных")
    
    print("\n🏆 ТОП-5 студентов по успеваемости:")
    if stats['top_5_students']:
        for i, student in enumerate(stats['top_5_students'], 1):
            print(f"   {i}. {student['fio']} - GPA: {student['gpa']:.2f}")
    else:
        print("   Нет данных")
def export_to_json(group):
    """Экспорт данных в JSON"""
    print_header("ЭКСПОРТ ДАННЫХ")
    
    students = group.list()
    if not students:
        print("📭 Нет данных для экспорта")
        return
    
    try:
        import json
        
        data = {
            "export_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_students": len(students),
            "students": [
                {
                    "fio": s.fio,
                    "birthdate": s.birthdate,
                    "group": s.group,
                    "gpa": s.gpa
                }
                for s in students
            ]
        }
        
        export_path = "data/lab9/students_export.json"
        
        # Создаем папку если её нет
        os.makedirs(os.path.dirname(export_path), exist_ok=True)
        
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Данные экспортированы в файл:")
        print(f"   📁 {os.path.abspath(export_path)}")
        print(f"   📊 Всего записей: {len(students)}")
        
    except ImportError:
        print("❌ Не удалось импортировать модуль json")
    except Exception as e:
        print(f"❌ Ошибка при экспорте: {e}")

def main():
    """Главное меню"""
    clear_screen()
    
    print("=" * 60)
    print(" " * 15 + "БАЗА ДАННЫХ СТУДЕНТОВ")
    print(" " * 10 + "(Лабораторная работа №9)")
    print("=" * 60)
    
    try:
        group = Group("data/lab9/students.csv")
        print(f"📁 База данных: data/lab9/students.csv")
        print(f"👥 Студентов в базе: {len(group.list())}")
    except Exception as e:
        print(f"❌ Ошибка при загрузке базы: {e}")
        return
    
    while True:
        print_header("ГЛАВНОЕ МЕНЮ")
        
        print("1. 📋 Показать всех студентов")
        print("2. ➕ Добавить нового студента")
        print("3. 🔍 Найти студента")
        print("4. ✏️  Обновить данные студента")
        print("5. 🗑️  Удалить студента")
        print("6. 📊 Показать статистику")
        print("7. 💾 Экспорт в JSON")
        print("0. 🚪 Выход")
        
        choice = input("\n👉 Выберите действие (0-7): ").strip()
        
        if choice == "0":
            print("\n👋 До свидания!")
            break
        
        elif choice == "1":
            clear_screen()
            show_all_students(group)
        
        elif choice == "2":
            clear_screen()
            add_student_interactive(group)
        
        elif choice == "3":
            clear_screen()
            find_student_interactive(group)
        
        elif choice == "4":
            clear_screen()
            update_student_interactive(group)
        
        elif choice == "5":
            clear_screen()
            delete_student_interactive(group)
        
        elif choice == "6":
            clear_screen()
            show_statistics(group)
        
        elif choice == "7":
            clear_screen()
            export_to_json(group)
        
        else:
            print("\n❌ Неверный выбор!")
        
        if choice != "0":
            input("\n↵ Нажмите Enter для возврата в меню...")
            clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана")
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()