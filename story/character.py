import random

class Character(object):

    def __init__(self, name, kind, gender, emotion='happy'):
        self.name = name
        self.kind = kind
        self.gender = gender
        self.emotion = emotion


def name_gen():
    return random.choice([])