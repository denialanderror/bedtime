import random
from app.models import Texts
import re

# _ref_expr = {"hero_full": random.choice(["a _charDescription _charKind named _charName",
#                                          "_charName the _charDescription _charKind"]),
#              "hero": random.choice(["_charName", "_charGender"]),
#              "npc_full": random.choice(
#                  ["a _npcDescription _npcKind called _npcName", "_npcName the _npcDescription _npcKind"]),
#              "npc": random.choice(["the _npcKind", "_npcName", "the _npcDescription _npcKind"])
#              }
#
# _openings = ["a long long time ago",
#              "in a galaxy far far away",
#              "in a far off land",
#              "over the hills and far away"]
#
# _intro = ["there was " + _ref_expr["hero_full"],
#           "there lived " + _ref_expr["hero_full"],
#           "you would find " + _ref_expr["hero_full"],
#           "you could hear stories about " + _ref_expr["hero_full"],
#           _ref_expr["hero_full"] + " lived"]
#
# _location_actions = ["_charName walked to the _locationDescription _location",
#                      "so _charName went to the _locationDescription _location",
#                      "_charName travelled to the _locationDescription _location",
#                      "when _charName got to the _locationDescription _location",
#                      "over by the _locationDescription _location",
#                      "After the long walk to the _locationDescription _location",
#                      "at the _locationDescription _location"]
#
# _meet_actions = ["_charName met " + _ref_expr["npc_full"],
#                  "_charName found " + _ref_expr["npc_full"],
#                  _ref_expr["npc_full"] + " appeared",
#                  _ref_expr["npc_full"] + " was there waiting"]
#
# _character_actions = ["played a game",
#                       "built a fort",
#                       "went looking for berries",
#                       "flew a kite",
#                       "danced a jig",
#                       "played hide and seek",
#                       "told funny jokes",
#                       "sung nursery rhymes",
#                       "painted pretty pictures",
#                       "went for a stroll",
#                       "ate some tasty snacks",
#                       "had a picnic"]
#
# _questions = ["\"have you seen my _questItem ?\" said _charName",
#               "\"Do you know where my _questItem is ?\" asked _charName",
#               "\"any idea where I could find my _questItem ?\" said _charName"]
#
# _yes = ["\"it's just over there\" said _npcName",
#         "\"yes I have it it in my pocket\" said _npcName"]
#
# _no = ["\"I'm not sure what you are talking about\" said _npcName",
#        "\"sorry but no\" said _npcName"]
#
# _next_scene = ["\"have you tried the _nextLocation ?\"",
#                "\"try over there by the _nextLocation\""]
#
# _closes = ["_charName was so happy to get the _questItem back",
#            "_charName went home to the _location with the _questItem"]

_test = ['this is a normal sentence']  # for test purposes only, to avoid issues with random.choice


def phrase(expression):
    """Returns a list representation of a randomised string from the requested
    expression type, using regex to maintain separation of punctuation within
    the lists"""
    switch = {"openings": random.choice(Texts.objects(category='openings').distinct('texts')),
              "intro": random.choice(Texts.objects(category='intro').distinct('texts')),
              "location_actions": random.choice(Texts.objects(category='location_actions').distinct('texts')),
              "meet_actions": random.choice(Texts.objects(category='meet_actions').distinct('texts')),
              "character_actions":
                  "_ref_expr_hero " + random.choice(
                      Texts.objects(category='character_actions').distinct('texts')) + " with _ref_expr_npc",
              "creature_actions":
                  "_ref_expr_npc" + " " + random.choice(
                      Texts.objects(category='character_actions').distinct('texts')) + " with _ref_expr_hero",
              "questions": random.choice(Texts.objects(category='questions').distinct('texts')),
              "yes": random.choice(Texts.objects(category='yes').distinct('texts')),
              "no": random.choice(Texts.objects(category='no').distinct('texts')),
              "next_scene": random.choice(Texts.objects(category='next_scene').distinct('texts')),
              "closes": random.choice(Texts.objects(category='closes').distinct('texts')),
              "test": _test[0]
              }
    return re.findall(r"[\w']+|[-.,!?;:\"\[\]]", str(switch[expression]).strip())
