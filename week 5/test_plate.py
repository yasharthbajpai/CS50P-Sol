from plates import is_valid

def test_is_valid():
    assert is_valid("AB1234") == True
    assert is_valid("AB12345") == False
    assert is_valid("AB123") == True    
    assert is_valid("AB123456") == False


def test1():
    assert is_valid("cs0123") == False
    assert is_valid("cs1023") == True
    assert is_valid("css034") == False
    assert is_valid("cssr04") == False
    assert is_valid("cssr40") == True


def test2():
    assert is_valid("a") == False
    assert is_valid("ab") == True


def test3():
    assert is_valid("ab56b") == False
    assert is_valid("ab566") == True
    assert is_valid("ab6abc") == False


def test():
    assert is_valid("") == False
    assert is_valid("ab./") == False

