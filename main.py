import os
from typing import Dict


def get_book_text(rel_path: str):
    abs_path = os.getcwd() + rel_path
    with open(abs_path, 'r') as f:
        return f.read()


def get_word_count(text: str):
    return len(text.split())


def get_letter_frequency(text: str):
    letter_frequency: Dict[str, int] = dict()

    for char in text:
        c = char.lower()

        if not c.isalpha():
            continue

        if c not in letter_frequency:
            letter_frequency[c] = 0
        letter_frequency[c] += 1

    return letter_frequency


def print_report(file: str, word_count: int, letter_frequency: Dict[str, int]):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    print()

    letters = sorted(letter_frequency, key=letter_frequency.get, reverse=True)

    for letter in letters:
        print(f"The '{letter}' character was found {letter_frequency[letter]} times")

    print(f"--- End report ---")


def main():
    book_path = "/books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    letter_frequency = get_letter_frequency(book_text)
    print_report(book_path, word_count, letter_frequency)


main()
