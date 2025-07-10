#  Task 1: Web Scraping – Book Data from books.toscrape.com

This task involves extracting book information from the website [books.toscrape.com](https://books.toscrape.com/) using Python and BeautifulSoup.

---

## Objective

- Use web scraping techniques to collect product data (books).
- Gather data across multiple pages of the website.
- Save the collected data into  Excel files.

---

##  Tools & Libraries

- `requests` – To fetch HTML content from the website.
- `BeautifulSoup` – To parse and extract data from HTML.
- `pandas` – To store, clean, and export data.
- `openpyxl` – For writing Excel files.

---

## Data Collected

From each book, the following details are scraped:

- **Title**
- **Price**
- **Rating**
- **Availability**
- **Book URL**
- **Image URL**

---

##  Pagination

The script automatically scrapes data from **all 50 pages** of the website using a loop.

---

##  Files Included

- `scrape_books.py` – Python script used for scraping
- `books_dataset.xlsx` – Same data saved in Excel format

---

##  Highlights

- Cleaned non-standard symbols (e.g. `Â£`) from the price column.
- The dataset serves as the base for **Task 2: Exploratory Data Analysis**.
- Successfully scrapes and processes **1000 books** from the website.

---

## 📂 Output Example

| Title                     | Price | Rating | Availability | Book URL                        |
|---------------------------|--------|--------|--------------|----------------------------------|
| A Light in the Attic      | 51.77  | 3      | In stock     | https://books.toscrape.com/...  |
| Tipping the Velvet        | 53.74  | 1      | In stock     | https://books.toscrape.com/...  |
| Soumission                | 50.10  | 1      | In stock     | https://books.toscrape.com/...  |

---

## 📌 How to Run

Make sure to install required libraries:
```bash
pip install requests beautifulsoup4 pandas openpyxl
