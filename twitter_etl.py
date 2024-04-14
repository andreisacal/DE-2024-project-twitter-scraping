import requests  # Importing the requests library to send HTTP requests
import pandas as pd  # Importing pandas library to work with data in tabular format
from datetime import datetime  # Importing datetime to work with dates and times
import s3fs  # Importing s3fs to interact with Amazon S3 storage
import json  # Importing json to work with JSON data
import sys  # Importing sys module to access system-specific parameters and functions

def run_twitter_etl():

    # Blank list to append the Twitter data once it's collected
    twitter_data = []

    # Set parameters that will dictate how the Twitter search will work
    payload = {
        "api_key":"1c3cbb3fe90460c3cd3b66a873d6e29f", #scraper api key
        "query": "AWS", #twitter search query
        "num": "50" #number of tweets to scrape
    }

    response = requests.get(
        "https://api.scraperapi.com/structured/twitter/search", params=payload
    )

    # Set the GET response to JSON format and save it to a variable
    data = response.json()

    # Iterate through the collected data and append it to the twitter_data list
    all_tweets = data['organic_results']
    for tweet in all_tweets:
        twitter_data.append(tweet)

    # Create a DataFrame from the collected Twitter data for better format
    df = pd.DataFrame(twitter_data)

    # Export the DataFrame as a CSV file named "AWS_twitter_data.csv"
    df.to_csv("s3://andrei-airflow-etl/data/AWS_twitter_data.csv")

    print("Twitter scraped and file saved successfully!")