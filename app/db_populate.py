from app.models import *

"""
This class is used solely for initial generation of the database.
It has no purpose within the application.
"""

# names taken from top 100 baby names for boys and girls of 2014
_name = {"male": ['Muhammad', 'Oliver', 'Jack', 'Noah', 'Jacob', 'Charlie', 'Harry', 'Joshua', 'James',
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

_covering = {"fur": ["furry", "fluffy", "downy", "hairy"],
             "spines": ["spiny", "spiky", "prickly"],
             "scales": ["scaly", "armoured", "plated"]}

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

term_dict = {'name': _name,
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
        print(category)
        for name, terms in dictionary.items():
            entry = Terms(category=category, name=name, terms=terms)
            entry.save()


def populate_contribute_term(term_dict):
    for category, dictionary in term_dict.items():
        print(category)
        for name in dictionary:
            cont = ContributeTerms(category=category, name=name, terms=[])
            cont.save()

_opening = ["a long long time ago",
            "in a galaxy far far away",
            "in a far off land",
            "over the hills and far away"]

_intro = ["there was _ref_expr_hero_full",
          "there lived _ref_expr_hero_full",
          "you would find _ref_expr_hero_full",
          "you could hear stories about _ref_expr_hero_full",
          "_ref_expr_hero_full lived"]

_quest = ["One day, _ref_expr_hero_full couldn't find the _item - where might _heroGender find it?"]

_status = ["_heroName wondered if he would ever find the _item",
           "\"what if I can never find my _item?\", thought _heroName"]

_location = ["_heroName walked to the _locationDescription _location",
             "so _heroName went to the _locationDescription _location",
             "_heroName travelled to the _locationDescription _location",
             "when _heroName got to the _locationDescription _location",
             "over by the _locationDescription _location",
             "After the long walk to the _locationDescription _location",
             "at the _locationDescription _location"]

_meet = ["_heroName met _ref_expr_npc_full",
         "_heroName found _ref_expr_npc_full",
         "_ref_expr_npc_full appeared",
         "_ref_expr_npc_full was there waiting"]

_no_npc = ["_heroName looked around but couldn't find anyone",
           "_heroName was all alone"]

_no_npc_action = ["_heroName tried to look for the _item alone but it's hard without friends to help",
                  "_heroName searched around a bit for the _item but got bored",
                  "\"this is a big place to search all by myself\" thought _heroName"]

_description = ["_npcName looked very _npcEmotion to see _heroName",
                "_npcName looked _npcEmotion to see _heroName"]

_next = ["\"maybe I'll have better luck over by the _nextLocation ?\" thought _heroName",
         "\"see if the _nextLocation gives you better luck\" said _npcName"]

_end = ["_heroName was so happy to get the _item back",
        "_heroName went home to the _location with the _item"]

_question = ["\"have you seen my _item ?\" said _heroName",
             "\"Do you know where my _item is ?\" asked _heroName",
             "\"any idea where I could find my _item ?\" said _heroName"]

_non_question = ["_heroName and _npcName searched the _location together",
                 "_heroName and _npcName looked high and low"]

text_dict = {'opening': _opening,
             'intro': _intro,
             'quest': _quest,
             'status': _status,
             'location': _location,
             'meet': _meet,
             'no_npc': _no_npc,
             'no_npc_action': _no_npc_action,
             'description': _description,
             'next': _next,
             'end': _end,
             'question': _question,
             'non_question': _non_question}


def populate_text(text_dict):
    for category, texts in text_dict.items():
        print(category)
        entry = Texts(category=category, texts=texts)
        entry.save()


_character_action = {'action': ["played a game with",
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

_happy_action = {'action': ["smiled warmly at",
                            "waved happily at",
                            "grinned cheekily at",
                            "went to hug"],
                 'reaction': ["it made _heroName feel very happy",
                              "_heroName waved back",
                              "_heroName felt safe and loved",
                              "_heroName had made a new friend"]}

_angry_action = {'action': ["roared angrily at",
                            "stared menacingly at",
                            "looked threateningly at",
                            "shouted loudly at",
                            "glared scarily at"
                            "growled at"],
                 'reaction': ["_heroName did not feel very welcome",
                              "_heroName ran away to hide",
                              "_heroName felt quite scared",
                              "_heroName looked around nervously"]}

_scared_action = {'action': ["hid from",
                             "ran away from",
                             "looked nervously at"],
                  'reaction': ["_heroName wondered what he had done wrong",
                               "_heroName tried their best to comfort them",
                               "_heroName tried to look less scary"]}

action_dict = {'character_action': _character_action,
               'happy_action': _happy_action,
               'angry_action': _angry_action,
               'scared_action': _scared_action}


def populate_action(action_dict):
    for category, dictionary in action_dict.items():
        print(category)
        entry = Actions(category=category, action=dictionary['action'], reaction=dictionary['reaction'])
        entry.save()


_answer = {'yes': ["\"it's just over there\" said _npcName",
                   "\"yes I have it it in my pocket\" said _npcName",
                   "\"you're in luck, it's right here\" said _npcName"],
           'no': ["\"I'm not sure if I've seen it\" said _npcName",
                  "\"sorry but no\" said _npcName",
                  "\"I can't help with that, sorry\" said _npcName"],
           'angry_answer': ["\"it's not here, now go away!\" growled _npcName",
                            "\"i'm not going to help you\" snapped _npcName",
                            "_npcName growled back and didn't sound very friendly"]}

_non_answer = {'yes': ["there it was underneath a rock!",
                       "\"oops,\" said _heroName \"it was in my pocket all this time!\""],
               'no': ["it was a long day of searching but they couldn't find the _item anywhere",
                      "\"thanks for helping, _npcName\" said _heroName \"but I don't think it's here\"",
                      "\"No luck I'm afraid\" said _npcName"],
               'angry_answer': ["they couldn't find the _item and _npcName teased _heroName about it",
                                "\"what a waste of time that was!\" snapped _npcName",
                                "maybe if _npcName wasn't so grumpy and helped a bit more, they may have found it"]}

answer_dict = {'answer': _answer,
               'non_answer': _non_answer}


def populate_answer(answer_dict):
    for category, dictionary in answer_dict.items():
        print(category)
        for answer_type, answers in dictionary.items():
            entry = Answers(category=category, answer_type=answer_type, answers=answers)
            entry.save()


def populate_term(term_dict):
    for category, dictionary in term_dict.items():
        print(category)
        for name, terms in dictionary.items():
            entry = Terms(category=category, name=name, terms=terms)
            entry.save()


"""Uncomment to delete and repopulate the database.
Make deletions first unless fresh data is being used to prevent collisions.
Story is populated when using the application so no pre-population is required"""
Answers.objects.delete()
Story.objects.delete()
Actions.objects.delete()
Texts.objects.delete()
ContributeTerms.objects.delete()
Terms.objects.delete()
populate_answer(answer_dict)
populate_action(action_dict)
populate_text(text_dict)
populate_contribute_term(term_dict)
populate_term(term_dict)
