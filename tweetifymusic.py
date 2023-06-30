import os
import spotipy, tweepy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Part :

spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
spotify_client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-read-recently-played",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri="http://app:8080",
    )
)

data = sp.current_user_recently_played(limit=1)
link = data["items"][0]["track"]["external_urls"]["spotify"]
name = data["items"][0]["track"]["name"]

# Twitter Part :
twitter_api_key = os.environ["TWITTER_API_KEY"]
twitter_api_secret = os.environ["TWITTER_API_SECRET"]
twitter_bearer_token = rf'{os.environ["TWITTER_BEARER_TOKEN"]}'
twitter_access_token = os.environ["TWITTER_ACCESS_TOKEN"]
twitter_access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

user = tweepy.Client(
    bearer_token=twitter_bearer_token,
    consumer_key=twitter_api_key,
    consumer_secret=twitter_api_secret,
    access_token=twitter_access_token,
    access_token_secret=twitter_access_token_secret,
)

auth = tweepy.OAuth1UserHandler(
    consumer_key=twitter_api_key,
    consumer_secret=twitter_api_secret,
    access_token=twitter_access_token,
    access_token_secret=twitter_access_token_secret,
)

api = tweepy.API(auth)


user.create_tweet(text=f"Song : {name}\n\n TweetifyMusic Bot by AzeemIdrisi {link}")
