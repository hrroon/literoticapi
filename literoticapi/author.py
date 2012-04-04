# be prepared to call this bs4
from BeautifulSoup import BeautifulSoup as soupify
import requests

from .story import Story

class Author(object):
    def __init__(self, uid):
        try:
            int(uid)
        except ValueError:
            raise ValueError("invalid author uid '%s'" %(uid))
        self.url = "http://literotica.com/stories/memberpage.php?uid=%s" %(uid)
        self.stories = []

    def get_stories(self):
        if not self.stories:
            r = requests.get("%s&page=submissions" %(self.url))
            status = r.status_code // 100
            if status == 2:
                self.p = soupify(r.content)
            elif status == 4:
                raise IOError("Client Error %s" %(r.status_code))
            elif status == 5:
                raise IOError("Server Error %s" %(r.status_code))
            else:
                raise IOError("Unidentified Error %s" %(r.status_code))
            
            # WARNING: hard coded class names
            tofind1, tofind2 = 'bb', 't-t84 bb nobck'
            self.stories = self.p.findAll('a', {'class': tofind1})
            self.stories += self.p.findAll('a', {'class': tofind2})
            self.stories = [x['href'][28:] for x in self.stories]
            self.stories = [Story(story_id) for story_id in self.stories]
        return self.stories

    def list_stories(self):
        if not self.stories:
            self.get_stories()
        for story in self.stories:
            print story.get_title()
