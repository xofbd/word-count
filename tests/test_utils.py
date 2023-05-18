import pytest

from src.utils import preprocess, filter


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hi", "hi"),
        ("HI", "hi"),
        ("hi!", "hi"),
        ("?!", None),
        ("?hi?!", "hi"),
    ]
)
def test_preprocess(word, expected):
    """
    GIVEN a word
    WHEN preprocess is called
    THEN only the cleaned up word is returned
    """

    assert preprocess(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hi", True),
        (None, False),
    ]
)
def test_filter(word, expected):
    """
    GIVEN a word
    WHEN filter is called
    THEN a truthy value is returned if it is indeed a word
    """

    assert bool(filter(word)) == expected
