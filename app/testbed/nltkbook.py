__author__ = 'denialanderror'

import re
import nltk

text = 'Once upon a time there lived a boy called Marbles. He lived in the forest with his mother and father. \
One day, Marbles was playing in the forest and lost his head. Marbles was very sad so decided to go and look for it. \
Marbles went to the beach, where he saw a dragon playing. "Have you seen my head?", said Marbles. "No", said the dragon. \
Marbles went to the big hill. He climbed up the hill and he climbed down the hill, but he could not find his head anywhere. \
Marbles went to the castle and saw the angry robot. The robot had his head! Marbles fought the robot and won. \
Marbles was very happy to have his head back and went back home to the forest where he lived happily ever after.'

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

print(tagged)

