from app import db, models
from app.models import *

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
         "average": ["average", "normal", "medium-sized", "unassuming"],
         "small": ["small", "tiny", "little", "petite", "pocket-sized", "miniature"]}

_covering = {"furry": ["furry", "fluffy", "downy", "hairy"],
             "spiny": ["spiny", "spiky", "prickly"],
             "scales": ["scales", "armoured", "plated"]}

_emotion = {"happy": ["happy", "jolly", "cheerful", "bouncy", "smiley", "joyous"],
            "sad": ["sad", "unhappy", "moody", "tearful"],
            "angry": ["angry", "scary", "frightening", "cross", "furious", "vicious"],
            "scared": ["scared", "fearful", "frightened"]}

_mood = {"positive": ["beautiful", "elegant", "lovely", "pretty", "majestic", "magical"],
         "neutral": ["plan", "average-looking", "normal-looking", "common-or-garden"],
         "negative": ["moody", "spooky", "haunted", "scary", "dark", "old"]}

_kind = {"kind": ["thing", "creature", "animal", "critter", "beast", "monster", "thingamajig"]}

_colour = {"colour": ["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"]}

_pattern = {"pattern": ["spotted", "striped", "plain", "freckled", "checkered"]}

_location = {"location": ["house", "hut", "castle", "tower", "lighthouse", "garden", "wood", "forest", "field", "town",
                          "river", "stream", "beach", "dunes", "seashore", "cave", "farm", "hill"]}

term_dict = {'name': _names,
             'size': _size,
             'covering': _covering,
             'emotion': _emotion,
             'mood': _mood,
             'kind': _kind,
             'colour': _colour,
             'pattern': _pattern,
             'location': _location}


def populate(term_dict):
    for k, v in term_dict.items():
        category = k
        dictionary = v
        for key, value in dictionary.items():
            entry = Terms(category=category, name=key, terms=value)
            entry.save()

populate(term_dict)