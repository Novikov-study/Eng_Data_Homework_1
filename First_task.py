import re
from collections import Counter

def read_file():
    with open("./data/first_task.txt", encoding="utf-8") as file:
        return file.readlines()

def text_to_words(lines):
    words = []
    for line in lines:
        _line = re.sub(r"[\'?!.,-]", "", line.lower().strip())
        words.extend(_line.split())
    return words

def calc_freq(words):
    return Counter(words).most_common()

def count_consonants(words):
    consonants = set("bcdfghjklmnpqrstvwxyz")
    total_consonants = 0
    total_letters = 0

    for word in words:
        for char in word:
            if char.isalpha():  # Учитываем только буквы
                total_letters += 1
                if char in consonants:
                    total_consonants += 1

    consonant_ratio = total_consonants / total_letters if total_letters > 0 else 0
    return total_consonants, consonant_ratio

def write_word_freq(stat):
    with open("first_task_result.txt", "w", encoding="utf-8") as file:
        for key, val in stat:
            file.write(f"{key}:{val}\n")

def write_consonant_stats(total_consonants, consonant_ratio):
    with open("first_task_result_variable.txt", "w", encoding="utf-8") as file:
        file.write(f"Всего согласных: {total_consonants}\n")
        file.write(f"Доля согласных: {consonant_ratio:.2%}\n")

lines = read_file()
words = text_to_words(lines)
word_freq = calc_freq(words)
total_consonants, consonant_ratio = count_consonants(words)

write_word_freq(word_freq)
write_consonant_stats(total_consonants, consonant_ratio)

