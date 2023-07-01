# TweetifyMusic

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/AzeemIdrisi/TweetifyMusic/main.yml?logo=github)

![Static Badge](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)



TweetifyMusic is a Twitter bot that automatically tweets your recently played song on Spotify on a manually scheduled basis using **GitHub Actions**. It leverages the Twitter and Spotify APIs to fetch the latest played song from Spotify and post it on your Twitter account.

## Features

- **Automated tweeting:** TweetifyMusic connects to your Spotify account and retrieves the most recently played song. It then automatically tweets the song details on your connected Twitter account.

- **Manual scheduling:** You have full control over when the tweets are posted. You can manually schedule the tweets according to your preference using GitHub Actions.

- **Twitter and Spotify API integration:** TweetifyMusic uses the Twitter API to post tweets and the Spotify API to fetch your recently played songs. The integration allows for seamless communication between the two platforms.

## Getting Started

### Prerequisites

To run TweetifyMusic locally, you'll need the following:

- **Python3** installed on your machine
- Python libraries: [`spotipy`](https://github.com/spotipy-dev/spotipy) and [`tweepy`](https://github.com/tweepy/tweepy)
- **Twitter API** credentials (API key, API secret key, Access token, Access token secret, Bearer token)
- **Spotify API** credentials (Client ID, Client Secret)

### Getting the Spotify refresh_token

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

4. Set up Spotify API credentials:

   - Obtain your **Spotify API credentials** by creating a **Spotify Developer Account**, registering a **new app**, and using a **Redirect URI** - `http://127.0.0.1:8080/callback`. Make sure to retrieve the **Client ID** and **Client Secret** and store them in a secure text file.

5. Edit the **get_refresh_token.py** file:

   - Paste the Client ID and Client Secret in this file and run the file:
      ```
      python3 get_refresh_token.py
      ```
   - A webpage for Spotify App Authorization will open. Approve it.
   - Store the **refresh_token** in a secure text file.

### Testing TweetifyMusic on your local machine

1. Set up Twitter API credentials:
    - Obtain your **Twitter API credentials** by creating a **Twitter Developer Account** and creating a **new app**. Note down the **API key, API secret key, Bearer token, Access token, and Access token secret**.

2. Edit the **tweetifymusic.py** OR Export **environment variables**:

   - For running TweetifyMusic locally, you have **2 choices**. Follow whichever you find easier:
      - **Option 1** - Edit the **tweetifymusic.py**:
         - Replace `os.environ["KEY_NAME"]` with your API credentials as strings.
         - For example:
         
             Change `client_id = os.environ["SPOTIFY_CLIENT_ID"]`
           to `client_id = "123yiuh47fguyer47546562c8476865485644bghf78"`
    
      - **Option 2** - Export API keys as **environment variables**:    
         - To keep the API credentials private, export the credentials as environment variables in your system.
         - Add all your keys in your .zshrc/.bashrc by adding these lines at the end. (**Note**: Do not use double quotes with keys)
           
          ```
         export

 SPOTIFY_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         export SPOTIFY_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXX
         export TWITTER_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         export TWITTER_API_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         export TWITTER_BEARER_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXX
         export TWITTER_ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         export TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         export SPOTIFY_REFRESH_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
           ```
          
     - Replace the placeholder values with your actual API credentials.

3. Run the bot:

   ```
   python3 tweetifymusic.py
   ```

   The bot will fetch your recently played song from Spotify and post it on Twitter.
   
   > If TweetifyMusic manages to tweet your recently played song on Spotify when run on a local machine, then you can proceed to set up the GitHub Action to automate it.
   
### Setting up TweetifyMusic GitHub Action

Schedule the tweets using **GitHub Actions**:

- Fork this repository to your GitHub account.
- Add the Spotify and Twitter API credentials as **new secrets** in your repository.
  
You can find this in your repository under:

Repository Settings -> Security -> Secrets and Variables -> Actions -> **New repository secret**.

Now add all your API credentials one by one with the following names:

| Name  | Secret (without double quotes) |
| ------------- | ------------- |
| SPOTIFY_CLIENT_ID  | Paste your API credential here without quotes |
| SPOTIFY_CLIENT_SECRET | Paste your API credential here without quotes |
| SPOTIFY_REFRESH_TOKEN | Paste your API credential here without quotes |
| TWITTER_ACCESS_TOKEN  | Paste your API credential here without quotes |
| TWITTER_ACCESS_TOKEN_SECRET |  Paste your API credential here without quotes |
| TWITTER_API_KEY |  Paste your API credential here without quotes |
| TWITTER_API_SECRET  | Paste your API credential here without quotes |
| TWITTER_BEARER_TOKEN  | Paste your API credential here without quotes |

This will save your API credentials which are only visible to you.

- The default workflow will run once every 24 hours. To change it, edit the **TweetifyMusic/.github/workflows/main.yml** and edit `- cron: '0 */24 * * *'`.

- Go to the **Actions** tab of the repository and run the workflow.
  
## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the * License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by the desire to share your favorite music with your Twitter followers effortlessly.
- Thanks to the creators and maintainers of the Twitter API for Python [tweepy](https://github.com/tweepy/tweepy) and the Spotify API for Python [spotipy](https://github.com/spotipy-dev/spotipy) for providing the necessary tools to develop this bot.


# Developer

<a href="https://github.com/azeemidrisi/">
  <img src="https://contrib.rocks/image?repo=azeemidrisi/tweetifymusic" />
</a>


**Mohd Azeem** - [@AzeemIdrisi](https://github.com/azeemidrisi/)
 

# Support Me

<a href="https://www.buymeacoffee.com/AzeemIdrisi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>