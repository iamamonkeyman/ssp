import allure

from support_classes.jira_project_properties import *
from pyquery import PyQuery
import pytest
import requests


@pytest.mark.parametrize("actual, expected", [
    ((user_name, "i'm_not_correct", 'h1'),      (requests.codes.unauthorized,"Unauthorized (401)")),
    (("i'm_not_correct", user_pass, 'h1'),      (requests.codes.unauthorized,"Unauthorized (401)")),
    ((user_name, user_pass, '#content h1'),     (requests.codes.ok,          "System Dashboard"))
])


@pytest.mark.jiraapi
@allure.step
def test_try_to_login(actual, expected):
    r = requests.get(base_URL, auth=(actual[0], actual[1]));
    pq = PyQuery(r.text)
    assert r.status_code == expected[0]
    assert pq(actual[2]).text() == expected[1]


if __name__ == '__main__':
    pytest.main()
