from selene import browser, be, by
import allure


def test_selene():
    browser.open('/')
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys("AozakiKatsu/qa_guru_hw9").press_enter()
    browser.element(by.link_text("AozakiKatsu/qa_guru_hw9")).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text("#2")).should(be.visible)
