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
    
    # Данные для теста JSON -> CSV
    test_json_data = [
        {"id": 1, "name": "Анна", "department": "HR", "email": "anna@company.com"},
        {"id": 2, "name": "Борис", "department": "IT", "skill": "Python"},
        {"id": 3, "name": "Виктория", "department": "Finance"}
    ]
    json_file = Path("source_data.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(test_json_data, f, ensure_ascii=False, indent=2)
    print(f"   ✅ Файл '{json_file.name}' создан.")

    # Данные для тестов CSV -> JSON и CSV -> XLSX
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
        # Используем тот же исходный CSV
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