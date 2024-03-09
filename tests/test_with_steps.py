from selene import browser, be, by
import allure


def test_with_steps():
    with allure.step('Open browser'):
        browser.open('/')
    with allure.step('Search repo'):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").send_keys("AozakiKatsu/qa_guru_hw9").press_enter()
    with allure.step('Click on link'):
        browser.element(by.link_text("AozakiKatsu/qa_guru_hw9")).click()
    with allure.step('Open tab Issues'):
        browser.element('#issues-tab').click()
    with allure.step('Search issue #2'):
        browser.element(by.partial_text("#2")).should(be.visible)
