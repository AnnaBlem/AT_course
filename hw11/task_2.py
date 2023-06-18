# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
from datetime import datetime
import time

driver = webdriver.Chrome()
site = 'https://fix-online.sbis.ru/'
user_login, user_password = 'Аргус1', 'Аргус123'
name_user = 'Дыгай Андрей'
message = f'Привет, друг, на дворе {time.time()}'

try:
    driver.get(site)
    sleep(1)

    print('Авторизоваться на сайте https://fix-online.sbis.ru/')
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    print('Перейти в реестр Контакты')
    contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    contacts.click()
    sleep(5)
    contacts2 = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts2.click()
    sleep(5)

    print('Отправить сообщение самому себе')
    plus = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    plus.click()
    sleep(5)
    date_today = datetime.today()
    search_user = driver.find_element(
        By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] .controls-InputBase__field>input'
    )
    search_user.send_keys(name_user, Keys.ENTER)
    sleep(5)
    choose_user = driver.find_element(By.CSS_SELECTOR, f'[title="{name_user}"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", choose_user)
    choose_user.click()
    sleep(5)
    text_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_message.send_keys(message, Keys.CONTROL + Keys.ENTER)
    sleep(5)

    print('Убедиться, что сообщение появилось в реестре')
    my_messages = [
        el for el in driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
        if el.text.strip() == message
    ]
    assert len(my_messages) != 0, 'Сообщение не появилось в реестре!'
    my_message = my_messages[0]

    print('Удалить это сообщение и убедиться, что удалили')
    actions_chains = ActionChains(driver)
    actions_chains.move_to_element(my_message)
    actions_chains.context_click(my_message)
    actions_chains.perform()
    sleep(5)
    delete = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    delete.click()
    sleep(5)
    my_messages = [
        el for el in driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text')
        if el.text.strip() == message
    ]
    assert len(my_messages) == 0, 'Сообщение не удалено!'
finally:
    driver.quit()
