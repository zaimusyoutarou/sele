from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from bottle import route, run

 
options = Options()

if chrome_binary_path: options.binary_location = chrome_binary_path
options.add_argument('--headless')


driver = Chrome(executable_path=driver_path, chrome_options=options)

driver.get("https://www.google.co.jp")
#Gmailへのリンク要素をClass属性名から取得
element = driver.find_element_by_class_name("gb_P")
#要素のinnerTextを出力
print(element.text)

@route("/")
def hello_world():
        return element.text

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))