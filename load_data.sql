CREATE TABLE reddit_raw_posts (
    id INT IDENTITY(1,1) PRIMARY KEY,
    subreddit NVARCHAR(255),
    title NVARCHAR(MAX),
    author NVARCHAR(255),
    created_utc DATETIME,
    score INT,
    num_comments INT,
    body NVARCHAR(MAX),
    polarity FLOAT,
    sentiment_category NVARCHAR(20)
);

select * from reddit_raw_posts