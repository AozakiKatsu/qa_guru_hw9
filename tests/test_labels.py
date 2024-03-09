import allure


def test_definition_in_labels():
    allure.dynamic.title("тестируем issue на github")
    allure.dynamic.suite('issue #2')
    allure.dynamic.sub_suite('2')
    allure.dynamic.link("https://github.com")
    allure.dynamic.epic("qaguru")
    allure.dynamic.severity("minor")
    allure.dynamic.parent_suite("parent-suite")
    allure.dynamic.manual()
    allure.dynamic.tag("web")
    allure.dynamic.description("Тестирование dinamic description")
    allure.dynamic.description_html("<h1>Тестирование dinamic description в html формате</h1>")
    allure.dynamic.feature("feature")
    allure.dynamic.id(1234)
    allure.dynamic.issue("#2")
    allure.dynamic.label("owner", "Irina Luchkova")