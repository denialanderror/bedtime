import string
import random
from .texts import phrase
from app import redis
from story.location import Location
from story.creature import Creature


class Writer(object):
    def __init__(self, name, kind, gender, quest):
        hero = Creature(name, kind, gender)
        self.characters = [hero, hero]  # added twice to correctly initialise list
        self._story_index = 0
        self.quest = quest
        self.end = False
        self.locations = [Location(), Location(), Location(), Location(), Location(), Location(), Location()]

    @property
    def story_index(self):
        return self._story_index % len(self.locations)

    @story_index.setter
    def story_index(self, index):
        self._story_index = index

    def realise(self, sentence: list):
        """
        Replaces text markup with the correct story attributes
        and corrects punctuation.
        """
        realiser = {'_charName': self.characters[0].name,
                    '_charKind': self.characters[0].kind,
                    '_charGender': self.characters[0].gender,
                    '_charEmotion': self.characters[0].emotion,
                    '_charLocation': self.locations[self.story_index].location,
                    # '_charDescription': self.descriptions(self.characters[0]),
                    '_locationCharName': self.characters[1].name,
                    '_locationCharKind': self.characters[1].kind,
                    '_locationCharGender': self.characters[1].gender,
                    '_locationCharEmotion': self.characters[1].emotion,
                    '_questItem': self.quest,
                    '_nextLocation': self.locations[(self.story_index + 1) % len(self.locations)].location,
                    }
        try:
            realised = [realiser[w] if w[0] == '_' else w for w in
                        sentence]  # sentence as a list with correct story attributes

            # creates sentence from list while leaving punctuation
            realised_string = ''.join([('' if char in [".", ",", "?", "!", "", '"', ":" ";"] else ' ')
                                       + char for char in realised]).strip()

            # capitalises first word in sentence, ignoring punctuation such as "
            if realised_string[0] in string.punctuation:
                realised_string = realised_string[0] + realised_string[2].capitalize() + realised_string[3:]
            else:
                realised_string = realised_string.capitalize()[0] + realised_string[1:]

            # adds full stop to end, unless end is terminal punctuation
            if realised_string[-1] in [".", ",", "?", "!"]:
                return realised_string
            else:
                return realised_string + "."

        except IndexError:
            # converts empty list to empty sentence
            return ""

    def aggregation(self, s1: list, s2: list):
        """Concatenates strings into one sentence and corrects names to pronouns
        """
        try:
            if s1[0].lower() == s2[0].lower():
                s1 += random.choice(["and".split(), "and there _charGender".split()])
                return s1 + s2[1:]
            else:
                s1.append(',')
                return s1 + s2
        except IndexError:
            # ignore string content if one or more list is empty
            return s1 + s2

    def descriptions(self, index):
        """Places in appropriate adjectives
        Index refers to character in characters
        """
        pass

    def scene(self):
        """Generates the next scene of the story.
        """
        self.characters[1] = self.locations[self.story_index].character  # load next non-user character
        if self.story_index == 0:
            return [self.realise(self.aggregation(
                self.aggregation("Once upon a time".split(), phrase("openings")), phrase("intro")))]
        elif self.story_index < len(self.locations) - 2:
            return [self.realise(self.aggregation(phrase("location_actions"), phrase("meet_actions"))),
                    self.realise(phrase("character_actions")),
                    self.realise(phrase("questions")),
                    self.realise(phrase("no")),
                    self.realise(phrase("next_scene"))]
        elif self.story_index < len(self.locations) - 1:
            return [self.realise(self.aggregation(phrase("location_actions"), phrase("meet_actions"))),
                    self.realise(phrase("character_actions")),
                    self.realise(phrase("questions")),
                    self.realise(phrase("yes"))]
        else:
            self.end = True
            return [self.realise(phrase("closes")),
                    "And they all lived happily ever after.",
                    "The end."]

    def generate(self):
        """Creates story by adding scenes until the end is reached.
        Story added to Redis instance under the given story ID, which
        is returned to the caller"""
        story_id = redis.incr("next_id")
        while not self.end:
            redis.zadd("story_id:" + str(story_id), self.scene(), self.story_index)
            self.story_index += 1
        return story_id
