import csv
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from src.lab8.models import Student


class Group:
    """Класс для управления базой данных студентов в CSV-файле"""
    
    def __init__(self, storage_path: str):  
        """
        Инициализация группы студентов

        Args:
            storage_path: путь к CSV-файлу
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()  # Вызываем метод без лишнего подчеркивания

    def _ensure_storage_exists(self):  # Один underscore, а не два
        """Создает файл с заголовком, если его нет"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()

    def read_all(self) -> List[dict[str, str]]:  # Правильные аннотации типов
        """Читает записи из CSV-файла"""
        rows = []
        try:
            with open(self.path, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row:
                        rows.append(row)
        except FileNotFoundError:
            pass
        return rows

    def _write_all(self, rows: List[dict[str, str]]):  # _write_all, а не _writer_all
        """Записывает все записи в CSV-файл"""
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)

    def _validate_student_data(self, student_data: dict):
        """Валидация данных студента"""
        required_fields = ["fio", "birthdate", "group", "gpa"]
        
        # Проверка наличия обязательных полей
        for field in required_fields:
            if field not in student_data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
        
        # Проверка формата даты
        try:
            datetime.strptime(student_data["birthdate"], "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {student_data['birthdate']}. Ожидается YYYY-MM-DD")
        
        # Проверка GPA
        try:
            gpa = float(student_data["gpa"])
            if not (0.0 <= gpa <= 5.0):
                raise ValueError(f"GPA должен быть в диапазоне от 0.0 до 5.0, получено: {gpa}")
        except ValueError:
            raise ValueError(f"Некорректное значение GPA: {student_data['gpa']}")

    # Добавим остальные методы для CRUD операций
    def list(self) -> List[Student]:
        """Возвращает список всех студентов"""
        rows = self.read_all()
        students = []
        for row in rows:
            try:
                self._validate_student_data(row)
                student = Student(
                    fio=row["fio"],
                    birthdate=row["birthdate"],
                    group=row["group"],
                    gpa=float(row["gpa"])
                )
                students.append(student)
            except ValueError as e:
                print(f"Пропущена некорректная запись: {row}. Ошибка: {e}")
        return students

    def add(self, student: Student):
        """Добавляет нового студента в CSV"""
        student_dict = {
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        }
        
        self._validate_student_data(student_dict)
        
        rows = self.read_all()
        
        # Проверка на дубликат
        for row in rows:
            if row["fio"] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        rows.append(student_dict)
        self._write_all(rows)
        print(f"✅ Студент '{student.fio}' успешно добавлен")






def find(self, substr: str) -> List[Student]:
        """Поиск студентов по подстроке в ФИО"""
        students = self.list()
        return [s for s in students if substr.lower() in s.fio.lower()]

def remove(self, fio: str) -> bool:
        """Удаляет студента по ФИО"""
        rows = self.read_all()
        initial_count = len(rows)
        
        rows = [r for r in rows if r["fio"] != fio]
        
        if len(rows) < initial_count:
            self._write_all(rows)
            return True
        return False

def update(self, fio: str, **fields):
        """Обновляет поля существующего студента"""
        rows = self.read_all()
        updated = False
        
        for i, row in enumerate(rows):
            if row["fio"] == fio:
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        row[key] = value
                    else:
                        raise ValueError(f"Недопустимое поле для обновления: {key}")
                
                self._validate_student_data(row)
                rows[i] = row
                updated = True
                break
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(rows)
        print(f"✅ Студент '{fio}' успешно обновлен")

def stats(self) -> dict:
        """Расширенная аналитика по группе"""
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [s.gpa for s in students]
        groups_count = {}
        
        for student in students:
            group = student.group
            groups_count[group] = groups_count.get(group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": round(sum(gpas) / len(gpas), 2),
            "groups": groups_count,
            "top_5_students": top_5
        }