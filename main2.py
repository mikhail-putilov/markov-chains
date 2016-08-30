import random
from io import BytesIO
from tokenize import tokenize
import numpy.random as npr

frequency_table = {}
following_siblings_table = {}

poems = [
    """Forever we remain oblivious to the future,
    lost to the past and enduring our torture.
    Forever we take chances to settle our scores,
    losing some battles and winning some wars.
    Forever praying out loud hoping someone will hear,
    forever crying softly but never shedding a tear.
    Forever exists behind a disguise,
    but the belief in forever keeps our hearts alive.""",
    """I come with no wrapping or pretty pink bows.
    I am who I am from my head to my toes.
    I tend to get loud when speaking my mind.
    Even a little crazy some of the time.
    I'm not a size 5 and don't care to be.
    You can be you and I can be me.
    I try to stay strong when pain knocks me down.
    And the times that I cry is when no ones around.
    To error is human or so that's what they say.
    Well tell me who's perfect anyway.""",
    """In all chaotic beauty lies a wounded work of art.
    Beautiful but torn, wreaking havoc on my heart.
    Camouflaged by insecurities, blinded by it all.
    I love the way you sit there and barely notice me at all.""",
    """To those whom I've fought with
    and to those I don't know your name
    We fought by one another.
    You did not die in vain.
    We fought, you died,
    We bled, and I cried,
    Even until our untimely end,
    our country, our families, our brothers,
    we shall defend"""]


def prepare_markov_chain(poem):
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
    last_word_counter = frequency_table.setdefault(last_word, 0)
    if last_word_counter == 0:
        frequency_table[last_word] = 1


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


def write_line(start_word=None):
    if start_word == None:
        base = random.choice(tuple(following_siblings_table.keys()))
    else:
        base = start_word
    accumulator = base
    for i in range(5):
        choice_from = tuple(following_siblings_table[base])
        if not choice_from:
            break
        all_sum = sum([frequency_table[word] for word in choice_from])
        choice = npr.choice(choice_from, 1, p=[frequency_table[word] / all_sum for word in choice_from])
        accumulator += " " + choice[0]
        base = choice[0]
    print(accumulator)


if __name__ == '__main__':
    for poem in poems:
        prepare_markov_chain(poem)
    # print(frequency_table)
    # print(following_siblings_table)
    write_line(start_word="I")
    write_line()
    write_line()
    write_line()
