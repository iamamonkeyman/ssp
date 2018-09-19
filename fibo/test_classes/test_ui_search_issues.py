import pytest
from support_classes.jira_pages import *


class TestSearchIssue:
    def test_find_one(s, prepareOneIssue, loginToJira):
        summary = prepareOneIssue
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.search_issue(summary)
        main_jira_page.select_issue(summary)
        assert main_jira_page.count_filtered_issues() == 1

    def test_find_five(s, prepareFiveIssues, loginToJira):
        summary = prepareFiveIssues[:7]
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.search_issue(summary)
        assert main_jira_page.count_filtered_issues() == 5

    def test_find_none(s, loginToJira):
        summary = "whereIam"
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.search_issue(summary)
        assert main_jira_page.count_filtered_issues() == 0


if __name__ == '__main__':
    pytest.main()
