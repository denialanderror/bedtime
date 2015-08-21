import string
import random
from .location import Location
from .creature import Creature
from app.models import Story, Pages, Texts, Actions
import re

_test = ['this is a normal sentence']  # for test purposes only, to avoid issues with random.choice


class Writer(object):
    def __init__(self, name, kind, gender, quest, story_length):
        # hero = Creature(name, kind, gender)
        hero = Creature(name=name, gender=gender)
        self.characters = [hero, hero]  # added twice to correctly initialise list
        self._story_index = 0
        self.quest = quest
        self.story_length = story_length
        self.locations = [Location(), Location()]

    @property
    def story_index(self):
        """Avoids Index Errors when finding next location"""
        return self._story_index % len(self.locations)

    @story_index.setter
    def story_index(self, index):
        self._story_index = index

    def add_location(self):
        self.locations.append(Location())

    def realise(self, sentence):
        """Replaces text markup with the correct story attributes
        and corrects punctuation."""
        realiser = {'_charName': self.characters[0].name,
                    '_charKind': self.characters[0].kind,
                    '_charGender': self.characters[0].gender,
                    '_ref_expr_hero_full': self.characters[0].ref_expr(True),
                    '_ref_expr_hero': self.characters[0].ref_expr(False),
                    '_location': self.locations[self.story_index].location,
                    '_locationDescription': self.locations[self.story_index].description(),
                    '_charDescription': self.characters[0].description(),
                    '_npcName': self.characters[1].name,
                    '_npcKind': self.characters[1].kind,
                    '_npcGender': self.characters[1].gender,
                    '_npcDescription': self.characters[1].description(),
                    '_ref_expr_npc_full': self.characters[1].ref_expr(True),
                    '_ref_expr_npc': self.characters[1].ref_expr(False),
                    '_questItem': self.quest,
                    '_nextLocation': self.locations[(self.story_index + 1) % len(self.locations)].location,
                    }
        try:
            realised = [realiser[w] if w[0] == '_' else w for w in
                        sentence]  # sentence as a list with correct story attributes

            # corrects a to an before a vowel
            for index, word in enumerate(realised):
                if word == 'a' and realised[index + 1][0] in ['a', 'e', 'i', 'o', 'u']:
                    realised[index] = "an"

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

    # def aggregation(self, s1: list, s2: list): - Dokku does not like Python3 type hinting!
    def aggregation(self, s1, s2=None):
        """Concatenates strings into one sentence and corrects names to pronouns"""
        try:
            if s1[0].lower() == s2[0].lower():
                s1 += random.choice(["and".split(), "and _charGender".split()])
                return s1 + s2[1:]
            else:
                s1.append(',')
                return s1 + s2
        except IndexError:
            # ignore string content if one or more list is empty
            return s1 + s2

    def action(self):
        switch = [self.phrase("character_actions"), self.phrase("npc_actions")]
        return ''

    def emotion_reaction(self):
        # happiness scale
        # if self.characters[0].happiness == "neutral":
        #     self.characters[0].happiness = self.characters[1].happiness
        #
        # if self.characters[0].happiness == "happy":
        #     if self.characters[1].happiness == "sad":
        #         if self.characters[1].size == "small":
        #             self.characters[0].happiness = self.characters[1].happiness
        #         else:
        #             self.characters[0].happiness = "neutral"
        #
        # if self.characters[0].happiness == "sad":
        #     if self.characters[1].happiness == "happy":
        #         if self.characters[1].size == "big":
        #             self.characters[0].happiness = self.characters[1].happiness
        #         else:
        #             self.characters[0].happiness = "neutral"
        #
        # # anger scale
        # if self.characters[1].anger == "big":
        #     self.characters[0].anger == "scared"
        # else:
        #     pass
        pass

    def phrase(self, expression):
        """Returns a list representation of a randomised string from the requested
        expression type, using regex to maintain separation of punctuation within
        the lists"""
        switch = {"openings": random.choice(Texts.objects(category='openings').distinct('texts')),
                  "intro": random.choice(Texts.objects(category='intro').distinct('texts')),
                  "location_actions": random.choice(Texts.objects(category='location_actions').distinct('texts')),
                  "meet_actions": random.choice(Texts.objects(category='meet_actions').distinct('texts')),
                  "character_actions":
                      "_ref_expr_hero " + random.choice(
                          Actions.objects(category='character_actions').distinct('actions')) + " with _ref_expr_npc",
                  "npc_actions":
                      "_ref_expr_npc" + " " + random.choice(
                          Actions.objects(category='character_actions').distinct('actions')) + " with _ref_expr_hero",
                  "questions": random.choice(Texts.objects(category='questions').distinct('texts')),
                  "yes": random.choice(Texts.objects(category='yes').distinct('texts')),
                  "no": random.choice(Texts.objects(category='no').distinct('texts')),
                  "next_scene": random.choice(Texts.objects(category='next_scene').distinct('texts')),
                  "closes": random.choice(Texts.objects(category='closes').distinct('texts')),
                  "test": _test[0]
                  }
        return re.findall(r"[\w']+|[-.,!?;:\"\[\]]", str(switch[expression]).strip())

    def story(self):
        """Generates the next scene of the story, with separate beginning, middle and end."""
        self.characters[1] = self.locations[self.story_index].character  # load next non-user character
        if self.story_index == 0:
            # add in a character description
            return [self.realise(self.aggregation(
                self.aggregation("Once upon a time".split(), self.phrase("openings")), self.phrase("intro")))]
        elif self.story_index < self.story_length - 1:
            return [self.realise(self.aggregation(self.phrase("location_actions"), self.phrase("meet_actions"))),
                    self.realise(self.phrase("character_actions")),
                    self.realise(self.phrase("questions")),
                    self.realise(self.phrase("no")),
                    self.realise(self.phrase("next_scene"))]
        elif self.story_index < self.story_length:
            return [self.realise(self.aggregation(self.phrase("location_actions"), self.phrase("meet_actions"))),
                    self.realise(self.phrase("character_actions")),
                    self.realise(self.phrase("questions")),
                    self.realise(self.phrase("yes"))]
        else:
            self.end = True
            return [self.realise(self.phrase("closes")),
                    "And they all lived happily ever after.",
                    "The end."]

    def scene(self):
        """Generates the scenes in between the middle and end of the story
        Sentence choices are lists of lists (the inner lists are to be aggregated) in order to use random.choice,
        which then need to be flattened
        Each scene is one page"""
        if random.Random() < 0.2:
            # No character at this location so can't finish here...
            sentences = random.choice([[['location', 'status'], ['no_npc', 'no_npc_action'], ['next_location']],
                                       [['location', 'no_npc'], ['no_npc_action', 'status'], ['next_location']]])
        else:
            # Location and NPC meeting options
            sentences = random.choice([[['location', 'meet']],
                                       [['location', 'status'], ['meet', 'description']]])
            if random.choice([True, False]) is True:
                # Adds an interaction
                sentences.append(['action', 'reaction'])
            # Question and answer
            sentences.append(random.choice([[['question'], ['answer']], [['non_question', 'non_answer']]]))
        if self.story_index == self.story_length - 1 and self.locations[1].character.emotion == 'angry':
            # Angry characters cannot answer and story must finish with one
            self.story_length += 1

        # flatten list
        sentences = [item for sublist in sentences for item in sublist]
        # transform phrases and aggregate

        # realise
        return sentences

    def generate(self):
        """Creates story by adding scenes to pages until the end is reached.
        Story added to MongoDB instance and the UUID of the story is returned to the caller"""
        pages = []
        while self.story_index < self.story_length:
            pages.append(Pages(page=self.story_index, sentences=self.story()))
            self.add_location()
            self.story_index += 1
        story = Story(pages=pages)
        story.save()
        return story.id
