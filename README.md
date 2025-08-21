# Reddit Data Pipeline & Dashboard

## Business Problem
The business problem addressed is the need to analyze and derive actionable insights from social media engagement and sentiment on Reddit to enhance marketing strategies, content creation, and community management. Companies often struggle to understand user behavior, identify trending topics, and gauge public sentiment toward their brand or industry. This project aims to provide a scalable solution to monitor engagement metrics and sentiment trends, enabling data-driven decision-making.

## Technology Used
- **Reddit API**: Used to extract raw post data (title, body, author, score, comments, polarity, etc.) for real-time data collection.
- **Python (Pandas, Requests)**: Employed for data cleaning and transformation of JSON data into a structured format, leveraging its powerful data manipulation libraries.
- **SQL Server**: Utilized as a staging database to store and preprocess structured data efficiently.
- **Amazon S3**: Chosen for scalable storage of raw and curated data, providing a cost-effective data lake solution.
- **AWS Glue**: Applied for data cataloging and ETL transformations, automating the process with serverless architecture.
- **Amazon Athena**: Used for querying transformed data directly from S3, offering a serverless SQL query engine.
- **Power BI**: Selected for building interactive dashboards, enabling visualization of complex data for business users.

## Benefits to Business
- **Improved Marketing Insights**: Identifying high-engagement subreddits and positive sentiment trends helps target marketing campaigns effectively.
- **Content Optimization**: Understanding which topics (e.g., informative posts) drive engagement allows for better content planning.
- **Sentiment Analysis**: Monitoring sentiment shifts aids in managing brand reputation and responding to negative feedback proactively.
- **Cost Efficiency**: The use of cloud-based AWS services (S3, Glue, Athena) reduces infrastructure costs while scaling with data volume.
- **Real-Time Decision Making**: The pipeline and dashboard provide timely insights, enabling quick strategic adjustments.

## Visualizations and Rationale
- **Posts Trend Over Time**: A line chart is used to show engagement trends over time, helping identify peak activity periods for scheduling content.
- **Top Subreddits by Engagement**: A bar chart visualizes the highest-engaged subreddits, aiding in targeting specific communities.
- **Engagement KPIs (Posts, Comments, Score)**: Cards and KPIs display key metrics, providing a quick overview of performance indicators.
- **Sentiment Distribution (Positive/Negative/Neutral)**: A pie chart breaks down sentiment proportions, offering a clear view of overall sentiment balance.
- **Sentiment Trend Over Time**: A line chart tracks sentiment changes, useful for spotting long-term sentiment shifts.
- **Subreddit-wise Sentiment Breakdown**: A stacked bar chart compares sentiment across subreddits, highlighting community-specific attitudes.
- **Top Posts by Score**: A bar chart ranks top posts, revealing what content resonates most with users.
- **Engagement Analysis (Score vs Comments)**: A scatter plot correlates score and comments, showing how emotional polarity drives discussion.
