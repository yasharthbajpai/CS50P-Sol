from bank import value




def test_value_with_numbers():
   assert value("hello")== "0$"


def test_value_with_string():
    assert value("hello") == "0$"
    assert value("hello World") == "20$"
    assert value("hello World!") == "20$"
  
def test_string():
    assert value("hi") == "20$"
    assert value("hulli") == "20$"

def test_string_with_numbers():
    assert value("tmkc") == "100$"
    assert value("tmkc123") == "100$"


