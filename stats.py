def count_words(text: str) -> int:
    if not text:
        raise ValueError("Input text cannot be empty.")
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    letter_dict = {}
    if not text:
        raise ValueError("Input text cannot be empty.")
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict

def sort_dict(char_count: dict) -> dict:
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict