import sys
import argparse
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n


def cmd_cat(args):
    try:
        path = Path(args.input)
        with path.open(encoding="utf-8") as f:
            if args.n:
                for line_num, line in enumerate(f, start=1):
                    print(f"{line_num:6} {line}", end="")
            else:
                print(f.read(), end="")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден - {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_stats(args):
    try:
        path = Path(args.input)
        with path.open(encoding="utf-8") as f:
            text = f.read()
        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        total_words = len(tokens)
        unique_words = len(freq)
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print(f"Топ-{args.top}:")
        for word, count in top_n(freq, args.top):
            print(f"  {word}: {count}")
            
    except FileNotFoundError:
        print(f"Ошибка: файл не найден - {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом"
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    cat_parser = subparsers.add_parser(
        "cat",
        help="Вывести содержимое файла"
    )
    cat_parser.add_argument(
        "--input",
        required=True,
        help="Путь к файлу"
    )
    cat_parser.add_argument(
        "-n",
        action="store_true",
        help="Нумеровать строки"
    )
    stats_parser = subparsers.add_parser(
        "stats",
        help="Анализ частот слов"
    )
    stats_parser.add_argument(
        "--input",
        required=True,
        help="Путь к текстовому файлу"
    )
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Количество топовых слов (по умолчанию: 5)"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == "cat":
        cmd_cat(args)
    elif args.command == "stats":
        cmd_stats(args)


if __name__ == "__main__":
    main()

