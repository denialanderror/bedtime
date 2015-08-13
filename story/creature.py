import random
from app.models import Terms

_gender = ["male", "female"]


class Creature(object):
    def __init__(self, name=None, kind=None, gender=None):
        """all variables with multiple choices are stored as indexes"""
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
        self._colour = random.sample(Terms.objects(category='colour').distinct('terms'), 2)
        self._pattern = random.choice(Terms.objects(category='pattern').distinct('terms'))
        self._size = random.choice(Terms.objects(category='size').distinct('name'))
        # self.size = random.randrange(len(_size))
        self._covering = random.choice(Terms.objects(category='covering').distinct('name'))
        # self.covering = random.randrange(len(_covering))
        self._emotion = random.choice(Terms.objects(category='emotion').distinct('name'))
        # self.happiness = random.randrange(len(_happiness))
        # self.anger = random.randrange(len(_anger))

    @property
    def gender(self):
        if self._gender == "male":
            return "he"
        return "she"

    @property
    def colour_mixer(self):
        if self._pattern == "plain":
            return self._colour[0]
        else:
            return " ".join([self._colour[0], "and", self._colour[1], self._pattern])

    def ref_expr(self, full=True):
        if full:
            return random.choice(["a {0} {1} named {2}".format(self.description(), self.kind, self.name),
                                 "{0} the {1} {2}".format(self.name, self.description(), self.kind)])
        else:
            return random.choice(["the {0} {1}".format(self.description(), self.kind), self.name])

    def description(self):
        choices = [self.colour_mixer, random.choice(Terms.objects(category='size', name=self._size).distinct('terms')),
                   random.choice(Terms.objects(category='emotion', name=self._emotion).distinct('terms')),
                   random.choice(Terms.objects(category='covering', name=self._covering).distinct('terms'))]
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
        return " ".join([self._gender, self.name, self._colour[0], self._colour[1], self._pattern, self._size,
                         self._covering, self._emotion])
