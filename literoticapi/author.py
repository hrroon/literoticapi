import os

# be prepared to call this bs4
from BeautifulSoup import BeautifulSoup as soupify
import requests

from story import Story

class Author(object):
    def __init__(self, uid):
        try:
            int(uid)
        except ValueError:
            raise ValueError("invalid author uid '%s'" %(uid))
        self.url = "http://literotica.com/stories/memberpage.php?uid=%s" %(uid)
        self.stories = []
        self.name = ""

    def fill_metadata(self):
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

    def get_name(self):
        if not self.name:
            self.fill_metadata()

            self.name = self.p.find('a', {'class': 'contactheader'}).getText()
        return self.name

    def get_stories(self):
        if not self.stories:
            self.fill_metadata()
            
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

    def download_stories(self):
        try:
            os.mkdir(self.get_name())
        except OSError:
            pass # folder already exists
        os.chdir(self.get_name())
        self.get_stories()
        for story in self.stories:
            f = open('%s - %s.html' %(story.get_title(), story.get_category()), 'w')
            f.write('<hr />'.join(story.get_text()))
            f.close()


DEBUG = True

if __name__ == "__main__":
    if DEBUG:
        for uid in (
            868670,
            534634,
        ):
            a = Author(uid)
            a.download_stories()
