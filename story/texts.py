import random
import re

_ref_expr = {"hero_full": random.choice(["a _charKind named _charName", "_charName the _charKind"]),
             "hero": random.choice(["_charName", "_charGender"]),
             "npc_full": random.choice(
                 ["a _locationCharKind called _locationCharName", "_locationCharName the _locationCharKind"]),
             "npc": random.choice(["the _locationCharKind", "_locationCharName"])
             }

openings = ["a long long time ago",
            "in a galaxy far far away",
            "beyond the dark, dark forest",
            "in a far off land",
            "over the hills and far away"]

intro = ["there was a _charKind named _charName",
         "there lived " + _ref_expr["hero_full"],
         _ref_expr["hero_full"] + " lived"]

location_actions = ["_charName walked to the _charLocation",
                    "So _charName went to the _charLocation",
                    "_charName travelled to the _charLocation",
                    "over by the _charLocation",
                    "at the _charLocation"]

meet_actions = ["_charName met " + _ref_expr["npc_full"],
                "_charName found " + _ref_expr["npc_full"],
                ]

character_actions = [_ref_expr["hero"] + " played a game with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " built a fort with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " went looking for berries with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " flew a kite with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " danced a jig with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " played hide and seek with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " told funny jokes with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " sung nursery rhymes with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " painted pretty pictures with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " went for a stroll with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " ate some tasty snacks with " + _ref_expr["npc"],
                     _ref_expr["hero"] + " had a picnic with " + _ref_expr["npc"]]

questions = ["\"have you seen my _questItem ?\" said _charName",
             "\"Do you know where my _questItem is ?\" asked _charName",
             "\"any idea where I could find my _questItem ?\" said _charName"]

yes = ["\"it's just over there\" said _locationCharName",
       "\"yes I have it it in my pocket\" said _locationCharName"]

no = ["\"I'm not sure what you are talking about\" said _locationCharName",
      "\"sorry but no\" said _locationCharName"]

next_scene = ["\"have you tried the _nextLocation ?\"",
              "\"try over there by the _nextLocation\""]

closes = ["_charName was so happy to get the _questItem back",
          "_charName went home to the _charLocation with the _questItem"]


def phrase(expression):
    switch = {"openings": openings,
              "intro": intro,
              "location_actions": location_actions,
              "meet_actions": meet_actions,
              "character_actions": character_actions,
              "questions": questions,
              "yes": yes,
              "no": no,
              "next_scene": next_scene,
              "closes": closes,
              }
    return re.findall(r"[\w']+|[.,!?;\"]", random.choice(switch[expression]))
