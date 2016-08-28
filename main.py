#!/usr/bin/env python3

from pymarkovchain import MarkovChain
# Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
# store and load its database files to. You probably want to give it another location, like so:
mc = MarkovChain()
# To generate the markov chain's language model, in case it's not present
mc.generateDatabase("""Angel

By gates of Eden, Angel, gentle,
Shone with his softly drooped head,
And Demon, gloomy and resentful
Over the hellish crevasse flapped.

The spirit of qualm and negation
Looked at another one – of good,
And fire of the forced elation
First time he vaguely understood.

“I’ve seen you,” he enunciated, -
“And not in vain you’ve sent me light:
Not all in heaven I have hated,
Not all in world I have despised.”""")
# To let the markov chain generate some text, execute
print(mc.generateString())
print(mc.generateString())
print(mc.generateString())
print(mc.generateString())

# result:
# Shone with his softly drooped head,
# First time he vaguely understood
# The spirit of qualm and negation
# And fire of the forced elation