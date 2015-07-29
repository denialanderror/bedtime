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

_size = {"big": ["big", "giant", "enormous", "gigantic", "huge", "massive", "great", "large", "tremendous"],
         "average": ["average", "normal"],
         "small": ["small", "tiny", "little", "petite", "pocket-sized", "baby"]}

_colour = ["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"]

_pattern = ["spots", "stripes", "plain"]

_covering = {"fur": ["fur", "fluff", "down", "hair"],
             "spines": ["spines", "spikes", "prickles"],
             "scales": ["scales"],
             "skin": ["skin"]}

_emotion = {"happy": ["happy", "jolly", "cheerful", "bouncy", "smiley", "joyous"],
            "neutral": ["neutral"],
            "sad": ["sad", "unhappy", "moody", "tearful"],
            "angry": ["angry", "scary", "frightening", "cross"],
            "scared": ["scared", "fearful", "frightened"]}

_kind = ["thing", "creature", "animal", "critter", "beast"]


class Creature(object):
    def __init__(self, name=None, kind=None, gender=None):
        if gender is None:
            self.gender = random.choice(_gender)
        else:
            self.gender = gender

        if name is None:
            self.name = random.choice(_names.get(self.gender))
        else:
            self.name = name
        if kind is None:
            self.kind = random.choice(_kind)
        else:
            self.kind = kind
        self.colour = [random.choice(_colour), random.choice(_colour)]
        self.pattern = random.choice(_pattern)
        self._size = random.choice(list(_size.keys()))
        self._covering = random.choice(list(_covering.keys()))
        self._emotion = random.choice(list(_emotion.keys()))

    @property
    def size(self):
        return random.choice(_size.get(self._size))

    @property
    def covering(self):
        return random.choice(_covering.get(self._covering))

    @property
    def emotion(self):
        return random.choice(_emotion.get(self._emotion))

    @emotion.setter
    def emotion(self, value):
        self._emotion = value

    def __repr__(self):
        return " ".join([self.gender, self.name, self.colour[0], self.colour[1], self.pattern, self.size,
                         self.covering, self.emotion])
