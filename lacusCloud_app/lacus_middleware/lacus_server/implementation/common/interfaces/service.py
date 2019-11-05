from threading import Thread
import time

class Service:

    done = False
    initialized = False
    thread = Thread(target=False)
    runningFlag = True
    timeWait = 1


    def start(self, timeWait):
        self.timeWait = timeWait
        self.initialized = True
        self.done=False
        self.thread = Thread(target=self.worker)
        self.thread.start()

    def stop(self):
        if (self.thread.isAlive()):
            self.runningFlag = False
            self.thread.join()
            return True
        return False

    def task (self):
        NotImplementedError

    def worker(self):
        while (self.runningFlag):
            self.task()
            time.sleep(self.timeWait)
            


    
