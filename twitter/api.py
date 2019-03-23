"""Tweepy API factory."""

import os
import tweepy
import dotenv

dotenv.load_dotenv()


def create_api():
    auth = tweepy.OAuthHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
    )
    auth.set_access_token(
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET")
    )
    return tweepy.API(auth)
