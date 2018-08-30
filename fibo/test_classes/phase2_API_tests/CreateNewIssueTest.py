from dev_classes.phase2_API.json_fixtures import *
from dev_classes.phase2_API.properties_for_phase2 import *
import requests
import pytest
import json


@pytest.fixture()
def s():
    sess = requests.Session()
    sess.auth = (user_name, user_pass)
    return sess


def test_request_with_all_required_fields(s):
    actual_summ = "JustCreateNewIssue "+generate_summary()
    r = s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, "Bug"))
    r = s.get(base_URL+create_URL + json.loads(r.text)['id'], headers=h)
    assert json.loads(r.text)['fields']['summary'] == actual_summ


def test_create_with_absent_required_field(s):
    actual_summ = "create_new_issue"+generate_summary()
    r = s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, ""))
    assert r.status_code == requests.codes.bad
    assert r.text.find("issue type is required") != -1


def test_create_with_text_longer_then_supported(s):
    actual_summ = '''Very__________________________Long_________________________summury____________________________100_
    Very__________________________Long_________________________summury______________________________200_
    Very_________________________Long_______________________summury___________________________300_'''+generate_summary()
    r = s.post(base_URL+create_URL,  headers=h,  data=newIssue("AQAPYTHON", actual_summ, "Bug"))
    assert r.status_code == requests.codes.bad
    assert r.text.find("Summary must be less than 255 characters") != -1


if __name__ == '__main__':
    pytest.main()