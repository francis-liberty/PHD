import unittest
import os

import srt as psrt


class TestSRT(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse(self):
        dr = os.path.dirname(__file__)
        file_path = os.path.join(dr, '../../data/test.srt')
        sents = psrt.parse(file_path)
        print('.\n'.join(sents[:10]))
