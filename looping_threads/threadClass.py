import threading
import Queue

q = Queue.Queue()

class listener(object):
    def __init__(self):
        thread = threading.Thread(target=self.loop)
        # thread.daemon = True
        thread.start()

    def loop(self):
        for i in xrange(0,13):
            q.put(i)

class ui(object):
    def __init__(self):
        listener()
        while True:
            item = q.get()
            print item
            if item == 10:
                break

ui()