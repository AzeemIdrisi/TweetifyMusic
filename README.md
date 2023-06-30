# TweetifyMusic

TweetifyMusic is a Twitter Bot that automatically tweets your recently played song on Spotify on a manually scheduled basis using GitHub Actions. It leverages the Twitter and Spotify APIs to fetch the latest played song from Spotify and post it on your Twitter account.

## Features

- **Automated tweeting:** TweetifyMusic connects to your Spotify account and retrieves the most recent song you played. It then automatically tweets the song details on your connected Twitter account.

- **Manual scheduling:** You have full control over when the tweets are posted. You can manually schedule the tweets according to your preference using GitHub Actions.

- **Twitter and Spotify API integration:** TweetifyMusic uses the Twitter API to post tweets and the Spotify API to fetch your recently played songs. The integration allows for seamless communication between the two platforms.

## Getting Started (Tutorial is to be completed)

### Prerequisites

To run TweetifyMusic locally, you'll need the following:

- Python 3 installed on your machine
- Twitter API credentials (API key, API secret key, Access token, Access token secret)
- Spotify API credentials (Client ID, Client Secret)

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/AzeemIdrisi/TweetifyMusic.git
   ```

2. Navigate to the project directory:

   ```
   cd TweetifyMusic
   ```

3. Install the required dependencies:

   ```
   pip install spotipy tweepy
   ```

4. Set up API credentials:

   - Obtain your Twitter API credentials by creating a Twitter Developer Account and creating a new app. Note down the API key, API secret key, Access token, and Access token secret.
   - Obtain your Spotify API credentials by creating a Spotify Developer Account and registering a new app. Make sure to retrieve the Client ID and Client Secret.

5. Export environment variables:

   - To keep the API credentials private, export the credentials as environment variables in your system.
   - Add all your keys in your .zshrc/.bashrc by adding these lines at the last. (Note : Do not use quotes with keys, Replace Xs with the actual keys)
     
    ```
   export SPOTIFY_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   export SPOTIFY_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXX
   export TWITTER_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   export TWITTER_API_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   export TWITTER_BEARER_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXX
   export TWITTER_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   export TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   export SPOTIFY_REFRESH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     ```
    
   - Replace the placeholder values with your actual API credentials.

6. Run the bot:

   ```
   python tweetifymusic.py
   ```

   The bot will fetch your recently played song from Spotify and post it on Twitter.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the * License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by the desire to share your favorite music with your Twitter followers effortlessly.
- Thanks to the creators and maintainers of the Twitter API for Python [tweepy](https://github.com/tweepy/tweepy)  and the Spotify API for Python [spotipy](https://github.com/spotipy-dev/spotipy) for providing the necessary tools to develop this bot.

## Developer
[Azeem Idrisi](https://github.com/AzeemIdrisi)
