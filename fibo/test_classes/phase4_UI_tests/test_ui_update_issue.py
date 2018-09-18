import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestUpdateIssue:

    def test_update_three_fields(s, loginToJira):
        summary = "Scaramouche"
        updated_summary = summary + "_fandango"
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.create_issue(project + "\n", "Bug", summary)
        main_jira_page.open_reported_by_me()
        main_jira_page.select_issue(summary)
        main_jira_page.trigger_update()
        main_jira_page.update_summary(updated_summary)
        main_jira_page.select_issue(updated_summary)
        main_jira_page.trigger_update()
        main_jira_page.update_priority("Lowest")
        main_jira_page.confirm_update()
        assert main_jira_page.countelem(main_jira_page._CHECK_PRIORITY_IMG) == 1
        main_jira_page.trigger_update()
        main_jira_page.assign_to_me()
        main_jira_page.confirm_update()
        assert main_jira_page.countelem(main_jira_page._CHECK_ASSIGNMENT_SPAN) == 2
        main_jira_page.delete_issue()
        assert True


if __name__ == '__main__':
    pytest.main()
