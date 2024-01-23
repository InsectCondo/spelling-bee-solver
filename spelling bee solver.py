from os.path import dirname

DIR = dirname(__file__)


def solve_spellingbee(center: str, outer: str, english_dictionary: list[str]) -> set[str]:
    all_letters = set((outer + center).lower())
    valid_words = {
        word
        for word in english_dictionary
        if center in word and set(word).issubset(all_letters)
    }
    return valid_words


if __name__ == "__main__":
    center = "t"
    outer = "choipk"
    with open(f'{DIR}/spellingbee_dict.txt', 'r') as file:
        english_dictionary = file.read().split('\n')
    valid_words = solve_spellingbee(center, outer, english_dictionary)
    print(valid_words)
