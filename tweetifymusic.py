import os
import spotipy, tweepy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Part :

from spotipy.oauth2 import SpotifyOAuth
client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
refresh_token = os.environ["SPOTIFY_REFRESH_TOKEN"]


# Spotify Part :
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri="http://127.0.0.1:8080/callback",
                        scope="user-read-recently-played",
                        cache_path='token.txt')  # Path to store the token

# Use the refresh token to get a new access token
token_info = sp_oauth.refresh_access_token(refresh_token)
access_token = token_info['access_token']

# Create a Spotipy client with the access token
sp = spotipy.Spotify(auth=access_token)
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
