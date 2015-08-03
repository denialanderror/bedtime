import unittest
from app import app
from story import writer
from story import texts


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

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
        self.assertEqual(result, "John boy!", "double word name realisation failed")

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
        w.story_index = len(w.locations) -1
        w.scene()
        self.assertTrue(w.end, "story end scene fail")

    """flask test cases"""

if __name__ == "__main__":
    unittest.main()
