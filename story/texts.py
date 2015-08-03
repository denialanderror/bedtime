import random
import re

_ref_expr = {"hero_full": random.choice(["a _charKind named _charName", "_charName the _charKind"]),
             "hero": random.choice(["_charName", "_charGender"]),
             "npc_full": random.choice(
                 ["a _locationCharKind called _locationCharName", "_locationCharName the _locationCharKind"]),
             "npc": random.choice(["the _locationCharKind", "_locationCharName"])
             }

_openings = ["a long long time ago",
             "in a galaxy far far away",
             "beyond the deep, dark forest",
             "in a far off land",
             "over the hills and far away"]

_intro = ["there was " + _ref_expr["hero_full"],
          "there lived " + _ref_expr["hero_full"],
          "you would find " + _ref_expr["hero_full"],
          "you could hear stories about " + _ref_expr["hero_full"],
          _ref_expr["hero_full"] + " lived"]

_location_actions = ["_charName walked to the _charLocation",
                     "so _charName went to the _charLocation",
                     "_charName travelled to the _charLocation",
                     "when _charName got to the _charLocation",
                     "over by the _charLocation",
                     "After the long walk to the _charLocation",
                     "at the _charLocation"]

_meet_actions = ["_charName met " + _ref_expr["npc_full"],
                 "_charName found " + _ref_expr["npc_full"],
                 _ref_expr["npc_full"] + " appeared",
                 _ref_expr["npc_full"] + " was there waiting",
                 ]

_character_actions = ["played a game",
                      "built a fort",
                      "went looking for berries",
                      "flew a kite",
                      "danced a jig",
                      "played hide and seek",
                      "told funny jokes",
                      "sung nursery rhymes",
                      "painted pretty pictures",
                      "went for a stroll",
                      "ate some tasty snacks",
                      "had a picnic"]

_questions = ["\"have you seen my _questItem ?\" said _charName",
              "\"Do you know where my _questItem is ?\" asked _charName",
              "\"any idea where I could find my _questItem ?\" said _charName"]

_yes = ["\"it's just over there\" said _locationCharName",
        "\"yes I have it it in my pocket\" said _locationCharName"]

_no = ["\"I'm not sure what you are talking about\" said _locationCharName",
       "\"sorry but no\" said _locationCharName"]

_next_scene = ["\"have you tried the _nextLocation ?\"",
               "\"try over there by the _nextLocation\""]

_closes = ["_charName was so happy to get the _questItem back",
           "_charName went home to the _charLocation with the _questItem"]

_test = ['this is a normal sentence', 'this is another']  # for test purposes only, to avoid issues with random.choice


def phrase(expression):
    """Returns a list representation of a randomised string from the requested
    expression type, using regex to maintain separation of punctuation within
    the lists"""
    switch = {"openings": random.choice(_openings),
              "intro": random.choice(_intro),
              "location_actions": random.choice(_location_actions),
              "meet_actions": random.choice(_meet_actions),
              "character_actions":
                  _ref_expr["hero"] + " " + random.choice(_character_actions) + " with " + _ref_expr["npc"],
              "creature_actions":
                  _ref_expr["npc"] + " " + random.choice(_character_actions) + " with " + _ref_expr["hero"],
              "questions": random.choice(_questions),
              "yes": random.choice(_yes),
              "no": random.choice(_no),
              "next_scene": random.choice(_next_scene),
              "closes": random.choice(_closes),
              "test": _test[0]
              }
    return re.findall(r"[\w']+|[-.,!?;:\"]", str(switch[expression]).strip())
