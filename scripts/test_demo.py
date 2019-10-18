import time

from selenium import webdriver


class TestDemo:

    def test_demo(self):
        driver = webdriver.Chrome()

        driver.get("http://www.baidu.com")
        driver.maximize_window()

        time.sleep(10)