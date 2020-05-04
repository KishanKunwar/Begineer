import time
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(1)


obj1 = Hello()
obj2 = Hi()
obj1.start()
time.sleep(.2)
obj2.start()

obj1.join()
obj2.join()


print("bye")