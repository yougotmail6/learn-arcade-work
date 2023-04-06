file = open("AliceInWonderLand200.txt")
file = open("dictionary.txt")
import re




for line in file:
    print(line)


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def Linear_Search():
