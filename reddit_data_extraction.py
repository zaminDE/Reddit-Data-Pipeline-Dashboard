import requests
import pandas as pd
import pyodbc
from datetime import datetime, timezone
from textblob import TextBlob
import csv

# 🔹 Step 1: Fetch Reddit Data
url = "https://www.reddit.com/r/dataengineering/hot.json?limit=50"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
data = response.json()

# 🔹 Step 2: Process into DataFrame
posts = []
for post in data['data']['children']:
    p = post['data']
    posts.append({
        'subreddit': p['subreddit'],
        'title': p['title'],
        'author': p['author'],
        'created_utc': datetime.fromtimestamp(p['created_utc'], tz=timezone.utc),
        'score': p['score'],
        'num_comments': p['num_comments'],
        'body': p.get('selftext', '')
    })

df = pd.DataFrame(posts)

# 🔹 Step 3: Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = 'positive'
    elif polarity < -0.1:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return pd.Series([polarity, sentiment])

df[['polarity', 'sentiment_category']] = df['body'].apply(get_sentiment)

# 🔹 Step 4: Connect to SQL Server (Windows Auth)
conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=DESKTOP-3642QNU;"      
    r"DATABASE=master;"             
    r"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# ⚠️ OPTIONAL: If table doesn't have these new columns, create or alter accordingly:
# ALTER TABLE reddit_raw_posts ADD polarity FLOAT, sentiment_category NVARCHAR(20)

# 🔹 Step 5: Insert Data into reddit_raw_posts table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reddit_raw_posts
        (subreddit, title, author, created_utc, score, num_comments, body, polarity, sentiment_category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row['subreddit'], row['title'], row['author'], row['created_utc'],
         row['score'], row['num_comments'], row['body'],
         row['polarity'], row['sentiment_category'])

conn.commit()
cursor.close()
conn.close()

print("✅ Reddit data with sentiment inserted into SQL Server successfully!")

df.to_csv("reddit_cleaned.csv", index=False, quoting=csv.QUOTE_ALL)
print("✅ Cleaned data saved to 'reddit_cleaned.csv' with proper quoting.")
