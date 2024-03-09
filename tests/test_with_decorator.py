from selene import browser, be, by
import allure


def test_with_decorator():
    open_main_page()
    search_repo()
    click_on_link()
    open_tab_issues()
    search_issue_2()


@allure.step('Open browser')
def open_main_page():
    browser.open('/')


@allure.step('Search repo')
def search_repo():
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys("AozakiKatsu/qa_guru_hw9").press_enter()


@allure.step('Click on link')
def click_on_link():
    browser.element(by.link_text("AozakiKatsu/qa_guru_hw9")).click()


@allure.step('Open tab Issues')
def open_tab_issues():
    browser.element('#issues-tab').click()


@allure.step('Search issue #2')
def search_issue_2():
    browser.element(by.partial_text("#2")).should(be.visible)
