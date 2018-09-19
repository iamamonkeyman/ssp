import allure
import pytest
d=0


@pytest.mark.jiraapi
@allure.step
@pytest.mark.flaky(reruns=1)
def test_11():
    global d
    while (d!=1):
        d+=1
        assert False
    assert True