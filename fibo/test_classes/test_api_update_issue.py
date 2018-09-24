import allure
import pytest
import requests
from support_classes.json_fixtures import *
from support_classes.jira_project_properties import *


@pytest.fixture()
def s():
    sess = requests.Session()
    sess.auth = (user_name, user_pass)
    return sess


@pytest.mark.jiraapi
@allure.step
def test_update_issue(s):
    actual_summ = "JustCreateNewIssue "+generate_summary()
    r = s.post(base_URL+create_URL,  headers=h,  data=newIssue(project_name, actual_summ, "Bug"))
    issueId = json.loads(r.text)['id']
    # update summary
    r = s.put(base_URL+create_URL + issueId, headers=h, data=updateSumm("Ughhh "+actual_summ))
    assert r.status_code == requests.codes.no_content
    r = s.get(base_URL + create_URL + issueId, headers=h)
    assert json.loads(r.text)['fields']['summary'] == "Ughhh "+actual_summ
    # update priority
    r = s.put(base_URL+create_URL + issueId, headers=h, data=updatePriority("High"))
    assert r.status_code == requests.codes.no_content
    r = s.get(base_URL + create_URL + issueId, headers=h)
    assert json.loads(r.text)['fields']['priority']['name'] == "High"
    # cleanup
    r = s.delete(base_URL + create_URL + issueId)
    assert r.status_code == requests.codes.no_content


if __name__ == '__main__':
    pytest.main()