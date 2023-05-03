from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--verbose")


script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the ChromeDriver executable
chromedriver_path = os.path.join(script_dir, "chromedriver")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Fetch the webpage
url = "https://www.sothebys.com/en/buy/fine-art"
try:
    driver.get(url)
    print("a")
except TimeoutException:
    print("Page load timed out.")


# Scroll down to load the entire page
SCROLL_PAUSE_TIME = 1.5
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Locate product elements
product_elements = soup.find_all("div", {"class": "grid_card_imageContainer__1hQRH"})

# Lists to store the scraped data
author_names = []
article_names = []
prices = []
image_paths = []

# Download folder for images
image_folder = "product_images"
os.makedirs(image_folder, exist_ok=True)

# Scrape author names, art names, prices, and images
for i, product in enumerate(product_elements):
    # Extract author name
    author_element = product.find_next_sibling("p", {"class": "paragraph-module_paragraph16Regular__CXt6G"})
    if author_element:
        author_name = author_element.text
        author_names.append(author_name)
        print("Author name:", author_name)
    else:
        print("Author name not found.")
        continue

    # Extract art name
    art_name_element = product.find_next_sibling("h5")
    if art_name_element:
        art_name = art_name_element.text
        article_names.append(art_name)
        print("Art name:", art_name)
    else:
        print("Art name not found.")

    # Extract price
    price_container = product.find_next_sibling("div", {"class": "grid_card_priceInfo__FHvIG"})
    if price_container:
        price_element = price_container.find("p", {"class": "label-module_label14Medium__uD9e-"})
        if price_element:
            price = price_element.text
            prices.append(price)
            print("Price:", price)
        else:
            print("Price not found.")
    else:
        print("Price container not found.")
    
    # Extract image
    image_element = product.find("img")
    if image_element:
        image_url = image_element["src"]
        image_filename = f"image_{i}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        urllib.request.urlretrieve(image_url, image_path)
        image_paths.append(image_path)
        print("Image downloaded:", image_path)
    else:
        print("Image not found.")


# Close the Selenium webdriver
driver.quit()









