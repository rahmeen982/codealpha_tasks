import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
data = []

for page in range(1, 51):
    url = base_url.format(page)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f" Error fetching page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text

        rating_text = book.p['class'][1]
        rating = rating_map.get(rating_text, 0)

        availability = book.find("p", class_="instock availability").text.strip()

        relative_url = book.h3.a['href'].replace('../../../', '')
        book_url = "https://books.toscrape.com/catalogue/" + relative_url

        image_url = "https://books.toscrape.com/" + book.find("img")["src"].replace('../', '')

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Book URL": book_url,
            "Image URL": image_url
        })

    print(f" Page {page} scraped.")
    time.sleep(1) 

df = pd.DataFrame(data)
df.to_csv("books_dataset.csv", index=False)

df.to_excel("books_dataset.xlsx", index=False ,engine='openpyxl')

print(" Done! All book data saved to 'books_dataset.csv'and 'books_dataset.xlsx'")
