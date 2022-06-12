import sys
import re


def remove_comments(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = re.sub('#.*$', '', content, flags=re.MULTILINE)

    with open(filename, 'w') as file:
        file.write(content)

for file in sys.argv[1:]:
    remove_comments(file)