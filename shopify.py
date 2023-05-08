from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv

browser = webdriver.Firefox(executable_path="../drivers/geckodriver")

search_queries = [
  "Smartphones India",
  "Laptops India",
  "Headphones India",
  "Bluetooth Speakers India",
  "Power Banks India",
  "Fitness Bands India",
  "Smart Watches India",
  "Televisions India",
  "Air Conditioners India",
  "Refrigerators India",
  "Washing Machines India",
  "Water Purifiers India",
  "Microwave Ovens India",
  "Induction Cooktops India",
  "Kitchen Chimneys India",
  "Home Theatres India",
  "Soundbars India",
  "Gaming Consoles India",
  "Gaming Laptops India",
  "Printers India",
  "External Hard Drives India",
  "Pen Drives India",
  "Memory Cards India",
  "Webcams India",
  "Wireless Routers India",
  "Network Switches India",
  "CCTV Cameras India",
  "Digital Cameras India",
  "Camera Lenses India",
  "Tripods India",
  "Gimbal Stabilizers India",
  "Drone Cameras India",
  "Projectors India",
  "Laser Printers India",
  "Ink Tank Printers India",
  "Sarees India",
  "Kurtis India",
  "Lehengas India",
  "Salwar Suits India",
  "T-Shirts India",
  "Shirts India",
  "Jeans India",
  "Casual Shoes India",
  "Sports Shoes India",
  "Flip-Flops India",
  "Sneakers India",
  "Watches India",
  "Sunglasses India",
  "Backpacks India",
  "Handbags India",
  "Wallets India",
  "Jewelry India",
  "Books India",
  "Toys India",
  "Pet Supplies India",
  "Baby Care Products India",
  "Air Fryers India",
  "Air Purifiers India",
  "Blenders India",
  "Coffee Makers India",
  "Electric Kettles India",
  "Food Processors India",
  "Juicers India",
  "Mixer Grinders India",
  "Ovens India",
  "Pressure Cookers India",
  "Toaster Ovens India",
  "Toasters India",
  "Water Heaters India",
  "Iron Boxes India",
  "Vacuum Cleaners India",
  "Electric Shavers India",
  "Hair Dryers India",
  "Hair Straighteners India",
  "Trimmers India",
  "Makeup Kits India",
  "Perfumes India",
  "Skin Care Products India",
  "Hair Care Products India",
  "Deodorants India",
  "Home Decor India",
  "Furniture India",
  "Mattresses India",
  "Carpets India",
  "Curtains India",
  "Wall Clocks India",
  "Artificial Flowers India",
  "Paintings India",
  "Wallpapers India",
  "Barbecue Grills India",
  "Helmets India",
  "Bicycles India",
  "Golf Equipment India",
  "Cricket Equipment India",
  "Badminton Equipment India",
  "Tennis Equipment India",
  "Footballs India",
  "Basketballs India",
  "Swimming Goggles India",
  "Fitness Equipment India",
  "Musical Instruments India",
  "Gardening Tools India",
  "Office Supplies India",
  "Stationery India",
  "Craft Supplies India",
  "Festive Decor India",
  "Party Supplies India"
]


start = 0  # variable for starting page number of google search
urls = []  # list to store URLs from the google search


# You can uncomment the line below to search for a single query 
# search_queries = "Smartphones"

for search_query in search_queries:
    while start < 330:  # this is the last page number of search, maximum limit is 350
        url = f'https://www.google.com/search?q=site%3Amyshopify.com+{search_query}&start={start}'
        browser.get(url)
        browser.maximize_window()

        sleep(2)

        wait = WebDriverWait(browser, 60)
        while True:
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#search')))
                break
            except:
                print("Could not find CSS selector 'div#search', retrying...")
                continue

        # Find all the search result URLs
        while True:
            try:
                elements = browser.find_elements((By.CSS_SELECTOR, 'div#search cite'))
                for element in elements:
                    if "myshopify.com" in element.text:
                        shopify_url = element.text
                        url = shopify_url.split()[0]
                        urls.append(url)
                break
            except:
                print("URL extraction failed, retrying...")
                continue

        start += 10  # increment the page number by 10

    # Removing duplicates from the list of URLs as sets cannot have a duplicate value
    urls = list(set(urls))

    # Write URLs to CSV file
    with open('final_indian_shopify_urls.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['shopify_url'])
        if csvfile.tell() == 0:
            writer.writeheader()
        for url in urls:
            writer.writerow({'shopify_url': url})

    # reset urls and start for the next value in search_queries
    urls = []
    start = 0

browser.close()