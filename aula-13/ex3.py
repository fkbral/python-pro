from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

search_term = input("Entre com o produto a ser pesquisado: ")

browser = webdriver.Chrome()
browser.get('https://www.ebay.com/')

search_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "gh-ac")))
search_box.send_keys(search_term)

submitButton = WebDriverWait(browser, 4).until(EC.element_to_be_clickable((By.ID, "gh-btn"))).click()

first_item = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-item__wrapper.clearfix")))

prices = browser.find_elements_by_class_name("s-item__price")

for price in prices:
  print(price.text)

browser.close()