#  Task 2: Exploratory Data Analysis (EDA)

## Objective

- Analyze the book data to uncover insights using statistical methods and visualizations.
- Identify patterns, trends, and outliers in book pricing and ratings.

---

## Key Questions Answered

1. What is the total number of books?
2. What are the minimum, maximum, and average prices of books?
3. What is the most common rating?
4. What is the average price for each rating?
5. How many books are priced over £50?
6. What does the price distribution of books look like?
7. How does price vary across different ratings?

---

##  Files Included

- `eda_books.py` – Python script for performing EDA
- `books_dataset_cleaned.xlsx` – Cleaned Excel dataset used in the analysis
- `price_distribution.png` – Histogram showing distribution of book prices
- `price_by_rating_boxplot.png` – Boxplot comparing prices by rating

---

##  Libraries Used

- `pandas` – Data manipulation
- `matplotlib` – Data visualization
- `seaborn` – Statistical graphics

---

##  Visual Output

The code generates two main charts:
- **Price Distribution** – Histogram with KDE overlay
- **Boxplot of Prices by Rating** – Helps visualize how book prices vary across ratings

---

##  Insights

- Most books have similar pricing (around £53.50)
- Ratings range from 1 to 5 with no strong price correlation
- All books are priced above £50, with minimal variance

---

##  Output Format

All visuals and the final cleaned dataset are saved and included in this folder for reference.

