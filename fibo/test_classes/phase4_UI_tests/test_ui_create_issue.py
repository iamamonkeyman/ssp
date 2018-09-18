import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestCreateIssue:
    def test_all_required_fields(s, loginToJira):
        summary = "Scaramouche"
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.create_issue(project + "\n", "Bug", summary)
        main_jira_page.tillInvisible(MainPO._CONFIRM_BUTTON)
        assert main_jira_page.ispresent(MainPO._CREATE_MESSAGE)
        main_jira_page.open_reported_by_me()
        main_jira_page.select_issue(summary)
        main_jira_page.delete_issue()
        assert main_jira_page.ispresent(MainPO._DELETE_MESSAGE)

    def test_missed_field(s, loginToJira):
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.create_issue(project + "\n", "Bug", "")
        isTrue = main_jira_page.ispresent(MainPO._EMPTY_MESSAGE)
        main_jira_page.cancel_creation()
        assert isTrue

    def test_looong_summary(s, loginToJira):
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.create_issue(project + "\n", "Bug", "iam_lon".ljust(265, "g"))
        isTrue = main_jira_page.ispresent(MainPO._LONG_MESSAGE)
        main_jira_page.cancel_creation()
        assert isTrue



if __name__ == '__main__':
    pytest.main()
