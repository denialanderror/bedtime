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
        self.story_index = 0
        self.quest = quest
        self.story_length = story_length
        self.locations = [Location(), Location()]
        self.end = False

    def add_location(self):
        """Shuffles next location to current location and adds a new one"""
        self.locations.append(Location())
        self.locations.pop(0)

    def realise(self, sentence):
        """Replaces text markup with the correct story attributes
        and corrects punctuation."""
        realiser = {'_heroName': self.characters[0].name,
                    '_heroKind': self.characters[0].kind,
                    '_heroGender': self.characters[0].gender,
                    '_ref_expr_hero_full': self.characters[0].ref_expr(True),
                    '_ref_expr_hero': self.characters[0].ref_expr(False),
                    '_location': self.locations[0].location,
                    '_locationDescription': self.locations[0].description(),
                    '_heroDescription': self.characters[0].description(),
                    '_npcName': self.characters[1].name,
                    '_npcKind': self.characters[1].kind,
                    '_npcGender': self.characters[1].gender,
                    '_npcDescription': self.characters[1].description(),
                    '_ref_expr_npc_full': self.characters[1].ref_expr(True),
                    '_ref_expr_npc': self.characters[1].ref_expr(False),
                    '_item': self.quest,
                    '_nextLocation': self.locations[1].location,
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

    def aggregation(self, phrases):
        """Concatenates strings into one sentence and corrects names to pronouns"""
        if len(phrases) == 1:
            return self.phrase(phrases[0])
        p1 = self.phrase(phrases[0])
        p2 = self.phrase(phrases[1])
        if p1[0].lower() == p2[0].lower():
            p1 += random.choice(["and".split(), "and _heroGender".split()])
            return p1 + p2[1:]
        else:
            p1.append(',')
            return p1 + p2

    def phrase(self, category):
        """Returns a list representation of a randomised string from the requested
        expression type, using regex to maintain separation of punctuation within
        the lists
        This was originally done using a dict implementation of a switch statement but this resulted
        in all options being evaluated and making extraneous calls to the database"""
        # action/reaction
        if category in ['npc_action', 'reaction']:
            expression = random.choice(
                Actions.objects(self.locations[0].character.emotion + '_action').distinct(category))
            # yes/no
            if category == 'answer':
                if self.locations[0].character.emotion == 'angry':
                    category = 'angry_answer'
                elif self.story_index == self.story_length - 1:
                    category = 'yes'
                else:
                    category = 'no'
            # all other expressions
        else:
            expression = random.choice(Texts.objects(category=category).distinct('texts'))
        # post processing
        if category == 'opening':
            expression = "once upon a time" + expression
        elif category == 'action':
            expression = "_ref_expr_npc" + " " + expression + " _ref_expr_hero"
        return re.findall(r"[\w']+|[-.,!?;:\"\[\]]", str(expression).strip())

    def story(self):
        """Generates the next scene of the story, with separate beginning, middle and end."""
        self.characters[1] = self.locations[1].character  # load next non-user character
        if self.story_index == 0:
            return [self.realise(self.aggregation(['opening', 'intro'])), self.realise(self.phrase('quest'))]
        if self.story_index < self.story_length - 1:
            return self.scene()
        else:
            self.end = True
            return [self.realise(self.phrase("end")),
                    "And they all lived happily ever after.",
                    "The end."]

    def scene(self):
        """Generates the scenes in between the middle and end of the story, where each scene is one page.
        Sentence choices are lists of lists (the inner lists are to be aggregated) in order to use random.choice,
        which then need to be flattened"""
        roll = random.Random() < 0.2
        if roll:
            # No character at this location so can't finish here...
            sentences = random.choice([[['location', 'status'], ['no_npc', 'no_npc_action'], ['next']],
                                       [['location', 'no_npc'], ['no_npc_action', 'status'], ['next']]])
        else:
            # Location and NPC meeting options
            sentences = random.choice([[['location', 'meet']],
                                       [['location', 'status'], ['meet', 'description']]])
            if random.choice([True, False]) is True:
                # Adds an interaction
                sentences.append([['npc_action', 'reaction']]) # PUT IN CHARACTER ACTIONS?
            # Question and answer
            sentences.append(random.choice([[['question'], ['answer']], [['non_question', 'non_answer']]]))

        if self.story_index == self.story_length - 1 and (self.locations[1].character.emotion == 'angry' or roll < 0.2):
            # Angry characters cannot answer and story must finish with one
            self.story_length += 1
        if self.story_index < self.story_length - 1:
            sentences.append([['next']])
        # flatten list
        sentences = [item for sublist in sentences for item in sublist]
        # transform phrases and aggregate
        sentences = [self.aggregation(phrases) for phrases in sentences]
        # realise
        sentences = [self.realise(sentence) for sentence in sentences]
        return sentences

    def generate(self):
        """Creates story by adding scenes to pages until the end is reached.
        Story added to MongoDB instance and the UUID of the story is returned to the caller"""
        pages = []
        while not self.end:
            pages.append(Pages(page=self.story_index, sentences=self.story()))
            self.add_location()
            self.story_index += 1
        story = Story(pages=pages)
        story.save()
        return story.id
