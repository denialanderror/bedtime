import random
from app.models import Texts, Actions
import re

_test = ['this is a normal sentence']  # for test purposes only, to avoid issues with random.choice
_openings = random.choice(Texts.objects(category='openings').distinct('texts'))


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
                      Actions.objects(category='character_actions').distinct('actions')) + " with _ref_expr_npc",
              "npc_actions":
                  "_ref_expr_npc" + " " + random.choice(
                      Actions.objects(category='character_actions').distinct('actions')) + " with _ref_expr_hero",
              "questions": random.choice(Texts.objects(category='questions').distinct('texts')),
              "yes": random.choice(Texts.objects(category='yes').distinct('texts')),
              "no": random.choice(Texts.objects(category='no').distinct('texts')),
              "next_scene": random.choice(Texts.objects(category='next_scene').distinct('texts')),
              "closes": random.choice(Texts.objects(category='closes').distinct('texts')),
              "test": _test[0]
              }
    return re.findall(r"[\w']+|[-.,!?;:\"\[\]]", str(switch[expression]).strip())
