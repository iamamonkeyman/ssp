import allure
import pytest
import requests
from support_classes.jira_pages import LoginPO
from support_classes.projectWd import ProjectWD
from support_classes.json_fixtures import *
from support_classes.jira_project_properties import *


@pytest.fixture(scope=pytestScope)
def wd_fixture():
    dr = ProjectWD()
    yield dr
    dr.closeWD()


@pytest.fixture(scope=pytestScope)
def loginToJira(wd_fixture):
    loginP = LoginPO(wd_fixture.getWD())
    mainP = loginP.loginToJira(user_name, user_pass)
    yield mainP


@pytest.fixture(scope=pytestScope)
def prepareOneIssue():
    s = requests.Session()
    s.auth = (user_name, user_pass)
    actual_summ = "JustCreateNewIssue " + generate_summary()
    r = s.post(base_URL + create_URL, headers=h, data=newIssue(project_name, actual_summ, "Bug"))
    id = json.loads(r.text)['id']
    yield actual_summ
    s.delete(base_URL + create_URL + id)


@pytest.fixture(scope=pytestScope)
def prepareFiveIssues():
    s = requests.Session()
    s.auth = (user_name, user_pass)
    ids = []
    for i in range(5):
        five_summs = "Ughhh_5 " + generate_summary()
        r = s.post(base_URL + create_URL, headers=h, data=newIssue(project_name, five_summs, "Bug"))
        ids.append(json.loads(r.text)['id'])
    yield five_summs
    for j in ids:
        r = s.delete(base_URL + create_URL + j)
        assert r.status_code == requests.codes.no_content


def pytest_exception_interact(node, call):
    dr = pytest.global_wd
    allure.attach(dr.get_screenshot_as_png(),
                  name=node.nodeid.rsplit("::", 1)[1],
                  attachment_type=allure.attachment_type.PNG, )
    allure.attach(body=str(call.excinfo.traceback).replace(",", ",\n"))

def pytest_namespace():
    return {'global_wd': 0}

