import csv
import sys
import os
from pathlib import Path
from typing import List, Optional
from datetime import datetime


sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..'))
from lab8.models import Student

class Group:
    """Класс для управления базой данных студентов в CSV - файле """
    def __init__(self,storage_path:str):
        """
        Иницилизация группы  студентов


        Args:
            storage_path: путь к CSV-файлу
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists_()


    def _ensure_storage_exists_(self): 
        """крафтит файл с названием если нет """
        if not self.path.exists():
            self.path.parent.mkdir(parents=True,exist_ok=True)
            with open(self.path,"w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["fio","birthdate","group", "gpa"])
                writer.writeheader()


    def read_all(self)-> list[dict]:
        """читает записи из CSV-файла"""
        rows = []
        try:
            with open(self.path,"r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row :
                        rows.append(row)
        except FileNotFoundError:
            pass
        return rows
    

    def _write_all(self, rows: List[dict[str,str]]):
        """Записывает все записи в CSV-файл"""
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["fio","birthdate","group","gpa"])
            writer.writeheader()
            writer.writerows(rows)

    def _validate_student_data(self,student_data: dict):
        """Валидация новых студентов"""
        required_fields = ["fio","birthdate","group","gpa"]        
        
        for field  in  required_fields:
            if field not in student_data:
                raise ValueError(f"отсутствует обязательный файл: {field}")

        try:
            datetime.strptime(student_data["birthdate"],"%Y-%m-%d")

        except ValueError:
            raise ValueError(f"Чувак тут рил не тот формат даты: {student_data['birthdate']}. we need YYYY-MM-DD ma boy")
        

        try:
            gpa = float(student_data["gpa"])
            if not (0.0 <= gpa <= 5.0):
                raise ValueError(f"GPA должен быть в диапозоне от 0.0 до 5.0,получено : {gpa}")
        except ValueError:
            raise ValueError(f"Неправильное значение GPA: {student_data['gpa']}")
    

    def list(self) -> List[Student]:
        """Возвращаем список студентов"""
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
                print(f"пропущена неккорректная запись:{row}.ошибка:{e}")
        return students
    def add(self,student:Student):
        """Добавляет нового студента  в CSV"""
        student_dict  = {
            "fio": student.fio,
            "birthdate" : student.birthdate,
            "group" : student.group,
            "gpa" : str(student.gpa)

        }

        self._validate_student_data(student_dict)
        rows = self.read_all()


        for row in rows:
            if row ["fio"] == student.fio:
                raise ValueError(f"студент с ФИО '{student.fio}'уже существует")
        
        rows.append(student_dict)
        self ._write_all(rows)
        print(f"Студент '{student.fio}'успешно добавлен")  


    def find(self,substr: str ) -> List [Student]:
        """Поиск студентов по подстроке в ФИО"""
        students = self.list()
        return[s for s in students if substr.lower() in s.fio.lower()]


    def remove(self, fio: str) -> bool:
        """Удаляет студента по ФИО"""
        rows = self.read_all()
        initial_count = len(rows)
        
        rows = [r for r in rows if r["fio"] !=fio]

        if len(rows) < initial_count:
            self._write_all(rows)
            return True
        return False
    def update(self,fio: str, **fields):
        """Обновляет поле нового студента """
        rows = self.read_all
        updated = False

        
        for i, row in enumerate(rows):
            if row ["fio"] == fio:
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        row[key] = value
                    else:
                        raise ValueError(f"Недопустимо поле для обновления : {key}")
                
                
                self._validate_student_data(row)    
                rows[i] = row
                updated = True
                break

        if not updated:

            raise ValueError(f"Студент с ФИО '{fio}'не найден") 
        self.writer_all(rows)
        print(f"Студент '{fio} успешно обновлен")


    def stats(self) -> dict:
        """Расширенная аналитика по группе"""
        students = self.list()
        
        if not students:
            return{
                "count": 0, 
                "min_gpa" : None,
                "max_gpa" : None,
                "avg_gpa" : None,
                "groups"  : {},
                "top_5_students" : []
            }
        gpas = [s.gpa for s in students]
        groups_count  = {}

        for student in students:
            group = student.group
            groups_count[group] = groups_count.get(group,0) + 1


        sorted_students = sorted(students, key = lambda s:s.gpa, reverse = True )
        top_5 = [ 
            {"fio": s.fio, "gpa" : s.gpa}
            for s in sorted_students[:5]
                ]
        return{
            "count" : len (students),
            "min_gpa" : min (gpas), 
            "max_gpa" : max (gpas),
            "avg_gpa" : round (sum(gpas) /  len (gpas),2),
            "groups" : groups_count, 
            "top_5_students" : top_5

        }

if __name__ == "__main__":
    print("===LETS DO IT===")
    
    
    csv_path = "data/students.csv"
    print(f"1. Чекаем файл : {csv_path}")

    group = Group(csv_path)

    import os

    if os.path.exists(csv_path):
        print(f"2. Файл создан/либо есть")
        print(f"Размер : {os.path.getsize(csv_path)} байт")
    else:
        print("2. Все херово фвйл не создан")
    
    
    print(f"3. Студентов в базе: {len(group.list())}")


    print("4.Добавляем теcтового студента...")
    test_student = Student(
        fio="Бузарова Ирена Казбекова" ,
        birthdate="2007-06-27" ,
        group = "TEST-17",
        gpa= 5.0
        
        )
    try:
        group.add(test_student)
        print(f"Добавлен : {test_student.fio}")
    
    except Exception as e:
        print(f"Ошибка: {e}")

    print(f"5. Теперь студентов в базе : {len(group.list())}")

    print("\n6. Содержимое файла:")
    print("-" * 40)
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(content if content else "(пусто)")
    except:
        print ("Не удалось прочитать фвйл")
    print("-" * 40)

    print("\n===БЛЯТЬ КАК ЖЕ ДОЛГО Я ЭТО ДЕЛАЛ ЧЕКАЙ ВСЕ ЗАЕБИСЬ===")