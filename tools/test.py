from tools.decorators import timing
import time

@timing
def for_loop(n):
    for i in range(n):
        time.sleep(0.2)
        print(i)

for_loop(20)