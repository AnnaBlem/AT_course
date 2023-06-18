# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    print('Перейти на https://sbis.ru/')
    driver.get("https://sbis.ru/")
    sleep(1)

    print('Перейти в раздел "Контакты"')
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contacts.text == 'Контакты'
    contacts.click()
    sleep(1)

    print('Найти баннер Тензор, кликнуть по нему')
    banner = driver.find_element(By.CSS_SELECTOR, '[alt="Разработчик системы СБИС — компания «Тензор»"]')
    banner.click()
    sleep(1)

    print('Перейти на https://tensor.ru/')
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://tensor.ru/', 'Страница https://tensor.ru/ не открылась'

    print('Проверить, что есть блок новости "Сила в людях"')
    strength_in_people = driver.find_element(By.XPATH, '//p[text()="Сила в людях"]')
    assert strength_in_people.is_displayed(), '"Сила в людях" не отображается'
    sleep(3)

    print('Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about')
    about = driver.find_element(By.XPATH, '//p[text()="Сила в людях"]/..//a[text()="Подробнее"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", about)
    sleep(3)
    about.click()
    sleep(3)
    assert driver.current_url == 'https://tensor.ru/about', 'Подробнее не открылась'
    sleep(3)
finally:
    driver.quit()


