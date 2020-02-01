some_lock = threading.Lock()

#harmful:
some_lock.acquire()
try:
    #do something
finally:
    some_lock.release()

#Better:

with some_lock:
    #do something