import numpy as np
import random


def load_text():
    try:
        with open('text', 'r', encoding='utf-8') as f:
            return f.read().lower()
    except FileNotFoundError:
        print("Файл 'text' не найден в текущей директории!")


def create_character_mappings(text):
    chars = sorted(set(text))
    char_to_idx = {c: i for i, c in enumerate(chars)}
    idx_to_char = {i: c for i, c in enumerate(chars)}
    return chars, char_to_idx, idx_to_char


def simple_text_generator(text, seed_length=20, output_length=500):
    ngram_length = 3
    ngrams = {}

    for i in range(len(text) - ngram_length):
        ngram = text[i:i + ngram_length]
        next_char = text[i + ngram_length]

        if ngram not in ngrams:
            ngrams[ngram] = []
        ngrams[ngram].append(next_char)

    start_idx = random.randint(0, len(text) - ngram_length - 1)
    current_ngram = text[start_idx:start_idx + ngram_length]
    generated = current_ngram

    print(f"Начальный n-грамм: {current_ngram}")

    for _ in range(output_length):
        if current_ngram in ngrams:
            next_char = random.choice(ngrams[current_ngram])
            generated += next_char
            current_ngram = generated[-ngram_length:]
        else:
            start_idx = random.randint(0, len(text) - ngram_length - 1)
            current_ngram = text[start_idx:start_idx + ngram_length]

    return generated

def main():
    print("Лабораторная работа 3: Генерация текста")
    print("=" * 50)

    text = load_text()
    print(f"Загружен текст из файла 'text'")
    print(f"Длина текста: {len(text)} символов")
    print(f"Уникальных символов: {len(set(text))}")
    print(f"\nПример текста (первые 300 символов):")
    print(text[:300], "...")

    print("\n" + "=" * 50)
    print("ГЕНЕРАЦИЯ ТЕКСТА (упрощенный алгоритм на n-граммах)")
    print("=" * 50)

    generated_text = simple_text_generator(text, output_length=1000)

    print("\nСгенерированный текст:")
    print("-" * 50)
    print(generated_text)
    print("-" * 50)

    with open("generated_text.txt", "w", encoding="utf-8") as f:
        f.write(generated_text)
    print(f"\nТекст сохранен в файл 'generated_text.txt'")

    print("\n" + "=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТА")
    print("=" * 50)

    original_chars = set(text)
    generated_chars = set(generated_text)

    print(f"Уникальные символы в оригинале: {len(original_chars)}")
    print(f"Уникальные символы в сгенерированном: {len(generated_chars)}")
    print(f"Общие символы: {len(original_chars & generated_chars)}")

    def get_top_chars(txt, n=10):
        from collections import Counter
        return Counter(txt).most_common(n)

    print("\nТоп-10 символов в оригинале:")
    for char, count in get_top_chars(text, 10):
        print(f"  '{char}': {count}")

    print("\nТоп-10 символов в сгенерированном тексте:")
    for char, count in get_top_chars(generated_text, 10):
        print(f"  '{char}': {count}")


if __name__ == "__main__":
    main()