from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hello" == more_hello()


def test_more_goodbye():
    assert "hi" == more_goodbye()
