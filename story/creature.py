import random
from app.models import Terms

_gender = ["male", "female"]


class Creature(object):
    def __init__(self, name=None, kind=None, gender=None):
        """Creature attributes with multiple matching terms are stored as a name rather
        than term e.g. Size is stored as either big, medium or small, each of which has matching
        terms"""
        if gender is None or gender not in _gender:
            self._gender = random.choice(_gender)
        else:
            self._gender = gender

        if name is None:
            self.name = random.choice(Terms.objects(name=self._gender).distinct('terms'))
        else:
            self.name = name.title()
        if kind is None:
            self.kind = random.choice(Terms.objects(category='kind').distinct('terms'))
        else:
            self.kind = kind
        self.colour = random.sample(Terms.objects(category='colour').distinct('terms'), 2)
        self.pattern = random.choice(Terms.objects(category='pattern').distinct('terms'))
        self.size = random.choice(Terms.objects(category='size').distinct('name'))
        self.covering = random.choice(Terms.objects(category='covering').distinct('name'))
        self._emotion = random.choice(Terms.objects(category='emotion').distinct('name'))

    @property
    def emotion(self):
        return random.choice(Terms.objects(category='emotion', name=self._emotion).distinct('terms'))

    @property
    def emotion_action(self):
        return self._emotion + "_action"

    @property
    def gender(self):
        if self._gender == "male":
            return "he"
        return "she"

    @property
    def colour_mixer(self):
        """Returns a colour description based on pattern and colour attributes
        :returns String"""
        if self.pattern == "plain":
            return self.colour[0]
        else:
            return " ".join([self.colour[0], "and", self.colour[1], self.pattern])

    def ref_expr(self, full=True):
        """Returns a full referring expression for the character
        The shortened version is used when the character has already been referenced in the story
        :returns String"""
        if full:
            return random.choice(["a {0} {1} named {2}".format(self.description(), self.kind, self.name),
                                 "{0} the {1} {2}".format(self.name, self.description(), self.kind),
                                  "{0} the {1}".format(self.name, self.kind),
                                  "a {0} named {1}".format(self.kind, self.name)])
        else:
            return random.choice(["the {0} {1}".format(self.description(), self.kind), self.name])

    def description(self):
        """Produces a randomised description of the character from their attributes
        The number of attributes returned is based on a randomly generated number
        :returns List"""
        choices = [self.colour_mixer, random.choice(Terms.objects(category='size', name=self.size).distinct('terms')),
                   random.choice(Terms.objects(category='emotion', name=self._emotion).distinct('terms')),
                   random.choice(Terms.objects(category='covering', name=self.covering).distinct('terms'))]
        roll = random.random()
        if roll < 0.2:
            return ""
        else:
            return random.choice(choices)
