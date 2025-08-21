Reddit Data Pipeline & Dashboard
📌 Project Overview

This project demonstrates an end-to-end data pipeline to extract, process, and visualize Reddit post data.
We integrate multiple tools (SQL Server, AWS services, and Power BI) to build a real-world data engineering workflow.

The pipeline covers:

Data extraction from Reddit API

Staging & preprocessing in SQL Server

Storage in Amazon S3

Data cataloging & transformation with AWS Glue

Querying with Amazon Athena

Visualization in Power BI

🏗️ Architecture

Reddit API → Extract raw post data (title, body, author, score, comments, polarity, etc.).

Python → Clean & transform JSON data into structured format.

SQL Server → Store structured data for staging & transformations.

Amazon S3 (Raw Zone) → Offload SQL data into S3 buckets for scalable storage.

AWS Glue → Create a catalog & apply ETL transformations.

Amazon Athena → Query transformed data directly from S3.

Amazon S3 (Curated Zone) → Store processed/cleaned data for analytics.

Power BI → Build interactive dashboards for engagement & sentiment analysis.

🛠️ Tools & Technologies

Reddit API – Data Source

Python (Pandas, Requests) – Data extraction & cleaning

SQL Server – Staging database

Amazon S3 – Data lake (raw + curated zones)

AWS Glue – Data catalog & ETL

Amazon Athena – Query engine

Power BI – Visualization

📊 Dashboard Visuals

Posts Trend Over Time

Top Subreddits by Engagement

Engagement KPIs (Posts, Comments, Score)

Sentiment Distribution (Positive/Negative/Neutral)

Sentiment Trend Over Time

Subreddit-wise Sentiment Breakdown

Top Posts by Score

Engagement Analysis (Score vs Comments)

🔍 Findings

Positive sentiment posts generally attract more comments.

Some subreddits show consistently higher engagement.

Score and number of comments are positively correlated.

Posting time/day impacts visibility and interaction.

High polarity + active subreddit = maximum engagement.

🎯 Outcomes

✔ Built a complete ETL + Analytics pipeline
✔ Learned AWS cloud data engineering workflow
✔ Delivered insights on engagement & sentiment
✔ Created a portfolio-ready case study
