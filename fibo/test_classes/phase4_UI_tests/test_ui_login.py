import pytest
from dev_classes.phase4_UI.jira_pages import *


class TestLogin:
    @pytest.mark.parametrize("creds, expected", [
        ((user_name, "no_valid_pass"), (LoginPO._LOGIN_ERROR,)),
        (("no_valid_login", user_pass), (LoginPO._LOGIN_ERROR,)),
        ((user_name, user_pass), (LoginPO._CREATE_BUTTON,))
    ])
    def test_login(s, wd_fixture, creds, expected):
        login_page = LoginPO(wd_fixture.getWD())
        login_page.loginToJira(creds[0], creds[1])
        assert login_page.ispresent(expected[0])


if __name__ == '__main__':
    pytest.main()
