import praw
import os
from datetime import datetime

# Read post content
today = datetime.today().strftime('%Y-%m-%d')
post_file = f"posts/{today}.md"

if not os.path.exists(post_file):
    print(f"❌ No post file found for {today}. Skipping...")
    exit()

with open(post_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    title = lines[0].strip().lstrip("#").strip()  # First line is the title
    body = "".join(lines[1:]).strip()  # Rest is body

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    username=os.environ['REDDIT_USERNAME'],
    password=os.environ['REDDIT_PASSWORD'],
    user_agent=os.environ['REDDIT_USER_AGENT']
)

# Post to subreddit
subreddit = reddit.subreddit("test")  # Replace with your subreddit
subreddit.submit(title, selftext=body)
print(f"✅ Posted to r/{subreddit.display_name}: {title}")
