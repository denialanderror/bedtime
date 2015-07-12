__author__ = 'Sam Joseph'

class Character(object):

    # def __init__(self, name, kind, gender, emotion, attributes, actions):
    #     self.name = name
    #     self.kind = kind
    #     self.gender = gender
    #     self.emotion = emotion
    #     self.attributes = attributes
    #     self.actions = actions

    def __init__(self, name, kind, gender):
        self.name = name
        self.kind = kind
        self.gender = gender

class Location(object):

    # def __init__(self, name, character, attributes, actions):
    #     self.name = name
    #     self.character = character
    #     self.attributes = attributes
    #     self.actions = actions

    def __init__(self, name):
        self.name = name
