from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("Python") == "Pythn"

def test_shorten_empty_string():
    assert shorten("") == ""
    assert shorten("aeiou") == ""

