import random
from story.creature import Creature

_location = ["house", "hut", "castle", "tower", "lighthouse", "garden", "wood", "forest", "field", "town", "river",
             "stream", "beach", "dunes", "seashore", "cave", "farm", "hill"]

_size = {"big": ["big", "giant", "enormous", "gigantic", "huge", "massive", "great", "large", "tremendous"],
         "average": ["average", "normal", "plain"],
         "small": ["small", "tiny", "little", "petite", "miniature"]}

_colour = ["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"]

_mood = {"positive": ["beautiful", "elegant", "lovely", "pretty", "majestic", "magical"],
         "neutral": ["plan", "average-looking", "normal-looking", "common-or-garden"],
         "negative": ["moody", "spooky", "haunted", "scary", "dark", "old"]}


class Location(object):
    def __init__(self, character=None):
        self.location = random.choice(_location)
        self.colour = random.choice(_colour)
        self._size = random.choice(list(_size.keys()))
        self._mood = random.choice(list(_mood.keys()))
        if character is None:
            self.character = Creature()
        else:
            self.character = character

    @property
    def size(self):
        return random.choice(_size.get(self._size))

    @property
    def mood(self):
        return random.choice(_mood.get(self._mood))

    def description(self):
        choices = [self.colour, self.size, self.mood]
        roll = random.random()
        if roll < 0.1:
            return ""
        elif roll < 0.5:
            choice = random.sample(choices, 2)
            choice.insert(1, "and")
            return " ".join(choice)
        else:
            return random.choice(choices)

    def __repr__(self):
        return " ".join([self.location, self.size, self.mood, self.character.__repr__()])
