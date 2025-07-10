import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("books_dataset.xlsx")

df['Price'] = df['Price'].astype(str).str.replace("£", "").str.replace("Â", "").astype(float)

total_books = len(df)
print(f"1️ Total number of books: {total_books}")

min_price = df['Price'].min()
max_price = df['Price'].max()
avg_price = df['Price'].mean()
print(f"2️ Book Price - Min: £{min_price:.2f}, Max: £{max_price:.2f}, Average: £{avg_price:.2f}")

most_common_rating = df['Rating'].mode()[0]
print(f"3️ Most common rating: {most_common_rating}")


print("4️ Average price for each rating:")
print(df.groupby('Rating')['Price'].mean().round(2))

expensive_books = df[df['Price'] > 50]
print(f"5️ Books priced over £50: {len(expensive_books)}")
print(expensive_books[['Title', 'Price', 'Rating']])


plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=20, kde=True, color='skyblue')
plt.title("6️ Price Distribution of Books")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='Rating', y='Price', data=df, hue='Rating', palette='pastel', legend=False)

plt.title("7️ Book Prices by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("price_by_rating_boxplot.png")
plt.show()

df.to_excel("books_dataset_cleaned.xlsx", index=False)
 