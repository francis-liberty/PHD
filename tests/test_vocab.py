import unittest
import os

import parser.srt as psrt
import nlp.vocab as vocab


class TestVocab(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse(self):
        dr = os.path.dirname(__file__)
        file_path = os.path.join(dr, '../data/test.srt')
        texts = psrt.parse(file_path)
        print texts

        sents, vb = vocab.make(texts)
        print sents
        print vb
