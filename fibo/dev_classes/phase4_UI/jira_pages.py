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
    LOGIN = (By.ID, "login-form-username")
    PASSW = (By.ID, "login-form-password")
    LOGBTN = (By.ID, "login")
    MAINPAGE = (By.ID, "create_link")
    LOGERR = (By.CSS_SELECTOR, ".aui-message.error")

    def __init__(s, webdr):
        super().__init__(webdr)
        s.wd.get(base_URL)

    def _loginaction(s, l, p):
        s.elem(s.LOGIN).clear()
        s.elem(s.LOGIN).send_keys(l)
        s.elem(s.PASSW).clear()
        s.elem(s.PASSW).send_keys(p)
        s.elem(s.LOGBTN).click()

    def loginToJira(s, l, p):
        s._loginaction(l, p)
        if s.ispresent(s.MAINPAGE):
            return MainPO(s.wd)
        return s


class MainPO(RootPO):
    ISSMENU = (By.ID, "find_link")
    SEARCH = (By.ID, "issues_new_search_link_lnk")
    ISSH1 = (By.CSS_SELECTOR, "h1[title='Search']")
    REPORTED = (By.CSS_SELECTOR, "a[title='Reported by me']")
    REPORTH1 = (By.CSS_SELECTOR, "h1[title='Reported by me']")
    CREATE = (By.ID, "create_link")
    PROJ = (By.ID, "project-field")
    H5 = (By.CSS_SELECTOR, "[id='project-field'][aria-expanded='true']")
    ISSTYPE = (By.ID, "issuetype-field")
    PRIORTYPE = (By.ID, "priority-field")
    ASSIGNEE = (By.ID, "assignee-field")
    SUMM = (By.ID, "summary")
    CREBTN = (By.ID, "create-issue-submit")
    CONFIRM = (By.ID, "create-issue-submit")
    EMPTYMESS = (By.XPATH, "//div[.='You must specify a summary of the issue.']")
    LONGMESS = (By.XPATH, "//div[.='Summary must be less than 255 characters.']")
    CANCEL = (By.CSS_SELECTOR, ".jira-dialog-content a.cancel")
    MORE = (By.ID, "opsbar-operations_more")
    DEL = (By.CSS_SELECTOR, "#opsbar-operations_more_drop #delete-issue")
    DELCONFIRM = (By.ID, "delete-issue-submit")
    ASSTOME = (By.ID, "assign-to-me-trigger")
    FILTERED = (By.CSS_SELECTOR, ".issue-list li")
    DELMESS = (By.XPATH, "//div[contains(text(), 'has been deleted')]")
    LOADING = (By.CSS_SELECTOR, ".loading")
    CHKASSI = (By.XPATH, "//dd/span[contains(.,'Alex Skryabin')]")
    CHKPRIO = (By.CSS_SELECTOR, "img[title*='Lowest']")
    USERMENU = (By.ID, "header-details-user-fullname")
    SEARCHF = (By.ID, "searcher-query")
    UPDBTN = (By.CSS_SELECTOR, "#issue-content #edit-issue")
    UPDMESS = (By.XPATH, "//div[contains(text(), 'has been updated')]")
    UPDCONFIRM = (By.ID, "edit-issue-submit")
    LOGOUT = (By.ID, "log_out")

    def __init__(s, webdr):
        super().__init__(webdr)

    def open_filter(s):
        s.tillInvisible(s.LOADING)
        s.elem(s.ISSMENU).click()
        s.elem(s.SEARCH).click()
        s.elem(s.ISSH1)
        s.tillInvisible(s.LOADING)

    def open_reported_by_me(s):
        if not s.ispresent(s.ISSH1):
            s.open_filter()
        s.elem(s.REPORTED).click()
        s.elem(s.REPORTH1)
        s.tillInvisible(s.LOADING)

    def create_issue(s, proj, type, sum):
        s.elem(s.CREATE).click()
        s.elem(s.PROJ).click()
        s.elem(s.PROJ).send_keys(proj)
        #
        s.tillInvisible(s.H5)
        s.elem(s.ISSTYPE).click()
        s.elem(s.ISSTYPE).send_keys(type + "\n")
        #
        s.tillInvisible(s.H5)
        s.elem(s.SUMM).clear()
        s.elem(s.SUMM).send_keys(sum)
        s.elem(s.CREBTN).click()
        #
        if len(sum) == 0:
            s.elem(s.EMPTYMESS)
            s.elem(s.CANCEL).click()
            s.wd.switch_to.alert.accept()
        if len(sum) > 255:
            s.elem(s.LONGMESS)
            s.elem(s.CANCEL).click()
            s.wd.switch_to.alert.accept()
        s.tillInvisible(s.CONFIRM)

    def select_issue(s, sum):
        s.tillInvisible(s.LOADING)
        s.elem((By.XPATH, f"//span[.='{sum}']")).click()
        s.tillInvisible(s.LOADING)

    def delete_issue(s):
        s.elem(s.MORE).click()
        s.elem(s.DEL).click()
        s.elem(s.DELCONFIRM).click()
        s.tillInvisible(s.LOADING)
        s.tillInvisible(s.DELMESS)

    def search_issue(s, sum):
        s.elem(s.SEARCHF).clear()
        s.elem(s.SEARCHF).send_keys(sum + "\n")
        s.tillInvisible(s.LOADING)

    def count_filtered_issues(s):
        return s.countelem(s.FILTERED)

    def trigger_update(s):
        s.elem(s.UPDBTN).click()
        s.elem(s.SUMM)

    def confirm_update(s):
        s.elem(s.UPDCONFIRM).click()
        s.tillInvisible(s.LOADING)
        s.tillInvisible(s.UPDMESS)

    def update_summary(s, new_sum):
        if not s.ispresent(s.SUMM):
            s.trigger_update()
        s.elem(s.SUMM).clear()
        s.elem(s.SUMM).send_keys(new_sum + "\n")
        s.tillInvisible(s.UPDMESS)

    def update_priority(s, new_priority):
        if not s.ispresent(s.SUMM):
            s.trigger_update()
        s.elem(s.PRIORTYPE).click()
        s.elem(s.PRIORTYPE).send_keys(new_priority + "\n")

    def assign_to_me(s):
        if not s.ispresent(s.SUMM):
            s.trigger_update()
        s.scrollintoview(s.ASSIGNEE)
        s.elem(s.ASSTOME).click()

    def log_out(s):
        s.elem(s.USERMENU).click()
        s.elem(s.LOGOUT).click()
