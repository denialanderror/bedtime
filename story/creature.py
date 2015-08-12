import random

_gender = ["male", "female"]

_names = {"male": ['Muhammad', 'Oliver', 'Jack', 'Noah', 'Jacob', 'Charlie', 'Harry', 'Joshua', 'James',
                   'Ethan', 'Thomas', 'William', 'Henry', 'Oscar', 'Daniel', 'Max', 'Leo', 'George', 'Alfie',
                   'Alexander', 'Lucas', 'Logan', 'Dylan', 'Adam', 'Isaac', 'Finley', 'Samuel', 'Benjamin',
                   'Theo', 'Liam', 'Freddie', 'Joseph', 'Sebastian', 'Harrison', 'Archie', 'Jake', 'Mason',
                   'Lewis', 'Nathan', 'Luke', 'Matthew', 'Jayden', 'Riley', 'Alex', 'Zachary', 'Elijah',
                   'Edward', 'Eliot', 'Ryan', 'Toby', 'Sam', 'Luca', 'Aiden', 'Arthur', 'Aaron', 'Michael',
                   'Reuben', 'David', 'Tyler', 'Caleb', 'Teddy', 'Ben', 'Evan', 'Rory', 'Jamie', 'Austin',
                   'Ollie', 'Gabriel', 'Finn', 'Dexter', 'Kian', 'Blake', 'Owen', 'Jonathan', 'Felix',
                   'Jackson', 'Connor', 'Seth', 'Omar', 'Stanley', 'Callum', 'Ali', 'Hugo', 'Harvey', 'Kai',
                   'Eli', 'Leon', 'Jasper', 'Cameron', 'Tommy', 'Hunter', 'Milo', 'Ibrahim', 'Jason', 'Jude',
                   'Andrew', 'Nathaniel', 'John', 'Aarav', 'Kyle'],
          "female": ['Sophia', 'Emily', 'Lily', 'Olivia', 'Amelia', 'Isla', 'Isabella', 'Ava', 'Sophie',
                     'Chloe', 'Isabelle', 'Ella', 'Poppy', 'Mia', 'Evie', 'Jessica', 'Charlotte', 'Grace',
                     'Emma', 'Alice', 'Ruby', 'Eva', 'Freya', 'Molly', 'Scarlett', 'Lucy', 'Abigail', 'Phoebe',
                     'Nur', 'Daisy', 'Elizabeth', 'Hannah', 'Florence', 'Ellie', 'Maryam', 'Erin', 'Sienna',
                     'Elsie', 'Matilda', 'Evelyn', 'Maya', 'Lola', 'Bella', 'Rosie', 'Holly', 'Millie',
                     'Annabelle', 'Jasmine', 'Imogen', 'Georgia', 'Sarah', 'Ivy', 'Emilia', 'Rose', 'Eliza',
                     'Layla', 'Mila', 'Anna', 'Willow', 'Amelie', 'Maisie', 'Summer', 'Zara', 'Katie', 'Megan',
                     'Amber', 'Harriet', 'Violet', 'Madison', 'Gracie', 'Leah', 'Aria', 'Thea', 'Lara', 'Elsa',
                     'Zoe', 'Eleanor', 'Kayla', 'Esme', 'Victoria', 'Maria', 'Iris', 'Gabriella', 'Lexi',
                     'Harper', 'Ariana', 'Lacey', 'Faith', 'Alexis', 'Robyn', 'Skye', 'Alyssa', 'Amy', 'Elena',
                     'Bethany', 'Rebecca', 'Lottie', 'Clara', 'Niamh', 'Naomi']}

# Commented out variables are dict implementation which has been amended to lists for index

_size = {"big": ["big", "giant", "enormous", "gigantic", "huge", "massive", "great", "large", "tremendous"],
         "average": ["average", "normal", "medium-sized", "unassuming"],
         "small": ["small", "tiny", "little", "petite", "pocket-sized", "miniature"]}

_covering = {"furry": ["furry", "fluffy", "downy", "hairy"],
             "spiny": ["spiny", "spiky", "prickly"],
             "scales": ["scales", "armoured", "plated"]}

_emotion = {"happy": ["happy", "jolly", "cheerful", "bouncy", "smiley", "joyous"],
            "sad": ["sad", "unhappy", "moody", "tearful"],
            "angry": ["angry", "scary", "frightening", "cross", "furious", "vicious"],
            "scared": ["scared", "fearful", "frightened"]}

# _size = [["big", "giant", "enormous", "gigantic", "huge", "massive", "great", "large", "tremendous"],
#          ["average", "normal" "medium-sized"],
#          ["small", "tiny", "little", "petite", "pocket-sized", "baby"]]
#
# _covering = [["fur", "fluff", "down", "hair"],
#              ["spines", "spikes", "prickles"],
#              ["scales"], ["skin"]]

# _happiness = [["happy", "jolly", "cheerful", "bouncy", "smiley", "joyous"], ["neutral"],
#               ["sad", "unhappy", "moody", "tearful"]]
#
# _anger = [["angry", "scary", "frightening", "cross", "furious"], ["neutral"],
#           ["scared", "fearful", "frightened"]]

_kind = "thing", "creature", "animal", "critter", "beast", "monster", "thingamajig"

# _kind = ["dragon", "hamster", "hedgehog", "badger", "fox", "horse", "pony", "donkey", "panda", "mouse",
#          "rabbit", "bear", "snake", "hippo", "cat", "dog", "frog", "lizard", "unicorn", "crocodile"]

_colour = ["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"]

_pattern = ["spotted", "striped", "plain", "freckled", "checkered"]


class Creature(object):
    def __init__(self, name=None, kind=None, gender=None):
        """all variables with multiple choices are stored as indexes"""
        if gender is None or gender not in _gender:
            self._gender = random.choice(_gender)
        else:
            self._gender = gender

        if name is None:
            self.name = random.choice(_names.get(self._gender))
        else:
            self.name = name
        if kind is None:
            self.kind = random.choice(_kind)
        else:
            self.kind = kind
        self._colour = random.sample(_colour, 2)
        self._pattern = random.choice(_pattern)
        self.size = random.choice(list(_size.keys()))
        # self.size = random.randrange(len(_size))
        self.covering = random.choice(list(_covering.keys()))
        # self.covering = random.randrange(len(_covering))
        self.emotion = random.choice(list(_emotion.keys()))
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

    def description(self):
        choices = [self.colour_mixer, random.choice(_size.get(self.size)), random.choice(_emotion.get(self.emotion)),
                   random.choice(_covering.get(self.covering))]
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
        return " ".join([self._gender, self.name, self._colour[0], self._colour[1], self._pattern, self.size,
                         self.covering, self.emotion])
