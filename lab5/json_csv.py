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
