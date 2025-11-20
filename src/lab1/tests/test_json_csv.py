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
