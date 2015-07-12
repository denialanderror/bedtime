__author__ = 'denialanderror'

class Action(object):

    def __init__(self, verb, det, emotion):
        self.verb = verb
        self.det = det
        self.emotion = emotion  # the emotion which stops the action from occuring...?
        # prepositions (with/on) go here or in the referring expressions
