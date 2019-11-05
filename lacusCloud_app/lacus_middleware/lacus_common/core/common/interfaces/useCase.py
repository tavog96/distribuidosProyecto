from threading import Thread

class UseCase:

    done = False
    initialized = False
    progress = 0
    asynchronous = False
    thread = False
    response = False


    def __init__(self):
        self.done = False
        initialized = False
        progress = 0
        asynchronous = False
        response = False
        
        


    def parameters(self):
        raise NotImplementedError

    def execute(self, asynchronousParam = False):
        self.asynchronous = asynchronousParam
        self.initialized = True
        self.progress = 0
        self.done=False
        self.response=False
        if self.asynchronous:
            self.thread = Thread(target=self.task)
            self.thread.start()
        else:
            self.task()


    def task(self):
        raise NotImplementedError

    def setDone (self):
        self.initialized = True
        self.done=True
        self.progress=100
