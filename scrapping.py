import os
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "Trailers",
}


# Fetch and parse the webpage
url = "https://www.sothebys.com/en/buy/fine-art"


print("Sending request...")
response = requests.get(url, headers=headers, timeout=10)  # 10 seconds timeout
print("Request completed.")

soup = BeautifulSoup(response.content, "html.parser")


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

# Scrape author names, article names, prices, and images
for product in product_elements:
   # Extract author name
    author_element = product.find("p")
    print(author_element)
    
    
    
    # if author_element:
    #     author_name = author_element.text
    #     author_names.append(author_name)
    # else:
    #     print("Author name not found.")
    #     continue


#     # Extract article name
#     article_element = product.find("h5")
#     if article_element:
#         article_name = article_element.text
#         article_names.append(article_name)
#     else:
#         print("Article name not found.")
#         continue

#     # Extract price
#     price_element = product.find("p", {"class": "label-module_label14Medium__uD9e-"})
#     if price_element:
#         price = price_element.text
#         prices.append(price)
#     else:
#         print("Price not found.")
#         continue

#     # Extract image URL
#     img_element = product.find("img")
#     if img_element:
#         img_url = img_element["src"]

#         # Download and save the image
#         img_data = requests.get(img_url).content
#         img_path = os.path.join(image_folder, f"{author_name}_{article_name}.jpg")
#         with open(img_path, "wb") as img_file:
#             img_file.write(img_data)

#         # Store the image path
#         image_paths.append(img_path)
#     else:
#         print("Image not found.")
#         continue


# # Create a DataFrame from the scraped data
# data = {"Author Name": author_names, "Article Name": article_names, "Price": prices, "Image Path": image_paths}
# df = pd.DataFrame(data)

# # Save the DataFrame to an Excel file
# df.to_excel("scraped_data_with_images.xlsx", index=False)
