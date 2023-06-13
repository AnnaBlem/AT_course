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
sleep(3)
try:
    print('Перейти на https://sbis.ru/')
    driver.get("https://sbis.ru/")
    sleep(1)

    print('Перейти в раздел "Контакты"')
    Contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    Contacts.click()
    sleep(1)

    print('Найти баннер Тензор, кликнуть по нему')
    Banner = driver.find_element(By.CSS_SELECTOR, '[alt="Разработчик системы СБИС — компания «Тензор»"]')
    Banner.click()
    sleep(1)

    print('Перейти на https://tensor.ru/')
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить, что есть блок новости "Сила в людях"')
    Strength_in_people = driver.find_elements(By.CSS_SELECTOR, '.tensor_ru-pb-16')[1]
    assert Strength_in_people.is_displayed(), '"Сила в людях" не отображается'
    sleep(3)

    print('Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about')
    About = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", About)
    sleep(3)
    About.click()
    sleep(3)
    assert driver.current_url == 'https://tensor.ru/about', 'Подробнее не открылась'
    sleep(3)
finally:
    driver.quit()


