# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os.path

import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
site = 'https://sbis.ru/'

try:
    print('Перейти на  https://sbis.ru/')
    driver.get(site)
    sleep(5)

    print('В Footer найти "Скачать СБИС"')
    download_button = driver.find_element(By.LINK_TEXT, 'Скачать СБИС')

    print('Перейти по "Скачать СБИС"')
    driver.execute_script("return arguments[0].scrollIntoView(true);", download_button)
    download_button.click()
    sleep(5)

    print('Скачать СБИС Плагин для вашей ОС в папку с данным тестом')
    plugin_button = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin_button.click()
    sleep(5)
    web_setup_url = driver.find_elements(By.XPATH,
                                         '//p[contains(text(), "СБИС Плагин работает на операционных системах")]/'
                                         '..//a[contains(text(), "Скачать")]')[0].get_attribute("href")
    download_path = os.path.join(os.path.dirname(__file__), "sbisplugin-setup-web.exe")
    urllib.request.urlretrieve(web_setup_url, download_path)

    print('Убедиться, что плагин скачался')
    assert os.path.exists(download_path), "Файл не скачался"

    print("Размер плагина:", os.path.getsize(download_path) // (1024 * 1024), "Мб")

finally:
    driver.quit()
