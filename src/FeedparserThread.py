import pytz
import time
from datetime import datetime, timedelta
import collections
import threading
import feedparser


Post = collections.namedtuple('Post', [
    'time',
    'blog',
    'title',
    'author',
    'link',
    'body'
])


class FeedparserThread(threading.Thread):
    """
    Each one of these threads will get the task of opening one feed
    and process its entries.

    Given an url, starting time and a global list, this thread will
    add new posts to the global list, after processing.

    """

    def __init__(self, url, START, posts):
        threading.Thread.__init__(self)
        self.url = url
        self.START = START
        self.posts = posts
        self.myposts = []

    def run(self):
        feed = feedparser.parse(self.url)
        try:
            blog = feed['feed']['title']
        except KeyError:
            blog = "---"
        for entry in feed['entries']:
            post = process_entry(entry, blog, self.START)
            if post:
                self.myposts.append(post)
        self.myposts.sort()
        self.posts += self.myposts


def process_entry(entry, blog, START):
    """
    Coerces an entry from feedparser into a Post tuple.
    Returns None if the entry should be excluded.

    If it was published before START date, drop the entry.
    """
    try:
        when = entry['updated_parsed']
    except KeyError:
        try:
            when = entry['published_parsed']
        except KeyError:
            return  # Ignore undateable posts

    if when:
        when = pytz.utc.localize(datetime.fromtimestamp(time.mktime(when)))
    else:
        # print blog, entry
        return

    if when < START:
        return

    title = entry.get('title', "Null")

    try:
        author = entry['author']
    except KeyError:
        try:
            author = ', '.join(a['name'] for a in entry.get('authors', []))
        except KeyError:
            author = 'Anonymous'

    link = entry['link']

    try:
        body = entry['content'][0]['value']
    except KeyError:
        body = entry['summary']

    return Post(when, blog, title, author, link, body)
