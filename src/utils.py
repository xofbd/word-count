import re


def preprocess(word):
    try:
        re.search(r"([a-z]+)" word.lower()).group(1)
    except AttributeError:
        return None


def filter(word):
    return word
