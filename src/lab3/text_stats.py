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

