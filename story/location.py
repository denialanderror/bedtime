import random
from app.models import Terms
from story.creature import Creature


class Location(object):
    def __init__(self, character=None):
        """Location attributes with multiple matching terms are stored as a name rather
        than term e.g. Size is stored as either big, medium or small, each of which has matching
        terms
        Locations are created without a specified character as default, though characters can be
        specified"""
        self.location = random.choice(Terms.objects(category='location').distinct('terms'))
        self.colour = random.choice(Terms.objects(category='colour').distinct('terms'))
        self._size = random.choice(Terms.objects(category='size').distinct('name'))
        self._mood = random.choice(Terms.objects(category='mood').distinct('name'))
        if character is None:
            self.character = Creature()
        else:
            self.character = character


    @property
    def size(self):
        return random.choice(Terms.objects(category='size', name=self._size).distinct('terms'))

    @property
    def mood(self):
        return random.choice(Terms.objects(category='mood', name=self._mood).distinct('terms'))

    def description(self):
        """Produces a randomised description of the character from their attributes
        The number of attributes returned is based on a randomly generated number
        :returns List"""
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
