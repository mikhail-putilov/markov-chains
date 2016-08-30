import random
from io import BytesIO
from tokenize import tokenize

table = {}
poem = """By gates of Eden, Angel, gentle,
    Shone with his softly drooped head,
    And Demon, gloomy and resentful
    Over the hellish crevasse flapped."""


def main():
    # 1st order:
    for type, word, _, _, _ in tokenize(BytesIO(poem.encode('utf-8')).readline):
        if type == 1:
            word_counter = table.setdefault(word, 1)
            if word_counter == 1:
                continue
            else:
                table[word] += 1


if __name__ == '__main__':
    main()
    print(table)
