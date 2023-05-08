from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv


browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

"""

"""

search_queries = ["Smartphones", "Laptops", "Headphones", "Bluetooth Speakers", "Power Banks", "Fitness Bands", "Smart Watches", "Televisions", "Air Conditioners", "Refrigerators", "Washing Machines", "Water Purifiers", "Microwave Ovens", "Induction Cooktops", "Kitchen Chimneys", "Home Theatres", "Soundbars", "Gaming Consoles", "Gaming Laptops", "Printers", "External Hard Drives", "Pen Drives", "Memory Cards", "Webcams", "Wireless Routers", "Network Switches", "CCTV Cameras", "Digital Cameras", "Camera Lenses", "Tripods", "Gimbal Stabilizers", "Drone Cameras", "Projectors", "Laser Printers", "Ink Tank Printers", "Sarees", "Kurtis", "Lehengas", "Salwar Suits", "T-Shirts", "Shirts", "Jeans", "Casual Shoes", "Sports Shoes", "Flip-Flops", "Sneakers", "Watches", "Sunglasses", "Backpacks", "Handbags", "Wallets", "Jewelry", "Books", "Toys", "Pet Supplies", "Baby Care Products", "Air Fryers", "Air Purifiers", "Blenders", "Coffee Makers", "Electric Kettles", "Food Processors", "Juicers", "Mixer Grinders", "Ovens", "Pressure Cookers", "Toaster Ovens", "Toasters", "Water Heaters", "Iron Boxes", "Vacuum Cleaners", "Electric Shavers", "Hair Dryers", "Hair Straighteners", "Trimmers", "Makeup Kits", "Perfumes", "Skin Care Products", "Hair Care Products", "Deodorants", "Home Decor", "Furniture", "Mattresses", "Carpets", "Curtains", "Wall Clocks", "Artificial Flowers", "Paintings", "Wallpapers", "Barbecue Grills", "Helmets", "Bicycles", "Golf Equipment", "Cricket Equipment", "Badminton Equipment", "Tennis Equipment", "Footballs", "Basketballs", "Swimming Goggles", "Fitness Equipment", "Musical Instruments", "Gardening Tools", "Office Supplies", "Stationery", "Craft Supplies", "Festive Decor", "Party Supplies"]


start = 0  # variable for starting page number of google search
urls = []  # list to store URLs from the google search


# You can uncomment the line below to search for a single query 
# search_queries = "Smartphones"


# Main Logic
for search_query in search_queries:
    while start < 330:  # this is the last page number of search, maximum limit is 350
        url = f'https://www.google.com/search?q=site%3Amyshopify.com+{search_queries}&start={start}'
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
                elements = browser.find_elements_by_css_selector('div#search cite')
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
    with open('shopify_urls_test.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['shopify_url'])
        if csvfile.tell() == 0:
            writer.writeheader()
        for url in urls:
            writer.writerow({'shopify_url': url})

    # reset urls and start the logic for the next value in the search_queries variable
    urls = []
    start = 0

browser.close()