import unittest
from app import app
from story import creature, writer, texts, location
from app.models import Terms
import random


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_an(self):
        realised = ["a", "noun", "a", "antelope", "a", "a", "real", "a", "eritrean"]
        for index, word in enumerate(realised):
            if word == 'a' and realised[index + 1][0] in ['a', 'e', 'i', 'o', 'u']:
                realised[index] = "an"
        self.assertSequenceEqual(realised, ["a", "noun", "an", "antelope", "an", "a", "real", "an", "eritrean"])

    """character create test cases"""

    def test_Creature1(self):
        c = creature.Creature()
        gender_bender = {"he": "male", "she": "female"}
        gender = gender_bender[c.gender]
        self.assertIn(c.gender, ["he", "she"],
                      "blank creature gender create failed")
        self.assertIn(c.name, Terms.objects(name=gender).distinct('terms'),
                      "blank creature name create failed")
        self.assertIn(c.kind, Terms.objects(category='kind').distinct('terms'),
                      "blank creature kind create failed")
        self.assertIn(c._colour[0], Terms.objects(category='colour').distinct('terms'),
                      "blank creature colour a create failed")
        self.assertIn(c._colour[1], Terms.objects(category='colour').distinct('terms'),
                      "blank creature colour b create failed")
        self.assertIn(c._pattern, Terms.objects(category='pattern').distinct('terms'),
                      "blank creature pattern create failed")
        self.assertIn(c._size, Terms.objects(category='size').distinct('terms'),
                      "blank creature size create failed")
        self.assertIn(c._covering, Terms.objects(category='covering').distinct('terms'),
                      "blank creature covering create failed")
        self.assertIn(c._emotion, Terms.objects(category='emotion').distinct('terms'),
                      "blank creature emotion create failed")

    def test_Creature2(self):
        c = creature.Creature(gender="elamef")
        self.assertIn(c.gender, ["he", "she"], "incorrect gender create failed")

    def test_Creature3(self):
        c = creature.Creature()
        if c._pattern == 'plain':
            self.assertEqual(c.colour_mixer, c._colour[0], "creature colour mixer plain failed")
        else:
            self.assertEqual(c.colour_mixer, "{0} and {1} {2}".format(c._colour[0], c._colour[1], c._pattern),
                             "creature colour mixer patterned failed")

    def test_Creature4(self):
        c = creature.Creature()
        # expands lists of terms into a flat list, in order to make the In assertion
        choices = [item for sublist in
                   [c.colour_mixer.split(), Terms.objects(category='size', name=c._size).distinct('terms'),
                    Terms.objects(category='emotion', name=c._emotion).distinct('terms'),
                    Terms.objects(category='covering', name=c._covering).distinct('terms')] for item in sublist]
        result = c.description().split()
        if not result:
            self.assertEqual("", "", "creature description empty failed")
        else:
            self.assertIn(result[0], choices, "creature description single return failed")
            if len(result) > 1:
                self.assertIn(result[2], choices, "creature description multiple returns failed")

    """location create test cases"""

    def test_Location1(self):
        l = location.Location()
        self.assertIn(l.location, Terms.objects(category='location').distinct('terms'),
                      "blank location name create failed")
        self.assertIn(l.colour, Terms.objects(category='colour').distinct('terms'),
                      "location colour create failed")
        self.assertIn(l.size, Terms.objects(category='size').distinct('terms'),
                      "location size create failed")
        self.assertIn(l.mood, Terms.objects(category='mood').distinct('terms'),
                      "location mood create failed")
        self.assertIsInstance(l.character, creature.Creature, "location unnamed character create failed")

    def test_Location2(self):
        c = creature.Creature("Fred", "frog", "male")
        l = location.Location(c)
        self.assertEqual(l.character.name, c.name, "character-specified location create failed")

    def test_Location3(self):
        l = location.Location()
        # expands lists of terms into a flat list, in order to make the In assertion
        choices = [item for sublist in
                   [[l.colour], Terms.objects(category='size', name=l._size).distinct('terms'),
                    Terms.objects(category='mood', name=l._mood).distinct('terms')] for item in sublist]
        result = l.description().split()
        if not result:
            self.assertEqual("", "", "location description empty failed")
        else:
            self.assertIn(result[0], choices, "location description single return failed")
            if len(result) > 1:
                self.assertIn(result[2], choices, "location description multiple returns failed")

    """texts test cases"""
    # phrase tests
    def test_phrase1(self):
        result = texts.phrase("test")
        self.assertEqual(result, ["this", "is", "a", "normal", "sentence"], "standard get phrase failed")

    def test_phrase2(self):
        texts._test[0] = ""
        result = texts.phrase("test")
        self.assertEqual(result, [], "empty get phrase failed")

    def test_phrase3(self):
        texts._test[0] = "let's keep punctuation like: -!?\""
        result = texts.phrase("test")
        self.assertEqual(result, ["let's", "keep", "punctuation", "like", ":", "-", "!", "?", '"'],
                         "punctuation get phrase failed")

    """writer test cases"""

    # aggregation tests
    def test_aggregation1(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        s1 = ["john", "likes", "cats"]
        s2 = ["he", "hates", "dogs"]
        result = w.aggregation(s1, s2)
        self.assertSequenceEqual(result, ["john", "likes", "cats", ",", "he", "hates", "dogs"],
                                 "comma aggregation failed")

    def test_aggregation2(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        s1 = ["john", "likes", "cats"]
        s2 = ["john", "hates", "dogs"]
        result = w.aggregation(s1, s2)
        if "_charGender" in result:
            self.assertSequenceEqual(result,
                                     ["john", "likes", "cats", "and", "there", "_charGender", "hates", "dogs"],
                                     "referring expression aggregation failed")
        else:
            self.assertSequenceEqual(result,
                                     ["john", "likes", "cats", "and", "hates", "dogs"],
                                     "referring expression aggregation failed")

    def test_aggregation3(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        s1 = ["john", "likes", "cats"]
        s2 = ["John", "hates", "dogs"]
        result = w.aggregation(s1, s2)
        if "_charGender" in result:
            self.assertSequenceEqual(result,
                                     ["john", "likes", "cats", "and", "there", "_charGender", "hates", "dogs"],
                                     "capitalisation anomaly aggregation failed")
        else:
            self.assertSequenceEqual(result,
                                     ["john", "likes", "cats", "and", "hates", "dogs"],
                                     "capitalisation anomaly aggregation failed")

    def test_aggregation4(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        s1 = ["john", "john", "john"]
        s2 = ["john", "john", "john"]
        result = w.aggregation(s1, s2)
        if "_charGender" in result:
            self.assertSequenceEqual(result,
                                     ["john", "john", "john", "and", "there", "_charGender", "john", "john"],
                                     "multiple character name aggregation failed")
        else:
            self.assertSequenceEqual(result,
                                     ["john", "john", "john", "and", "john", "john"],
                                     "multiple character name aggregation failed")

    def test_aggregation5(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        s1 = []
        s2 = []
        result = w.aggregation(s1, s2)
        self.assertSequenceEqual(result, [],
                                 "empty list aggregation failed")

    # realise tests
    def test_realise1(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = ["john", "likes", "cats"]
        result = w.realise(sentence)
        self.assertEqual(result, "John likes cats.", "standard realisation failed")

    def test_realise2(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = ["_charName", "likes", "cats"]
        result = w.realise(sentence)
        self.assertEqual(result, "John likes cats.", "substitution realisation failed")

    def test_realise3(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = []
        result = w.realise(sentence)
        self.assertSequenceEqual(result, [], "empty list realisation failed")

    def test_realise4(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = ["_charName", "+", "cats", "=", "heaven"]
        result = w.realise(sentence)
        self.assertEqual(result, "John + cats = heaven.", "centre punctuation realisation failed")

    def test_realise5(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = ["?", "this", "should", "be", "capitalised"]
        result = w.realise(sentence)
        self.assertEqual(result, "?This should be capitalised.", "beginning capitalisation realisation failed")

    def test_realise6(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        sentence = ["should", "this", "have", "a", "full", "stop", "?"]
        result = w.realise(sentence)
        self.assertEqual(result, "Should this have a full stop?", "terminal punctuation realisation failed")

    def test_realise6(self):
        w = writer.Writer(name="john boy", kind="pony", gender="male", quest="hat")
        sentence = ["_charName", "!"]
        result = w.realise(sentence)
        self.assertEqual(result, "John Boy!", "double word name realisation failed")

    # descriptions tests
    def test_descriptions(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")

    # scene tests
    def test_scene1(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        w.story_index = len(w.locations)
        self.assertEqual(w.story_index, 0, "story index mod scene fail")

    def test_scene2(self):
        w = writer.Writer(name="john", kind="pony", gender="male", quest="hat")
        w.story_index = len(w.locations) - 1
        w.scene()
        self.assertTrue(w.end, "story end scene fail")

    """flask test cases"""


if __name__ == "__main__":
    unittest.main()
