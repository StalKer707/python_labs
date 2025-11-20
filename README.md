# Лабораторна работа №1

Задача 1
```py
name = input()
age = int(input())
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```
![Привет и возраст](/images1/lab01/img_1.png)

Задача 2
```py
import math
a1 = input()
a2 = input()
a1 = a1.replace(',', '.')
a2 = a2.replace(',', '.')
a1 = float(a1)
a2 = float(a2)
sum = a1 + a2
avg = sum / 2
print(f'sum={sum}; avg={round(avg, 2)}')
```
![Сумма и среднее](/images1/lab01/img_2.png)

Задача 3
```py
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки: {base:.2f}')
print(f'НДС:               {vat_amount:.2f}')
print(f'Итого к оплате:    {total:.2f}')
```
![Чек: скидка и НДС](/images1/lab01/img_3.png)

Задача 4
```py
m = int(input())
ch = m // 60
print(f'{ch}:{m - ch * 60}')
```
![Минуты -> ЧЧ:ММ](/images1/lab01/img_4.png)

Задача 5
```py
fio = input().split()
print(f'Инициалы: {fio[0][0] + fio[1][0] + fio[2][0]}.')
print(f'Длина (символов): {len(fio[0]) + len(fio[1]) + len(fio[2]) + 2}')
```
![Инициалы и длина строки](/images1/lab01/img_5.png)

Задача 6
```py
n = int(input().strip())
t = 0
f = 0
for x in range(n):
    line = input().strip()
    a = line.split()
    b = a[-1]
    if b == 'True':
        t += 1
    elif b == 'False':
        f += 1
print(t, f)
```
![Задание со звёздочкой](/images1/lab01/img_6.png)

Задача 7
```py
a = input().strip()
alf = 'QWERTYUIOPASDFGHJKLZXCVBNM'
ch = '0123456789'
bukv = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
start = 0
for i in range(len(a)):
    st = a[i]
    if st in alf:
        start = i
        break
second = 0
for i in range(len(a)):
    st = a[i]
    if st in ch and a[i + 1] in bukv:
        second = i + 1
        break
step = second - start
ans = []
i = start
while i < len(a):
    ans.append(a[i])
    if a[i] == '.':
        break
    i += step
print(''.join(ans))
```
![Задание со звёздочкой](/images1/lab01/img_7.png)


# Лабораторна работа №2

Задание 1 
```py
nums = []
def min_max(nums):
    nums_tup = []
    if len(nums) > 0:
        mini = nums_tup.append(min(nums))
        maxi = nums_tup.append(max(nums))
        print (tuple(nums_tup))
    else:
        raise ValueError
min_max(nums)
```
![Пункт 1](/images1/lab02/img_1.png) 
![Пункт 2](/images1/lab02/img_1.2png)
![Пункт 3](/images1/lab02/img_1.3png)  


Задание 2
```py
nums = [1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums):
    new_nums = sorted(set(nums))
    print(new_nums)
unique_sorted(nums)
```
![.](/images1/lab02/img_2.png) 
![.](/images1/lab02/img_2.1.png) 
![.](/images1/lab02/img_2.2.png) 

Задание 3
```py
mat = [[1,2], "xx"]
def flatten(mat):
    new_mat = []
    for num in mat :
        if type(num) == tuple or type(num) == list:
            for i in range(len(num)):
                if num [i] != '':
                    new_mat.append(num[i])
        else:
            raise ValueError
    print(new_mat)
flatten(mat)
```   
![.](/images1/lab02/img_3.png) 
![.](/images1/lab02/img_3.1.png) 
![.](/images1/lab02/img_3.2.png) 

Матрица 1
```py
mat = [ [1,2], [3,4]]
def check_rvanost(mat):
    dlina = len(mat[-1])
    for x in mat:
        if len(x) != dlina:
            raise ValueError
        else:
            return True
def transpose(mat):
    if check_rvanost:
        new_mat = []
        for stolbik in range (len(mat[-1])):
            new_row = []
            for row in range(len(mat)):
                new_row.append(mat[row][stolbik])
            new_mat.append(new_row)
    print(new_mat)
transpose(mat)           
``` 
![.](/images1/lab02/matrica_1.png) 

Матрица 2 
```py
mat=[[1,2],[3,4]]
def check_rvanost(mat):
    for i in range(len(mat)):
        if len (mat[i]) == len(mat[i+1]):
            return True
        else:
            return False
def row_sums(mat):
    new_mat = []
    for x in mat:
        if type(x) == list and check_rvanost(mat):
            summa = 0
            for i in range(len(x)):
                summa += x[i]
            new_mat.append(summa)
        else:
            raise ValueError
    print(new_mat)
row_sums(mat)    
```
![.](/images1/lab02/matrica_2.png) 

Матрица 3
```py
def kol_sums(matrica):
    results = []
    max_lenght_row = max([len(row)for row in matrica])
    try:
        for i in range(max_lenght_row):
            count = 0
            for row in matrica:
                count += row[i]
            results.append(count)
    except:
        raise ValueError
    return results
matrica = [[1,2,3],[4,5,6]]
print(kol_sums(matrica))
```
![.](/images1/lab02/matrica_3.png) 

РЕЙХ
```py
roan = ("адольф гитлер верховный","ABB-07", 3.999)
def fio(roan):
    if len (roan[0])> 0 :
        fio = roan[0].split()
        iniliats = ''.join(i [0]for i in fio).upper()
        if len (iniliats) == 3 :
            return fio[0][0].upper() + fio [0][1:] + " " + iniliats [1]  +  " " + iniliats[2] + " "
        elif len (iniliats) == 2:
            return fio[0][0].upper() + fio [0][1:] + " " + iniliats [1]  +  " "
        else:
             return fio[0][0].upper() + fio [0][1:]
    else:
        raise ValueError
def gpa(roan):
    if len(str(roan[2])) > 0 :
        return round (roan[2], 2)
    else:
        raise ValueError

def format_record(roan):
    if tuple(roan) == roan:
        if len (str(roan[1]))> 0:
            res = fio(roan) + "," + " " + " mr" + roan [1] + "," + " " + "NBA" + " " + str(gpa(roan))
            print(roan) 
            print(res)   
        else:
            raise ValueError
format_record(roan)
```
![.](/images1/lab02/tuples_ru.png)


# Лабораторная работа №3

Задание 1 
```py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n


def main():
    text = sys.stdin.read()
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```
![.](/images1/lab01/img_3laba.png)





# Лабораторная работа №4
Задание 1 
```py
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> Dict[str, int]:
    tokens = tokenize(normalize(text))
    return count_freq(tokens)


def sorted_word_counts(freq: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main():
    parser = argparse.ArgumentParser(
        description="Генерация CSV-отчёта по частотам слов"
    )
    parser.add_argument(
        "--input", "--in",
        dest="input_file",
        default="data/lab04/input.txt",
        help="Входной текстовый файл (по умолчанию: data/lab04/input.txt)"
    )
    parser.add_argument(
        "--output", "--out",
        dest="output_file",
        default="data/lab04/report.csv",
        help="Выходной CSV файл (по умолчанию: data/lab04/report.csv)"
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка входного файла (по умолчанию: utf-8)"
    )
    
    args = parser.parse_args()
    
    try:
        text = read_text(args.input_file, encoding=args.encoding)
        freq = frequencies_from_text(text)
        tokens = tokenize(normalize(text))
        total_words = len(tokens)
        unique_words = len(freq)
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_n(freq, 5):
            print(f"{word}:{count}")
        sorted_freq = sorted_word_counts(freq)
        write_csv(sorted_freq, args.output_file, header=("word", "count"))
        print(f"\nОтчёт сохранён в: {args.output_file}")
        
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}", file=sys.stderr)
        print("Попробуйте указать другую кодировку с помощью --encoding", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
![.](/images1/lab01/img_lab4.png)


# Лабораторная работа №5
Задание 1 
```py
import csv
from pathlib import Path
from typing import Union

try:
    from openpyxl import Workbook
    from openpyxl.utils import get_column_letter
except ImportError:
    raise ImportError(
        
    )


def csv_to_xlsx(csv_path: Union[str, Path], xlsx_path: Union[str, Path]) -> None:
    csv_p = Path(csv_path)
    xlsx_p = Path(xlsx_path)
    if not csv_p.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    row_count = 0
    max_widths = {}
    with csv_p.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, start=1):
            if not row:
                continue
            ws.append(row)
            row_count += 1
            for col_idx, cell_value in enumerate(row, start=1):
                current_width = len(str(cell_value))
                if col_idx not in max_widths:
                    max_widths[col_idx] = 0
                max_widths[col_idx] = max(max_widths[col_idx], current_width)
    if row_count == 0:
        raise ValueError("Пустой CSV файл")
    for col_idx, width in max_widths.items():
        column_letter = get_column_letter(col_idx)
        adjusted_width = max(width + 2, 8)
        ws.column_dimensions[column_letter].width = adjusted_width
    xlsx_p.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_p)
    print(f"Успешно: Файл Excel сoхранен")
```
Задание 2
```py
import json
import csv
from pathlib import Path
from typing import Union, List, Dict, Any


def json_to_csv(json_path: Union[str, Path], csv_path: Union[str, Path]) -> None:
    json_p = Path(json_path)
    csv_p = Path(csv_path)
    if not json_p.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    with json_p.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список словарей")
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = sorted(all_keys)
    csv_p.parent.mkdir(parents=True, exist_ok=True)
    with csv_p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)
print(f'Успешно: Файл CSV сохранен')


def csv_to_json(csv_path: Union[str, Path], json_path: Union[str, Path]) -> None:
    csv_p = Path(csv_path)
    json_p = Path(json_path)
    if not csv_p.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    with csv_p.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    if not data:
        raise ValueError("Пустой CSV или отсутствует заголовок")
    json_p.parent.mkdir(parents=True, exist_ok=True)
    with json_p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Успешно: Файл JSON сoхранен")
```
Задание 3
```py 
    import json
import csv
from pathlib import Path
import sys

try:
    from lab5.json_csv import json_to_csv, csv_to_json
    from lab5.csv_xlsx import csv_to_xlsx
except ImportError:
    print(f"❌ Ошибка: Не удалось импортировать модули из 'lab5'.")
    print("Убедитесь, что 'main.py' находится в одной папке с 'lab5',")
    print("и что в 'lab5' есть файл 'init.py'.")
    sys.exit(1)


def setup_test_files():
    """
    
    """
    print("--- 🛠️ Создаю тестовые файлы... ---")
    

    test_json_data = [
        {"id": 1, "name": "Анна", "department": "HR", "email": "anna@company.com"},
        {"id": 2, "name": "Борис", "department": "IT", "skill": "Python"},
        {"id": 3, "name": "Виктория", "department": "Finance"}
    ]
    json_file = Path("source_data.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(test_json_data, f, ensure_ascii=False, indent=2)
    print(f"   ✅ Файл '{json_file.name}' создан.")

    
    test_csv_data = [
        ["Product", "Price", "Category", "StockCount"],
        ["Ноутбук 'Ultra'", "120000", "Электроника", "15"],
        ["Кофе (зерно)", "1500", "Продукты", "150"],
        ["Книга 'Изучаем Python'", "3000", "Книги", "45"]
    ]
    csv_file = Path("source_data.csv")
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(test_csv_data)
    print(f"   ✅ Файл '{csv_file.name}' создан.")
    print("----------------------------------\n")


def main():
    """
    
    """
    try:
        # 0. Создаем исходные файлы
        setup_test_files()

        # --- Тест 1: JSON -> CSV ---
        print("--- 🧪 Тест 1: Запуск json_to_csv ---")
        json_in = "source_data.json"
        csv_out = "output_from_json.csv"
        json_to_csv(json_in, csv_out)
        


        # --- Тест 2: CSV -> JSON ---
        print("\n--- 🧪 Тест 2: Запуск csv_to_json ---")
        csv_in = "source_data.csv"
        json_out = "output_from_csv.json"
        csv_to_json(csv_in, json_out)



        # --- Тест 3: CSV -> XLSX ---
        print("\n--- 🧪 Тест 3: Запуск csv_to_xlsx ---")
        xlsx_out = "output_from_csv.xlsx"
        csv_to_xlsx(csv_in, xlsx_out)
    

        print("\n" + "="*40)
        print("🎉🎉🎉 ВСЕ ТЕСТЫ УСПЕШНО ЗАВЕРШЕНЫ! 🎉🎉🎉")
        print("Проверьте созданные файлы в папке:")
        print(f"- {csv_out}")
        print(f"- {json_out}")
        print(f"- {xlsx_out}")
        print("="*40)

    except FileNotFoundError as e:
        print(f"❌ ОШИБКА: Файл не найден. {e}")
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка: {e}")

if __name__ == '__main__':
    main()
```
![.](/images1/lab01/img_lab5.png)
![.](/images1/lab01/img_lab5.2.png)


# Лабораторная работа №6
Задание 1 
```py


import sys
import argparse
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.parent))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def cmd_json2csv(args):
    try:
        json_to_csv(args.input, args.output)
        print(f"✓ JSON → CSV: {args.input} → {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_csv2json(args):
    try:
        csv_to_json(args.input, args.output)
        print(f"✓ CSV → JSON: {args.input} → {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_csv2xlsx(args):
    try:
        csv_to_xlsx(args.input, args.output)
        print(f"✓ CSV → XLSX: {args.input} → {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ImportError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилита для конвертации форматов данных"
    )
    subparsers = parser.add_subparsers(dest="cmd", help="Доступные конвертеры")
    p1 = subparsers.add_parser(
        "json2csv",
        help="Конвертировать JSON в CSV"
    )
    p1.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному JSON файлу"
    )
    p1.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному CSV файлу"
    )
    p2 = subparsers.add_parser(
        "csv2json",
        help="Конвертировать CSV в JSON"
    )
    p2.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному CSV файлу"
    )
    p2.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному JSON файлу"
    )
    p3 = subparsers.add_parser(
        "csv2xlsx",
        help="Конвертировать CSV в XLSX"
    )
    p3.add_argument(
        "--in",
        dest="input",
        required=True,
        help="Путь к входному CSV файлу"
    )
    p3.add_argument(
        "--out",
        dest="output",
        required=True,
        help="Путь к выходному XLSX файлу"
    )
    
    args = parser.parse_args()
    
    if not args.cmd:
        parser.print_help()
        sys.exit(1)
    
    if args.cmd == "json2csv":
        cmd_json2csv(args)
    elif args.cmd == "csv2json":
        cmd_csv2json(args)
    elif args.cmd == "csv2xlsx":
        cmd_csv2xlsx(args)


if __name__ == "__main__":
    main()
```
![.](/images1/lab02/img_6.png)





# Лабораторная работа №7
Задание 1 
```py
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    assert normalize("САП МИР") == "сап мир"
    assert normalize("Бладс Бладс") == "бладс бладс"
    print("normalize с базовыми все четко")


def test_normalize_edge_cases():
    assert normalize("") == ""
    assert normalize("  ") == ""
    assert normalize("     Много пробелов       ") == "много пробелов"
    print("normalize с граничными уцы все в порядке")


def test_tokenize_basic():
    result = tokenize("сап ма бой как район")
    assert result == ["сап", "ма", "бой", "как", "район"]

    result2 = tokenize("ты,он и она!")
    assert "ты" in result2 and "она" in result2
    print("tokenize базовые работают")


def test_count_freq_basic():
    tokens = ["черный", "белый", "черный", "белый", "серый"]
    result = count_freq(tokens)
    expected = {"черный": 2, "белый": 2, "серый": 1}
    assert result == expected
    print("count_freq базовые прошли как надо")


def test_top_n_basic():
    freq_dict = {"Мерс": 3, "БМВ": 3, "Audi": 3}
    result = top_n(freq_dict, 2)
    assert result == [("Audi", 3), ("БМВ", 3)]
    print("top_n сортировка при равной частоте прошла на ура")


def test_top_n_tie_breaker():
    freq_dict = {"пингвин": 3, "медведь": 3, "волк": 3}
    result = top_n(freq_dict, 2)
    assert result == [("волк", 3), ("медведь", 3)]
    print("top_n сортировка при равной частоте прошла")
```
![.](/images1/lab02/img_7.png)
![.](/images1/lab02/img_7.1.png)
![.](/images1/lab02/img_7.2.png)



Задание 2
```py
import pytest
import sys
import os
import json
import csv
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    """Тестируем конвертацию JSON → CSV"""
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "test.csv"

    test_data = [
        {"name": "Иван", "age": 25, "city": "Москва"},
        {"name": "Мария", "age": 30, "city": "СПб"},
    ]

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)

    json_to_csv(str(json_file), str(csv_file))

    assert csv_file.exists()

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows)
    assert rows[0]["name"] == "Иван"
    assert rows[1]["city"] == "СПб"
    print(" json_to_csv базовый тест прошёл")


def test_csv_to_json_basic(tmp_path):
    """Тестируем конвертацию CSV → JSON"""
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "test.json"

    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerow({"name": "Петр", "age": 35, "city": "Казань"})
        writer.writerow({"name": "Ольга", "age": 28, "city": "Екатеринбург"})

    csv_to_json(str(csv_file), str(json_file))

    assert json_file.exists()

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Петр"
    assert data[1]["city"] == "Екатеринбург"
    print(" csv_to_json базовый тест прошёл")


def test_json_to_csv_file_not_found():
    """Тестируем обработку ошибки когда файл не найден"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")
    print(" json_to_csv обработка ошибок прошла")
```
![.](/images1/lab02/img_7.3.png)
![.](/images1/lab02/img_7.4.png)