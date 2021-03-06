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
def test_find_one_issue(s):
    actual_summ = "JustCreateNewIssue "+generate_summary()
    r=s.post(base_URL+create_URL,  headers=h,  data=newIssue(project_name, actual_summ, "Bug"))
    id=json.loads(r.text)['id']
    r = s.get(base_URL+search_URL+"summary~'"+actual_summ+"'",  headers=h)
    assert json.loads(r.text)['total'] == 1
    assert json.loads(r.text)['issues'][0]['fields']['summary']==actual_summ
    r = s.delete(base_URL + create_URL + id)
    assert r.status_code == requests.codes.no_content


@pytest.mark.jiraapi
@allure.step
def test_find_five_issues(s):
    ids=[]
    for i in range(6):
        actual_summ = "JustCreateNewIssue "+generate_summary()
        r=s.post(base_URL+create_URL,  headers=h,  data=newIssue(project_name, actual_summ, "Bug"))
        ids.append(json.loads(r.text)['id'])
    r = s.get(base_URL+search_URL+"summary~JustCreateNewIssue&maxResults=5",  headers=h)
    assert json.loads(r.text)['total'] > 5
    assert json.loads(r.text)['maxResults'] == 5
    for j in ids:
        r = s.delete(base_URL + create_URL + j)
        assert r.status_code == requests.codes.no_content



@pytest.mark.jiraapi
@allure.step
def test_find_no_results(s):
    r = s.get(base_URL + search_URL + "summary~there_is_no_spoon", headers=h)
    assert json.loads(r.text)['total'] == 0


if __name__ == '__main__':
    pytest.main()