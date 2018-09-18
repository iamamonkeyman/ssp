from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RWD
from dev_classes.phase4_UI.properties4 import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class RootPO:
    def __init__(s, wd: RWD):
        s.wd = wd
        s.wdw = WebDriverWait(wd, 10)

    def elem(s, *loc):
        return s.wdw.until(ec.visibility_of_element_located(loc[0]))

    def countelem(s, *loc):
        return len(s.wd.find_elements(loc[0][0], loc[0][1]))

    def isvisible(s, *loc):
        try:
            WebDriverWait(s.wd, 2).until(ec.visibility_of_element_located(loc[0]))
            return True
        except Exception as e:
            return False

    def ispresent(s, *loc):
        try:
            WebDriverWait(s.wd, 2).until(ec.presence_of_element_located(loc[0]))
            return True
        except Exception as e:
            return False

    def tillInvisible(s, *loc):
        return s.wdw.until(ec.invisibility_of_element_located(loc[0]))

    def scrollintoview(s, *loc):
        el = s.wd.find_element(loc[0][0], loc[0][1])
        s.wd.execute_script("return arguments[0].scrollIntoView();", el)


class LoginPO(RootPO):
    _LOGIN_INPUT = (By.ID, "login-form-username")
    _PASSW_INPUT = (By.ID, "login-form-password")
    _LOGIN_BUTTON = (By.ID, "login")
    _CREATE_BUTTON = (By.ID, "create_link")
    _LOGIN_ERROR = (By.CSS_SELECTOR, ".aui-message.error")

    def __init__(s, webdr):
        super().__init__(webdr)
        s.wd.get(base_URL)

    def _loginaction(s, l, p):
        s.elem(s._LOGIN_INPUT).clear()
        s.elem(s._LOGIN_INPUT).send_keys(l)
        s.elem(s._PASSW_INPUT).clear()
        s.elem(s._PASSW_INPUT).send_keys(p)
        s.elem(s._LOGIN_BUTTON).click()

    def loginToJira(s, l, p):
        s._loginaction(l, p)
        if s.ispresent(s._CREATE_BUTTON):
            return MainPO(s.wd)
        return s


class MainPO(RootPO):
    _ISSUES_MENU_LINK = (By.ID, "find_link")
    _SEARCHFOR_SUBMENU_LINK = (By.ID, "issues_new_search_link_lnk")
    _ISSUE_HEADER = (By.CSS_SELECTOR, "h1[title='Search']")
    _REPORTED_BY_ME_LINK = (By.CSS_SELECTOR, "a[title='Reported by me']")
    _REPORTED_HEADER = (By.CSS_SELECTOR, "h1[title='Reported by me']")
    _CREATE_LINK = (By.ID, "create_link")
    _PROJECT_INPUT = (By.ID, "project-field")
    _EXPANDED_HEADER = (By.CSS_SELECTOR, "[id='project-field'][aria-expanded='true']")
    _ISSUE_TYPE_INPUT = (By.ID, "issuetype-field")
    _PRIORITY_TYPE_INPUT = (By.ID, "priority-field")
    _ASSIGNEE_INPUT = (By.ID, "assignee-field")
    _SUMMARY_HEADER = (By.ID, "summary")
    _CREATE_ISSUE_BUTTON = (By.ID, "create-issue-submit")
    _CONFIRM_BUTTON = (By.ID, "create-issue-submit")
    _EMPTY_MESSAGE = (By.XPATH, "//div[.='You must specify a summary of the issue.']")
    _LONG_MESSAGE = (By.XPATH, "//div[.='Summary must be less than 255 characters.']")
    _CANCEL_BUTTON = (By.CSS_SELECTOR, ".jira-dialog-content a.cancel")
    _MORE_BUTTON = (By.ID, "opsbar-operations_more")
    _DEL_BUTTON = (By.CSS_SELECTOR, "#opsbar-operations_more_drop #delete-issue")
    _DEL_CONFIRM_BUTTON = (By.ID, "delete-issue-submit")
    _ASSIGNE_TO_ME_LINK = (By.ID, "assign-to-me-trigger")
    _FILTERED_LI = (By.CSS_SELECTOR, ".issue-list li")
    _DELETE_MESSAGE = (By.XPATH, "//div[contains(text(), 'has been deleted')]")
    _LOADING = (By.CSS_SELECTOR, ".loading")
    _CHECK_ASSIGNMENT_SPAN = (By.XPATH, "//dd/span[contains(.,'Alex Skryabin')]")
    _CHECK_PRIORITY_IMG = (By.CSS_SELECTOR, "img[title*='Lowest']")
    _USER_MENU_BUTTON = (By.ID, "header-details-user-fullname")
    _SEARCHER_QUERY_INPUT = (By.ID, "searcher-query")
    _UPDATE_BUTTON = (By.CSS_SELECTOR, "#issue-content #edit-issue")
    _CREATE_MESSAGE = (By.XPATH, "//div[contains(., 'successfully created')]")
    _UPDATE_MESSAGE = (By.XPATH, "//div[contains(text(), 'has been updated')]")
    _UPDATE_CONFIRM_BUTTON = (By.ID, "edit-issue-submit")
    _LOGOUT_BUTTON = (By.ID, "log_out")
    _FILTER_BASIC_A = (By.CSS_SELECTOR, "[data-id='advanced']")

    def __init__(s, webdr):
        super().__init__(webdr)

    def open_filter(s):
        s.tillInvisible(s._LOADING)
        s.elem(s._ISSUES_MENU_LINK).click()
        s.elem(s._SEARCHFOR_SUBMENU_LINK).click()
        s.elem(s._ISSUE_HEADER)
        s.tillInvisible(s._LOADING)

    def open_reported_by_me(s):
        if not s.ispresent(s._ISSUE_HEADER):
            s.open_filter()
        s.elem(s._REPORTED_BY_ME_LINK).click()
        s.elem(s._REPORTED_HEADER)
        s.tillInvisible(s._LOADING)

    def create_issue(s, proj, type, sum):
        s.elem(s._CREATE_LINK).click()
        s.elem(s._PROJECT_INPUT).click()
        s.elem(s._PROJECT_INPUT).send_keys(proj)
        #
        s.tillInvisible(s._EXPANDED_HEADER)
        s.elem(s._ISSUE_TYPE_INPUT).click()
        s.elem(s._ISSUE_TYPE_INPUT).send_keys(type + "\n")
        #
        s.tillInvisible(s._EXPANDED_HEADER)
        s.elem(s._SUMMARY_HEADER).clear()
        s.elem(s._SUMMARY_HEADER).send_keys(sum)
        s.elem(s._CREATE_ISSUE_BUTTON).click()
        if 0 < len(sum) < 255:
            s.tillInvisible(s._CONFIRM_BUTTON)

    def cancel_creation(s):
        s.elem(s._CANCEL_BUTTON).click()
        s.wd.switch_to.alert.accept()
        s.tillInvisible(s._CONFIRM_BUTTON)

    def select_issue(s, sum):
        s.tillInvisible(s._LOADING)
        s.elem((By.XPATH, f"//span[.='{sum}']")).click()
        s.tillInvisible(s._LOADING)

    def delete_issue(s):
        s.elem(s._MORE_BUTTON).click()
        s.elem(s._DEL_BUTTON).click()
        s.elem(s._DEL_CONFIRM_BUTTON).click()
        s.tillInvisible(s._LOADING)
        s.tillInvisible(s._DELETE_MESSAGE)

    def search_issue(s, sum):
        if (s.isvisible(s._FILTER_BASIC_A)):
            s.elem(s._FILTER_BASIC_A).click()
        s.elem(s._SEARCHER_QUERY_INPUT).clear()
        s.elem(s._SEARCHER_QUERY_INPUT).send_keys(sum + "\n")
        s.tillInvisible(s._LOADING)

    def count_filtered_issues(s):
        return s.countelem(s._FILTERED_LI)

    def trigger_update(s):
        s.elem(s._UPDATE_BUTTON).click()
        s.elem(s._SUMMARY_HEADER)

    def confirm_update(s):
        s.elem(s._UPDATE_CONFIRM_BUTTON).click()
        s.tillInvisible(s._LOADING)
        s.tillInvisible(s._UPDATE_MESSAGE)

    def update_summary(s, new_sum):
        if not s.ispresent(s._SUMMARY_HEADER):
            s.trigger_update()
        s.elem(s._SUMMARY_HEADER).clear()
        s.elem(s._SUMMARY_HEADER).send_keys(new_sum + "\n")
        s.tillInvisible(s._UPDATE_MESSAGE)

    def update_priority(s, new_priority):
        if not s.ispresent(s._SUMMARY_HEADER):
            s.trigger_update()
        s.elem(s._PRIORITY_TYPE_INPUT).click()
        s.elem(s._PRIORITY_TYPE_INPUT).send_keys(new_priority + "\n")

    def assign_to_me(s):
        if not s.ispresent(s._SUMMARY_HEADER):
            s.trigger_update()
        s.scrollintoview(s._ASSIGNEE_INPUT)
        s.elem(s._ASSIGNE_TO_ME_LINK).click()

    def log_out(s):
        s.elem(s._USER_MENU_BUTTON).click()
        s.elem(s._LOGOUT_BUTTON).click()
