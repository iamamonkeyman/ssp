import allure
import pytest
from support_classes.jira_pages import *


@pytest.mark.jiraui
class TestUpdateIssue:

    def test_update_three_fields(s, loginToJira):
        summary = "Scaramouche"
        updated_summary = summary + "_fandango"
        main_jira_page: MainPO = loginToJira
        main_jira_page.open_filter()
        main_jira_page.create_issue(project, "Bug", summary)
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
        main_jira_page.click_on_assign_to_me_button()
        main_jira_page.confirm_update()
        assert main_jira_page.countelem(main_jira_page._CHECK_ASSIGNMENT_SPAN) == 2
        main_jira_page.delete_issue()
        assert main_jira_page.ispresent(MainPO._DELETE_MESSAGE)


if __name__ == '__main__':
    pytest.main()
