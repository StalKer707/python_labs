from dataclasses import dataclass 
from datetime import datetime, date
import re

@dataclass
class Student:
    fio: str
    birthdate: str
    group : str
    gpa : float 

    def __post_init__(self):
    
        try:
            datetime.strptime(self.birthdate,"%Y-%m-%d")
        except ValueError:
            raise ValueError ("Чувак дата в формате YYYY-MM-DD")

        if not (0 <= self.gpa <= 5):    
            raise ValueError("GPA должен быть в диапозоне от 0 до 5")
        


    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - birth_date.year

        if today.month < birth_date.month or(today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
    def to_dict(self) -> dict:
        return{
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    @classmethod
    
    def from_dict(cls, d: dict):
        return cls(
            fio = d["fio"],
            birthdate = d ["birthdate"],
            group = d ["group"],
            gpa = d["gpa"]
            )
    
    def __str__(self):
        return f"{self.fio}, {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"
    