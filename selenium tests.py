from selenium import webdriver

chrome = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

chrome.get('https://www.zerocarbo.com.br/')

vitaminas = chrome.find_element_by_xpath(
    '//*[@id="corpo"]/div/div[1]/div[1]/div[1]/div/ul/li[5]/ul/li[18]/a'
)

vitaminas.click()
