# be prepared to call this bs4
from BeautifulSoup import BeautifulSoup as soupify
import requests

class Author(object):
    def __init__(self, uid):
        try:
            int(uid)
        except ValueError:
            raise ValueError("invalid author uid '%s'" %(uid))
        url = "http://literotica.com/stories/memberpage.php?uid=%s" %(uid)

if __name__ == "__main__":
    a = Author("534634")

def get_story_html(story_id):
    """
    Retrieves a one-page HTML representation of a Literotica story.

    Args:
        story_id (str): The id found in the URL of a story.

    Returns:
        story_html (str): A single page of HTML with the story.

    """

    # get the damn story and init
    story_id = story_id.lower().replace(' ', '-')
    story_html = ''
    story_id = "http://www.literotica.com/s/%s" %(story_id)
    page = requests.get(story_id)

    # soupify that shit
    soup = soupify(page.content)

    # how many pages, uses a custom class name
    if 'b-pager-next' in page.content:
        # assumes the only <option> tags are the page nums
        # be ready to turn this into soup.find_all() for bs4
        pages = int(soup.findAll('option')[-1].text)
    else:
        pages = 1

    for page_num in xrange(pages):
        page = requests.get("%s?page=%s" %(story_id, page_num + 1))
        soup = soupify(page.content)
        # find the div with class 'b-story-body-x x-r15'
        # also a custom class name
        wanted_html = soup.find('div', {'class' : 'b-story-body-x x-r15'})
        # append its contents to story_html
        story_html += str(wanted_html)
        story_html += '<hr />'

    return story_html

def gen_story_ids(author_id):
    """
    Generates a list of IDs associated with an author.

    Args:
        author_id (str): An id associated with an author of Literotica.

    Returns:
        story_ids (list): A list of story ids.

    """

    url = "http://literotica.com/stories/memberpage.php?uid=%s&page=submissions" %(author_id)
    page = requests.get(url)
    soup = soupify(page.content)

    # bit of random custom code
    story_ids = soup.findAll('a', {'class' : 'bb'}) + soup.findAll('a', {'class' : 't-t84 bb nobck'})

    # the index 28 refers to removing "http://www.literotica.com/s/"
    # from the link URLs
    return list([story_id['href'][28:] for story_id in story_ids if '/p/' not in story_id['href']])

def story_to_file(story_id):
    """
    Writes the HTML of a story to a file.

    Args:
        story_id (str): Self explanatory.

    """
    file = open("%s.html" %(story_id), 'w')
    file.write(get_story_html(story_id))
    file.close()

def download_author(author_id):
    """
    Downloads every story by an author.

    Args:
        author_id (str): The ID of the author.

    """
    story_ids = gen_story_ids(author_id)

    pool = Pool(processes=10)
    pool.map(story_to_file, story_ids)

