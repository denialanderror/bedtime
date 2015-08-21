from app.models import *

"""
This class is used solely for initial generation of the database.
It has no purpose within the application.
"""

# names taken from top 100 baby names for boys and girls of 2014
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
            "angry": ["angry", "scary", "frightening", "cross", "furious", "vicious"],
            "scared": ["scared", "fearful", "frightened", "sad", "unhappy", "moody", "tearful"]}

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


def populate_term(term_dict):
    for category, dictionary in term_dict.items():
        for name, terms in dictionary.items():
            entry = Terms(category=category, name=name, terms=terms)
            entry.save()

_openings = ["a long long time ago",
             "in a galaxy far far away",
             "in a far off land",
             "over the hills and far away"]

_intro = ["there was _ref_expr_hero_full",
          "there lived _ref_expr_hero_full",
          "you would find _ref_expr_hero_full",
          "you could hear stories about _ref_expr_hero_full",
          "_ref_expr_hero_full lived"]

_location_actions = ["_charName walked to the _locationDescription _location",
                     "so _charName went to the _locationDescription _location",
                     "_charName travelled to the _locationDescription _location",
                     "when _charName got to the _locationDescription _location",
                     "over by the _locationDescription _location",
                     "After the long walk to the _locationDescription _location",
                     "at the _locationDescription _location"]

_meet_actions = ["_charName met _ref_expr_npc_full",
                 "_charName found _ref_expr_npc_full",
                 "_ref_expr_npc_full appeared",
                 "_ref_expr_npc_full was there waiting"]

_questions = ["\"have you seen my _questItem ?\" said _charName",
              "\"Do you know where my _questItem is ?\" asked _charName",
              "\"any idea where I could find my _questItem ?\" said _charName"]

_yes = ["\"it's just over there\" said _npcName",
        "\"yes I have it it in my pocket\" said _npcName"]

_no = ["\"I'm not sure what you are talking about\" said _npcName",
       "\"sorry but no\" said _npcName"]

_next_scene = ["\"have you tried the _nextLocation ?\"",
               "\"try over there by the _nextLocation\""]

_closes = ["_charName was so happy to get the _questItem back",
           "_charName went home to the _location with the _questItem"]

text_dict = {'openings': _openings,
             'intro': _intro,
             'location_actions': _location_actions,
             'meet_actions': _meet_actions,
             'questions': _questions,
             'yes': _yes,
             'no': _no,
             'next_scene': _next_scene,
             'closes': _closes}


def populate_text(text_dict):
    for category, texts in text_dict.items():
        entry = Texts(category=category, texts=texts)
        entry.save()

_character_actions = {'action': ["played a game with",
                                 "built a fort with",
                                 "went looking for berries with",
                                 "flew a kite with",
                                 "danced a jig with",
                                 "played hide and seek with",
                                 "told a funny joke to",
                                 "sung nursery rhymes with",
                                 "painted a picture of",
                                 "went for a stroll with",
                                 "had a picnic with"],
                      'reaction': ["they had a lovely time",
                                   "they had a lot of fun",
                                   "they became the best of friends",
                                   "they lost track of time",
                                   "they didn't want to stop",
                                   "they enjoyed themselves"]}

_happy_actions = {'action': ["smiled warmly at",
                             "waved happily at",
                             "grinned cheekily at",
                             "went to hug"],
                  'reaction': ["it made _charName feel very happy",
                               "_charName waved back",
                               "_charName felt safe and loved",
                               "_charName had made a new friend"]}

_angry_actions = {'action': ["roared angrily at",
                             "stared menacingly at",
                             "looked threateningly at",
                             "shouted loudly at",
                             "glared scarily at"
                             "growled at"],
                  'reaction': ["_charName did not feel very welcome",
                               "_charName ran away to hide",
                               "_charName felt quite scared",
                               "_charName looked around nervously"]}

_scared_actions = {'action': ["hid from",
                              "ran away from",
                              "looked nervously at"],
                   'reaction': [""]}

action_dict = {'character_actions': _character_actions,
               'happy_actions': _happy_actions,
               'angry_actions': _angry_actions,
               'scared_actions': _scared_actions}


def populate_action(action_dict):
    for category, dictionary in action_dict.items():
            entry = Actions(category=category, actions=dictionary['action'], reactions=dictionary['reaction'])
            entry.save()

"""Uncomment to clear the database.
Do so before making changes to model/schema to prevent MongoDB exceptions"""
# Story.objects.delete()
# Actions.objects.delete()
# Texts.objects.delete()
# Terms.objects.delete()

"""Uncomment to repopulate the database.
Make deletions first unless fresh data is being used to prevent collisions.
Story is populated when using the application so no pre-population is required"""
# populate_action(action_dict)
# populate_text(text_dict)
# populate_term(term_dict)