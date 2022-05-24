# Write your code here
from itertools import count


def countdown(n):
    return ", ".join([str(i) for i in range(n, 0, -1)])