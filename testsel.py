from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
options = Options()

if chrome_binary_path: options.binary_location = chrome_binary_path
options.add_argument('--headless')


driver = Chrome(executable_path=driver_path, chrome_options=options)

driver.get("https://www.google.co.jp")
#Gmailへのリンク要素をClass属性名から取得
element = driver.find_element_by_class_name("gb_P")
#要素のinnerTextを出力
print(element.text)

