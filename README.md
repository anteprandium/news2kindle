# Send your RSS news to your Kindle

`news2kindle` is a little Python script, based on code from `https://gist.github.com/alexwlchan/01cec115a6f51d35ab26` will read a list of RSS news, package them as a MOBI file, and then send it to your kindle via kindle mail address and Amazon's whispersync. 

This script is intended for “know-how” users, if any of the above puzzles you, you're probably not the intended audience.


*Caveat*: If your MOBI file gets bigger than 25MB (easy if  you have a lot of RSS sources), amazon will refuse to whispersync to your device. Can't do anything about it.

## Under the hood

This is a simple Python script that will download all your RSS news, package them as an EPUB first using `pandoc`, and then generate a Kindle file from that. This is a very roundabout way to do things, but it turned out to give the best results.

The RSS feeds are listed in a file called `feeds.txt`, one per line. The modification date of `feeds.txt` will be the starting date from which news are downloaded.

Then, it will sleep for twelve hours (adjustable) and do it all over again. The idea is to leave the script running in some server, and comfortably have your news delivered to your Kindle, once in the morning, ready for your breakfast news;  and once in the evening, while you seep your tea (or other hot beverage.)


## Installation
Also, you'll need several things for this to work:

* From the Python side:
    * `pytz`,
    * `pypandoc`, and 
    * `feedparser`.
    
(You can `pip install` all of these. Actually, you can just install them under the directory where you will store this script, with `pip install -t . pytz pypandoc feedparser` and be done with it.)

* Programs:
    * [`pandoc`](http://pandoc.org), if not bundled with `pypandoc` above, and
    * [`kindlegen`](https://www.amazon.com/gp/feature.html?docId=1000765211).
    
then, configure the first part of the file with appropriate mail server, user, password, fee file and paths. Finaly, just run the script.

Good luck.