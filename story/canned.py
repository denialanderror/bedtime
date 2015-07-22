import string
import random
from .texts import phrase
from app import redis

class Character(object):
    def __init__(self, name, kind, gender, emotion):
        self.name = name
        self.kind = kind
        self.gender = gender
        self.emotion = emotion


class Location(object):
    def __init__(self, name, character):
        self.name = name
        self.character = character


class Canned(object):
    def __init__(self, name, kind, gender, quest):
        hero = Character(name, kind, gender, "happy")
        self.characters = [hero, hero]
        self._story_index = 0
        self.quest = quest
        self.end = False
        self.locations = [Location("hill", Character("Barry", "hedgehog", "he", "happy")),
                          Location("cave", Character("Ryan", "dragon", "he", "angry")),
                          Location("castle", Character("Polly", "princess", "she", "happy")),
                          Location("farm", Character("Jonah", "cow", "he", "sad")),
                          Location("forest", Character("Harold", "snake", "he", "angry")),
                          Location("river", Character("Felicity", "fish", "she", "sad")),
                          Location("beach", Character("Patricia", "crab", "she", "happy"))]
        random.shuffle(self.locations)

    @property
    def story_index(self):
        return self._story_index % len(self.locations)

    @story_index.setter
    def story_index(self, index):
        self._story_index = index

    def realise(self, sentence):
        """
        Replaces text markup with the correct story attributes.
        """
        realiser = {'_charName': self.characters[0].name,
                    '_charKind': self.characters[0].kind,
                    '_charGender': self.characters[0].gender,
                    '_charLocation': self.locations[self.story_index].name,
                    '_charEmotion': self.characters[0].emotion,
                    '_locationCharName': self.characters[1].name,
                    '_locationCharKind': self.characters[1].kind,
                    '_locationCharGender': self.characters[1].gender,
                    '_locationCharEmotion': self.characters[1].emotion,
                    '_questItem': self.quest,
                    '_nextLocation': self.locations[(self.story_index + 1) % len(self.locations)].name,
                    }
        realised = [realiser[w] if w[0] == '_' else w for w in
                    sentence]  # sentence as a list with correct story attributes
        # creates sentence from list while leaving punctuation
        try:
            realised_string = ''.join([('' if char in string.punctuation else ' ') + char for char in realised]).strip()
            # correcting punctuation and capitalising the start of the sentence
            if realised_string[0] in string.punctuation:
                return realised_string[0] + realised_string[2].capitalize() + realised_string[3:] + "."
            else:
                return realised_string.capitalize()[0] + realised_string[1:] + "."
        except Exception as e:
            print(realised)

    def aggregation(self, s1, s2):
        if s1[0] == s2[0]:
            s1 += random.choice(["and".split(), "and there _charGender".split()])
            return s1 + s2[1:]
        else:
            s1.append(',')
            return s1 + s2

    def scene(self):
        self.characters[1] = self.locations[self.story_index].character
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
        story_id = redis.incr("next_id")
        while not self.end:
            redis.zadd("story_id:" + str(story_id), self.scene(), self.story_index)
            self.story_index += 1
        return story_id
