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

