import time

t=time.time()

while True:
    if t+5==time.time():
        print(5)
        t=time.time()
