import unittest

from literoticapi.author import *

class testStory(unittest.TestCase):

    def setUp(self):
        self.author = Author(868670)

    def testGetSeriesAndNonSeries(self):
        assert len(self.author.get_stories()) >= 132

if __name__ == "__main__":
    unittest.main()
