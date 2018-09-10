import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestCreateIssue:
    def test_all_required_fields(s, loginToJira):
        summ = "Scaramouche"
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.create_issue(project + "\n", "Bug", summ)
        mp.open_reported_by_me()
        mp.select_issue(summ)
        mp.delete_issue()
        assert True

    def test_missed_field(s, loginToJira):
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.create_issue(project + "\n", "Bug", "")
        assert True

    def test_looong_summary(s, loginToJira):
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.create_issue(project + "\n", "Bug", "iam_lon".ljust(265, "g"))
        assert True


if __name__ == '__main__':
    pytest.main()
