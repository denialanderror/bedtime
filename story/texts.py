import random
import re

_openings = ["once upon a time",
            "a long long time ago",
            "in a galaxy far far away",
            "way way back",
            "over the hills and far away"]

_intro = ["there lived a _charKind named _charName"]

_location_actions = ["_charName walked to the _charLocation",
                    "_charName went to the _charLocation",
                    "_charName travelled to the _charLocation"]

_meet_actions = ["_charName met a _locationCharKind called _locationCharName",
                "_charName met _locationCharName the _locationCharKind",
                "_charName found a _locationCharKind called _locationCharName"]

_character_actions = ["_charName played a game with the _locationCharKind",
                     "_charName built a fort with the _locationCharKind",
                     "_charName went looking for berries with the _locationCharKind",
                     "_charName flew a kite with the _locationCharKind",
                     "_charName danced a jig with the _locationCharKind",
                     "_charName played hide and seek with the _locationCharKind",
                     "_charName told funny jokes with the _locationCharKind",
                     "_charName sung nursery rhymes with the _locationCharKind",
                     "_charName painted pretty pictures with the _locationCharKind",
                     "_charName went for a stroll with the _locationCharKind",
                     "_charName ate some tasty snacks with the _locationCharKind",
                     "_charName had a picnic with the _locationCharKind"]

_questions = ["\"have you seen my _questItem ?\" said _charName",
             "\"Do you know where my _questItem is ?\" asked _charName",
             "\"any idea where I could find my _questItem ?\" said _charName"]

_yes = ["\"it's just over there\" said _locationCharName",
       "\"yes I have it it in my pocket\" said _locationCharName"]

_no = ["\"I'm not sure what you are talking about\" said _locationCharName",
      "\"sorry but no\" said _locationCharName"]

_next_scene = ["\"have you tried the _charLocation ?\"",
              "\"try over there by the _charLocation\""]

_closes = ["_charName was so happy to get the _questItem back",
          "_charName went home to the _charLocation with the _questItem"]

def openings():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_openings))

def intro():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_intro))

def location_actions():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_location_actions))

def meet_actions():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_meet_actions))

def character_actions():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_character_actions))

def questions():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_questions))

def yes():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_yes))

def no():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_no))

def next_scene():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_next_scene))

def closes():
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(_closes))
