import time
from math import sin, cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_cos_dot_string(x):
    return '>' * int(10 * cos(radians(x)) + 20) + '0'

def make_sin_dot_string(x):
    return '<' * int(10 * sin(radians(x)) + 20) + '1'


for i in range(0, 3600, 18):
    print(make_cos_dot_string(i))
    print(make_sin_dot_string(i))
    time.sleep(0.05)