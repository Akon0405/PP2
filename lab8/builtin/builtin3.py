import math
import time

num = int(input())
times = int(input())
time.sleep(times/1000.0)
print('Square root of', num, 'after', times, 'miliseconds is', math.sqrt(num))
