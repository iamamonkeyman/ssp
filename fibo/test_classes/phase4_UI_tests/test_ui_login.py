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


if __name__ == '__main__':
    pytest.main()
