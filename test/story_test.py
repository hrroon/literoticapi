import unittest

from literoticapi.story import *

class testStory(unittest.TestCase):

    def setUp(self):
        self.story = Story('e-beth-ch-01')

    def testGetAuthor(self):
        assert self.story.get_author() == 'bluedragonauthor'

    def testGetTitle(self):
        assert self.story.get_title() == "E-Beth Ch. 01"

    def testGetCategory(self):
        assert self.story.get_category() == "Group Sex"

    def testGetDescription(self):
        assert self.story.get_description() == "E-Beth from 'The Book of David' searches for happiness."

    def testGetNumPages(self):
        assert self.story.get_num_pages() == 7

    def testGetText(self):
        print self.story.get_text()[-1]

if __name__ == "__main__":
    unittest.main()
