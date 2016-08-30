import random
from collections import namedtuple
from io import BytesIO
from tokenize import tokenize

frequency_table = {}
following_siblings_table = {}

poem = """By, gates of Eden, Angel, gentle,
By gates of Eden, Angel, gentle,
    Shone with his softly drooped head,
    And Demon, gloomy and resentful
    Over the hellish crevasse flapped."""


def main():
    # 1st order markov chains:
    for current, next_token, _ in trios(tokenize(BytesIO(poem.encode('utf-8')).readline)):
        _, word, _, _, _ = current
        _, next_word, _, _, _ = next_token
        word_counter = frequency_table.setdefault(word, 0)

        siblings = following_siblings_table.setdefault(word, [])
        siblings.append(next_word)

        if word_counter == 0:
            frequency_table[word] = 1
        else:
            frequency_table[word] += 1


def trios(input):
    input = iter(input)  # make sure input is an iterator

    def get_next_word():
        for i in input:
            if i.type == 1:
                return i

    try:
        prev, current = get_next_word(), get_next_word()
    except StopIteration:
        return
    for next_word in input:
        if next_word.type == 1:
            yield prev, current, next_word
            prev, current = current, next_word


if __name__ == '__main__':
    main()
    print(following_siblings_table)
    base = random.choice(list(frequency_table.keys()))

    # for i in range(10):
    #     base += " " + random.choice(frequency_table[base])
