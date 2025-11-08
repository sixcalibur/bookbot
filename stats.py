def get_num_words(text: str):
    words = len(text.split())
    return words


def get_num_letters(text: str) -> dict[str, int]:
    newtext = text.lower()
    countdic: dict[str, int] = {}
    for char in newtext:
        if char in countdic:
            countdic[char] += 1
        else:
            countdic[char] = 1
    return countdic


def sort_on(item):
    return item["num"]


def sort_dict(countdic):
    sorted = [{"char": ch, "num": cnt} for ch, cnt in countdic.items() if ch.isalpha()]

    sorted.sort(key=sort_on, reverse=True)
    return sorted
