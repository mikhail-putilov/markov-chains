import random
from io import BytesIO
from tokenize import tokenize

frequency_table = {}
following_siblings_table = {}

poem = """I am Misha. I am Sasha. I am Kostya"""


def prepare_markov_chain():
    # 1st order markov chains:
    last_word = ""
    for current, next_token in duos(tokenize(BytesIO(poem.encode('utf-8')).readline)):
        _, word, _, _, _ = current
        _, next_word, _, _, _ = next_token
        word_counter = frequency_table.setdefault(word, 0)
        last_word = next_word

        siblings = following_siblings_table.setdefault(word, set())
        siblings.add(next_word)

        if word_counter == 0:
            frequency_table[word] = 1
        else:
            frequency_table[word] += 1
    following_siblings_table.setdefault(last_word, set())


def duos(_input):
    _input = iter(_input)  # make sure input is an iterator

    def get_next_word():
        for i in _input:
            if i.type == 1:
                return i

    try:
        prev = get_next_word()
    except StopIteration:
        return
    for next_word in _input:
        if next_word.type == 1:
            yield prev, next_word
            prev = next_word


def write_poem():
    base = random.choice(tuple(following_siblings_table.keys()))
    accumulator = base
    for i in range(10):
        choice_from = tuple(following_siblings_table[base])
        if not choice_from:
            break
        choice = random.choice(choice_from)
        accumulator += " " + choice
        base = choice
    print(accumulator)


if __name__ == '__main__':
    prepare_markov_chain()
    write_poem()
