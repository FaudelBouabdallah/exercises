list = ["1234", "12", "123456", "1", "1234"]
def nth_longest_string(n, strings):
    sorted_strings = sorted(strings, key=len)
    return sorted_strings[-n]