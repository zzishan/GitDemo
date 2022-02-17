import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param




@pytest.fixture()
def dataLoad():
    print("User profile data has been created")
    return ["Zishan","Ali","google.com"]