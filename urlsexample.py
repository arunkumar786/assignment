import threading
import urllib2
import time

start = time.time()
urls = ["http://www.google.com", "http://www.apple.com", "http://www.oracle.com", "http://www.amazon.com", "http://www.facebook.com"]

class FetchUrl(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        urlHandler = urllib2.urlopen(self.url)
        html = urlHandler.read()
        print "'%s\' fetched in %ss and status code is %s" % (self.url,(time.time() - start), urlHandler.getcode())

for url in urls:
    FetchUrl(url).start()

#Join all existing threads to main thread.
for thread in threading.enumerate():
    if thread is not threading.currentThread():
        thread.join()

print "Elapsed Time: %s" % (time.time() - start)
