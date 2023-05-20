import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    from selenium import webdriver
    test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

    # options = Options()
    # FFmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    # ff = ffmpy3.FFmpeg(
    #     executable=FFmpeg,
    #     inputs={old: None},
    #     outputs={new: None}
    # )

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")

    options.add_argument(f'--user-agent={test_ua}')

    # options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    # driver = webdriver.Chrome()
    s = Service(r'C:\Users\tz\PycharmProjects\pythonProject6\static\chromedriver.exe')  # 驱动path

    driver = webdriver.Chrome(options=options,service=s)
    driver.get("https://store.steampowered.com/join?l=schinese")

    # search=driver.find_element_by_id("kw")这种方式已经被弃用
    search = driver.find_element(By.ID, "email")
    search.send_keys("test")
    search = driver.find_element(By.ID, "reenter_email")
    search.send_keys("test")

    search = driver.find_element(By.ID, "i_agree_check")
    search.click()
    time.sleep(5)
    solver = RecaptchaSolver(driver=driver)

    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    # search = WebDriverWait(driver, 13).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]')))  # 60s
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    # from selenium.webdriver.common.by import By
    #
    #
    #
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    # s = Service(r'C:\Users\tz\PycharmProjects\pythonProject6\static\chromedriver.exe')  # 驱动path
    #
    # driver = webdriver.Chrome(service=s)
    # driver.get("https://www.baidu.com/")
    #
    # # search=driver.find_element_by_id("kw")这种方式已经被弃用
    # search = driver.find_element(By.ID, "kw")
    # search.send_keys("伊木子曦")
    #
    # # send_button=driver.find_element_by_id("su")
    # send_button = driver.find_element(By.ID, "su")
    # send_button.click()



