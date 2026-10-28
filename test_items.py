import time

from selenium.webdriver.common.by import By


def test_product_page_has_add_to_basket_button(browser):
    """На странице товара должна быть кнопка добавления товара в корзину."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза нужна для визуальной проверки языка кнопки при запуске с --language=fr
    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления товара в корзину не найдена на странице"
