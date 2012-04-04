# be prepared to call this bs4
from BeautifulSoup import BeautifulSoup as soupify
import requests

class Story(object):
    def __init__(self, id):
        self.url = "http://www.literotica.com/s/%s" %(id)
        self.first_page = ""
        self.text = []
        self.title = ""
        self.author = ""
        self.category = ""
        self.description = ""

    def cache_first_page(self):
        '''
        Caches the first page of a story.

        You don't even understand how fucking useful this is.

        :raises: IOError
        '''
        r = requests.get(self.url)
        status = r.status_code // 100
        if status == 2:
            self.first_page = soupify(r.content)
        elif status == 4:
            raise IOError("Client Error %s" %(r.status_code))
        elif status == 5:
            raise IOError("Server Error %s" %(r.status_code))
        else:
            raise IOError("Unidentified Error %s" %(r.status_code))

    def fill_metadata(self):
        if not self.first_page:
            self.cache_first_page()

        # WARNING: hard coded class string
        tofind = "b-story-user-y x-r22"
        self.author = self.first_page.find('span', {'class': tofind})
        # that indexing is to get rid of a '!'
        self.author = self.author.getText()[1:]

        self.title, self.category = self.first_page.find('title')[0:1]



class Series(object):
    def __init__(self, title):
        self.title = title
        self.stories = []
        self.author = ""
