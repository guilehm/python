from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
print(dir(chrome))
chrome.get('https://www.zerocarbo.com.br/')
action = action_chains.ActionChains(chrome)

vitaminas = chrome.find_element_by_xpath(
    '//*[@id="corpo"]/div/div[1]/div[1]/div[1]/div/ul/li[5]/ul/li[18]/a'
)

vitaminas.click()


zma = chrome.find_element_by_xpath(
    '//div/ul/li/ul/li/a[contains(@title, "ZMA")]'
)
