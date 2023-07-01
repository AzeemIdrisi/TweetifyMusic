import os
from spotipy.oauth2 import SpotifyOAuth

# Spotify Part :

client_id = "Paste your spotify client_id here as a string"
client_secret = "Paste your spotify client_secret here as a string"

sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:8080/callback",
    scope="user-read-recently-played",
    cache_path="token.txt",  # Path to store the token
)
token = sp_oauth.get_access_token()
refresh_token = token["refresh_token"]


print("\n\nPlease copy your refresh_token somewhere safe : \n\n")
print(refresh_token)

with open("refresh_token.txt", "w") as file:
    file.write(refresh_token)
