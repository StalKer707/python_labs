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

