import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestSearchIssue:
    def test_find_one(s, prepareOneIssue, loginToJira):
        summ = prepareOneIssue
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.search_issue(summ)
        mp.select_issue(summ)
        assert mp.count_filtered_issues() == 1

    def test_find_five(s, prepareFiveIssues, loginToJira):
        summ = prepareFiveIssues[:7]
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.search_issue(summ)
        assert mp.count_filtered_issues() == 5

    def test_find_none(s, loginToJira):
        summ = "whereIam"
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.search_issue(summ)
        assert mp.count_filtered_issues() == 0


if __name__ == '__main__':
    pytest.main()
