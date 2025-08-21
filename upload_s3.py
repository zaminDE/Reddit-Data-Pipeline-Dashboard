import pyodbc
import pandas as pd
import boto3
from io import StringIO
import os

# 🔹 Step 1: Connect to SQL Server
conn_str = (
    r"DRIVER={SQL Server};"
    r"SERVER=DESKTOP-3642QNU;"         
    r"DATABASE=master;"                
    r"Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)

# 🔹 Step 2: Read data from SQL Server into a DataFrame
query = "SELECT * FROM reddit_raw_posts"   
df = pd.read_sql(query, conn)
conn.close()

# 🔹 Step 3: Convert to CSV (in-memory)
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# 🔹 Step 4: Upload to S3 using boto3
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_name = 'redditpipelinemz'
object_key = 'raw/reddit_posts.csv'              

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

s3.put_object(Bucket=bucket_name, Key=object_key, Body=csv_buffer.getvalue())

print("✅ Data uploaded to S3 successfully!")