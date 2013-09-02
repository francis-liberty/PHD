import unittest
import os

import parser.srt as psrt


class TestSRT(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse(self):
        dr = os.path.dirname(__file__)
        file_path = os.path.join(dr, '../data/test.srt')
        texts = psrt.parse(file_path)
        print texts
