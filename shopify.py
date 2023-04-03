from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv


browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

start = 0  # starting page number
urls = []  # list to store URLs
while start < 330:  # set the limit here
    url = f'https://www.google.com/search?q=site%3Amyshopify.com+online&start={start}'
    browser.get(url)
    browser.maximize_window()

    sleep(2)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#search')))

    # Find all the search result URLs
    elements = browser.find_elements_by_css_selector('div#search cite')
    for element in elements:
        if "myshopify.com" in element.text:
            shopify_url = element.text
            url = shopify_url.split()[0]
            urls.append(url)

    start += 10  # increment the page number by 10

browser.close()

# Write URLs to CSV file
with open('shopify_urls.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['shopify_url'])
    writer.writeheader()
    for url in urls:
        writer.writerow({'shopify_url': url})