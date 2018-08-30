import pytest
import requests
from dev_classes.phase2_API.json_fixtures import *
from dev_classes.phase2_API.properties_for_phase2 import *


@pytest.fixture()
def s():
    sess = requests.Session()
    sess.auth = (user_name, user_pass)
    return sess


def test_update_issue_summary(s):
    actual_summ = "JustCreateNewIssue "+generate_summary()
    r = s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, "Bug"))
    issueId = json.loads(r.text)['id']
    r = s.put(base_URL+create_URL + issueId, headers=h, data=updateSumm("Ughhh "+actual_summ))
    assert r.status_code == requests.codes.no_content
    r = s.get(base_URL + create_URL + issueId, headers=h)
    assert json.loads(r.text)['fields']['summary'] == "Ughhh "+actual_summ
    r = s.put(base_URL+create_URL + issueId, headers=h, data=updatePriority("High"))
    assert r.status_code == requests.codes.no_content
    r = s.get(base_URL + create_URL + issueId, headers=h)
    assert json.loads(r.text)['fields']['priority']['name'] == "High"


if __name__ == '__main__':
    pytest.main()