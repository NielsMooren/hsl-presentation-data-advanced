"""
Generate realistic raw data with data quality issues for workshop
This creates data that NEEDS cleaning to teach ETL concepts
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Products
products = [
    {'id': 1, 'name': 'Potatoes'},
    {'id': 2, 'name': 'Carrots'},
    {'id': 3, 'name': 'Spinach'},
    {'id': 4, 'name': 'Tomatoes'},
    {'id': 5, 'name': 'Lettuce'},
    {'id': 6, 'name': 'Broccoli'}
]

# Review templates by sentiment
positive_reviews = [
    "Amazing quality! These {product} are so good.",
    "Perfect {product}! Great taste and very fresh.",
    "Outstanding! The {product} exceeded my expectations.",
    "Love these {product}! Always consistent quality.",
    "Very fresh and tasty {product}. Highly recommend!",
    "Delicious {product}! My family loved them.",
    "Best {product} I've bought in a while.",
    "Excellent quality, will buy again!",
    "Super fresh {product}, very satisfied.",
    "Great {product}, perfect for cooking!"
]

neutral_reviews = [
    "The {product} are okay, nothing special.",
    "Fair quality {product}.",
    "Average quality {product}. Not bad but not great.",
    "The {product} are alright, nothing to complain about.",
    "Decent {product}, but I've had better.",
    "The {product} are okay, I've had better.",
    "Standard {product}, meets expectations.",
]

negative_reviews = [
    "Terrible {product}! Completely rotten.",
    "Very disappointed with these {product}.",
    "The {product} were wilted and tasteless.",
    "Poor quality {product}. Would not recommend.",
    "The {product} was moldy when I opened it.",
    "Disgusting! The {product} smelled bad.",
    "Worst {product} I've ever bought.",
    "The {product} was a bit stale and disappointing.",
    "Not fresh at all. Very disappointing {product}.",
    "Really bad {product}, had to throw them away."
]

def generate_reviews(n_reviews=850):
    """Generate reviews with DATA QUALITY ISSUES"""
    reviews = []
    
    # Generate dates (last 3 months)
    start_date = datetime.now() - timedelta(days=90)
    
    for i in range(n_reviews):
        product = random.choice(products)
        date = start_date + timedelta(days=random.randint(0, 89))
        
        # Sentiment distribution: 60% positive, 25% neutral, 15% negative
        rand = random.random()
        if rand < 0.15:
            sentiment = 'negative'
            rating = random.choice([1, 1, 2, 2])
            template = random.choice(negative_reviews)
        elif rand < 0.40:
            sentiment = 'neutral'
            rating = 3
            template = random.choice(neutral_reviews)
        else:
            sentiment = 'positive'
            rating = random.choice([4, 4, 5, 5])
            template = random.choice(positive_reviews)
        
        # Generate review text
        review_text = template.format(product=product['name'].lower())
        
        # DATA QUALITY ISSUE 1: Missing review text (~5%)
        if random.random() < 0.05:
            review_text = None
        
        # DATA QUALITY ISSUE 2: Extra whitespace (~3%)
        elif random.random() < 0.03:
            review_text = "  " + review_text + "  "
        
        # DATA QUALITY ISSUE 3: Inconsistent capitalization (~2%)
        elif random.random() < 0.02:
            review_text = review_text.upper()
        
        # DATA QUALITY ISSUE 4: Special characters/typos (~2%)
        elif random.random() < 0.02:
            review_text = review_text.replace('!', '!!!')
        
        reviews.append({
            'product_id': product['id'],
            'product_name': product['name'],
            'date': date.strftime('%Y-%m-%d'),
            'rating': rating,
            'review_text': review_text
        })
    
    df = pd.DataFrame(reviews)
    
    # DATA QUALITY ISSUE 5: Duplicates (~3%)
    n_duplicates = int(len(df) * 0.03)
    duplicate_indices = df.sample(n=n_duplicates).index
    df_duplicates = df.loc[duplicate_indices]
    df = pd.concat([df, df_duplicates], ignore_index=True)
    
    # DATA QUALITY ISSUE 6: Invalid ratings (some ratings outside 1-5)
    invalid_indices = df.sample(n=10).index
    df.loc[invalid_indices, 'rating'] = [0, 6, 7, -1, 10, 0, 6, 8, -2, 99]
    
    # DATA QUALITY ISSUE 7: Missing ratings (~2%)
    missing_rating_indices = df.sample(n=int(len(df) * 0.02)).index
    df.loc[missing_rating_indices, 'rating'] = None
    
    # DATA QUALITY ISSUE 8: Future dates (~1%)
    future_indices = df.sample(n=int(len(df) * 0.01)).index
    future_dates = [(datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d') 
                    for _ in range(len(future_indices))]
    df.loc[future_indices, 'date'] = future_dates
    
    # DATA QUALITY ISSUE 9: Inconsistent date formats (~2%)
    inconsistent_indices = df.sample(n=int(len(df) * 0.02)).index
    for idx in inconsistent_indices:
        date_obj = datetime.strptime(df.loc[idx, 'date'], '%Y-%m-%d')
        df.loc[idx, 'date'] = date_obj.strftime('%d/%m/%Y')  # Different format
    
    # Shuffle
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

def generate_inventory(n_records=300):
    """Generate inventory data with QUALITY ISSUES"""
    inventory = []
    
    # Generate dates (daily for last 3 months)
    start_date = datetime.now() - timedelta(days=90)
    
    for product in products:
        for day in range(90):
            date = start_date + timedelta(days=day)
            
            # Stock levels vary by product
            base_stock = {1: 200, 2: 150, 3: 100, 4: 180, 5: 120, 6: 90}
            stock = base_stock[product['id']] + random.randint(-50, 50)
            
            # DATA QUALITY ISSUE: Negative stock (~1%)
            if random.random() < 0.01:
                stock = -random.randint(1, 50)
            
            # DATA QUALITY ISSUE: Unrealistically high stock (~1%)
            if random.random() < 0.01:
                stock = random.randint(10000, 50000)
            
            inventory.append({
                'product_id': product['id'],
                'product_name': product['name'],
                'date': date.strftime('%Y-%m-%d'),
                'stock_level': stock
            })
    
    df = pd.DataFrame(inventory)
    
    # DATA QUALITY ISSUE: Missing stock levels (~3%)
    missing_indices = df.sample(n=int(len(df) * 0.03)).index
    df.loc[missing_indices, 'stock_level'] = None
    
    # DATA QUALITY ISSUE: Duplicates (~2%)
    n_duplicates = int(len(df) * 0.02)
    duplicate_indices = df.sample(n=n_duplicates).index
    df_duplicates = df.loc[duplicate_indices]
    df = pd.concat([df, df_duplicates], ignore_index=True)
    
    # DATA QUALITY ISSUE: Wrong product names (~1%)
    wrong_name_indices = df.sample(n=int(len(df) * 0.01)).index
    df.loc[wrong_name_indices, 'product_name'] = 'Unknown'
    
    # Shuffle
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

def generate_sales(n_records=300):
    """Generate sales data with QUALITY ISSUES"""
    sales = []
    
    # Generate dates (daily for last 3 months)
    start_date = datetime.now() - timedelta(days=90)
    
    for product in products:
        for day in range(90):
            date = start_date + timedelta(days=day)
            
            # Sales vary by product and day
            base_sales = {1: 100, 2: 80, 3: 60, 4: 90, 5: 70, 6: 50}
            
            # Weekend boost
            if date.weekday() >= 5:
                multiplier = 1.3
            else:
                multiplier = 1.0
            
            units_sold = int(base_sales[product['id']] * multiplier + random.randint(-30, 30))
            
            # Ensure non-negative
            units_sold = max(0, units_sold)
            
            sales.append({
                'product_id': product['id'],
                'product_name': product['name'],
                'date': date.strftime('%Y-%m-%d'),
                'units_sold': units_sold
            })
    
    df = pd.DataFrame(sales)
    
    # DATA QUALITY ISSUE: Missing units_sold (~2%)
    missing_indices = df.sample(n=int(len(df) * 0.02)).index
    df.loc[missing_indices, 'units_sold'] = None
    
    # DATA QUALITY ISSUE: Negative sales (~1%)
    negative_indices = df.sample(n=int(len(df) * 0.01)).index
    df.loc[negative_indices, 'units_sold'] = -random.randint(1, 50)
    
    # DATA QUALITY ISSUE: Unrealistically high sales (~1%)
    high_indices = df.sample(n=int(len(df) * 0.01)).index
    df.loc[high_indices, 'units_sold'] = random.randint(10000, 50000)
    
    # DATA QUALITY ISSUE: Duplicates (~2%)
    n_duplicates = int(len(df) * 0.02)
    duplicate_indices = df.sample(n=n_duplicates).index
    df_duplicates = df.loc[duplicate_indices]
    df = pd.concat([df, df_duplicates], ignore_index=True)
    
    # Shuffle
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

# Generate all datasets
print("Generating realistic raw data with quality issues...")
print("=" * 70)

reviews_df = generate_reviews(850)
inventory_df = generate_inventory(300)
sales_df = generate_sales(300)

# Save to CSV
reviews_df.to_csv('data/raw/reviews.csv', index=False)
inventory_df.to_csv('data/raw/inventory.csv', index=False)
sales_df.to_csv('data/raw/sales.csv', index=False)

# Report data quality issues
print("\n✅ REVIEWS DATA GENERATED:")
print(f"  Total records: {len(reviews_df):,}")
print(f"  Missing review_text: {reviews_df['review_text'].isnull().sum()}")
print(f"  Duplicates: {reviews_df.duplicated().sum()}")
print(f"  Invalid ratings: {((reviews_df['rating'] < 1) | (reviews_df['rating'] > 5)).sum()}")
print(f"  Missing ratings: {reviews_df['rating'].isnull().sum()}")

print("\n✅ INVENTORY DATA GENERATED:")
print(f"  Total records: {len(inventory_df):,}")
print(f"  Missing stock_level: {inventory_df['stock_level'].isnull().sum()}")
print(f"  Negative stock: {(inventory_df['stock_level'] < 0).sum()}")
print(f"  Duplicates: {inventory_df.duplicated().sum()}")

print("\n✅ SALES DATA GENERATED:")
print(f"  Total records: {len(sales_df):,}")
print(f"  Missing units_sold: {sales_df['units_sold'].isnull().sum()}")
print(f"  Negative sales: {(sales_df['units_sold'] < 0).sum()}")
print(f"  Duplicates: {sales_df.duplicated().sum()}")

print("\n" + "=" * 70)
print("🎯 DATA QUALITY ISSUES SUMMARY:")
print("=" * 70)
print("These issues will be cleaned in Notebook 2 (ETL):")
print("  ✓ Missing values (reviews, stock, sales)")
print("  ✓ Duplicates (all datasets)")
print("  ✓ Invalid values (negative stock, invalid ratings)")
print("  ✓ Inconsistent formats (dates, text)")
print("  ✓ Whitespace issues")
print("  ✓ Data validation needed")
print("\n✅ Realistic raw data ready for workshop!")
