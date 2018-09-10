import pytest
from dev_classes.phase4_UI.jira_pages import *


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
