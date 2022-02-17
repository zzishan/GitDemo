import pytest


@pytest.mark.skip
def test_firstProgram():
    print('Hello')

def test_secondProgram():
    msg = 'Hello'
    assert msg == 'Hi', 'This failed bro'