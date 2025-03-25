# scraper.py# scraper.py
import tweepy
import pandas as pd

# Twitter API credentials
API_KEY = "voffnFpuMCUGsfsktxKYBAOKl"
API_SECRET = "YVfloVkk8nqe3NRPfHtAnfXOGDU3JAgr43aHR2QxvN6YWi7pb1"
ACCESS_TOKEN = "1551891624665690112-OYnk62cZg9zoTOx1m10LvmcSUXaZZ2"
ACCESS_TOKEN_SECRET = "O7ybO0TPAXhvNkYzb9ZFxFLwMbZ593oadWhAMMWNBSpnO"

def scrape_tweets(keyword, start_date, end_date, limit):
    try:
        # Set up OAuth 1.0a authentication
        auth = tweepy.OAuth1UserHandler(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        # Create Client for v2 endpoints
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

        # Build query
        query = f"{keyword} -is:retweet"
        tweets_list = []

        # Use paginator for Twitter API v2
        for tweet in tweepy.Paginator(
            client.search_recent_tweets,
            query=query,
            start_time=f"{start_date}T00:00:00Z",
            end_time=f"{end_date}T23:59:59Z",
            tweet_fields=['created_at', 'public_metrics', 'lang', 'source'],
            user_fields=['username'],
            expansions=['author_id'],
            max_results=100
        ).flatten(limit=limit):
            user = tweet.author_id
            tweets_list.append({
                'date': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'id': tweet.id,
                'url': f"https://twitter.com/{user}/status/{tweet.id}",
                'content': tweet.text,
                'user': user,
                'reply_count': tweet.public_metrics['reply_count'],
                'retweet_count': tweet.public_metrics['retweet_count'],
                'language': tweet.lang,
                'source': tweet.source,
                'like_count': tweet.public_metrics['like_count']
            })

        if not tweets_list:
            raise ValueError("No tweets found for the given criteria")
        
        return pd.DataFrame(tweets_list)
    
    except Exception as e:
        raise Exception(f"Error scraping tweets: {str(e)}")
