import pytest
import requests
from dev_classes.phase2_API.json_fixtures import *
from dev_classes.phase2_API.properties_for_phase2 import *


@pytest.fixture()
def s():
    sess = requests.Session()
    sess.auth = (user_name, user_pass)
    return sess


def test_find_one_issue(s):
    actual_summ = "JustCreateNewIssue "+generate_summary()
    s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, "Bug"))
    r = s.get(base_URL+search_URL+"summary~'"+actual_summ+"'",  headers=h)
    assert json.loads(r.text)['total']== 1
    assert json.loads(r.text)['issues'][0]['fields']['summary']==actual_summ


def test_find_five_issues(s):
    for i in range(1):
        actual_summ = "JustCreateNewIssue "+generate_summary()
        s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, "Bug"))
    r = s.get(base_URL+search_URL+"summary~JustCreateNewIssue&maxResults=5",  headers=h)
    assert json.loads(r.text)['total'] > 5
    assert json.loads(r.text)['maxResults'] == 5


def test_find_no_results(s):
    r = s.get(base_URL + search_URL + "summary~there_is_no_spoon", headers=h)
    assert json.loads(r.text)['total'] == 0


if __name__ == '__main__':
    pytest.main()