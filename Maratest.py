from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re



PATH = "C:\ini\chromedriver.exe"
driver = webdriver.Chrome(PATH)

soup = bs(driver.page_source, 'lxml')


driver.get("https://www.marathonbet.ru/su/betting/Football/Russia/Premier+League/Akhmat+Grozny+vs+Spartak+Moscow+-+11444660")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//html[1]/body[1]/div[11]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")))
element.click()
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//html[1]/body[1]/div[11]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[3]/td[1]/div[1]/div[2]/span[1]")))
# element.click()
# element = driver.find_element_by_css_selector('[data-selection-key*="@To_Win_Match_With_Asian_Handicap0.HB_ASN_H"]')
# element.click()
time.sleep(4)
# element = driver.find_elements_by_xpath("//div[contains(text(),'(-1.0)')]/following::div[1]/span")
# fora = '(0)'
# element = driver.find_element_by_xpath(f"//body[1]/div[11]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[4]/td[1]/div[1]/div[contains(text(), '{fora}')]")
fora = '(+2.5)'



path = (f"//body[1]/div[11]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[5]/td[1]/div[1]/div[contains(text(), '{fora}')]")

my_list = []
for x in range(9):
    my_list.append(f"//body[1]/div[11]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/table[2]/tbody[1]/tr[{x}]/td[1]/div[1]/div[contains(text(), '{fora}')]")

for i in my_list:
    try:
        element = driver.find_element_by_xpath(i)
        element.click()
    except:
        pass








# element = driver.find_element_by_class_name('choice-price').text






# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#
#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)
# except:
#     driver.quit()

