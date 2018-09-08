import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestLogin:
    @pytest.mark.parametrize("creds, expected", [
        ((user_name, "no_valid_pass"), (LoginPO.LOGERR,)),
        (("no_valid_login", user_pass), (LoginPO.LOGERR,)),
        ((user_name, user_pass), (LoginPO.MAINPAGE,))
    ])
    def test_login(s, wd, creds, expected):
        loginP = LoginPO(wd.getWD())
        loginP.loginToJira(creds[0], creds[1])
        assert loginP.ispresent(expected[0])


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


class TestUpdateIssue:
    def test_update_three_fields(s, loginToJira):
        summ = "Scaramouche"
        upd = summ + "_fandango"
        mp: MainPO = loginToJira
        mp.open_filter()
        mp.create_issue(project + "\n", "Bug", summ)
        mp.open_reported_by_me()
        mp.select_issue(summ)
        mp.trigger_update()
        mp.update_summary(upd)
        mp.select_issue(upd)
        mp.trigger_update()
        mp.update_priority("Lowest")
        mp.confirm_update()
        assert mp.countelem(mp.CHKPRIO) == 1
        mp.trigger_update()
        mp.assign_to_me()
        mp.confirm_update()
        assert mp.countelem(mp.CHKASSI) == 2
        mp.delete_issue()
        assert True


if __name__ == '__main__':
    pytest.main()
