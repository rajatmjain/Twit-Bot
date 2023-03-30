# Twit-Bot

Twit-Bot is a Python script that uses the Tweepy library to like and retweet tweets that contain a specific hashtag.

## Requirements

To use Twit-Bot, you need to have the following:

- Python 3 installed on your machine
- Tweepy library installed (can be installed using pip)
- Twitter API keys and access tokens

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/rajatmjain/Twit-Bot.git
```

2. Install the required packages:

```
pip install tweepy
```

3. Create a Twitter developer account and create an app to get the API keys and access tokens.

4. Update the script with your Twitter API keys and access tokens.

## Usage

To use Twit-Bot, run the following command in your terminal:
```
python twitBot.py
```


The script will prompt you to enter a hashtag and the number of tweets you wish to like. It will then like and retweet the tweets that match the hashtag.

## Customization

You can customize the script by changing the hashtag and the number of tweets you wish to like/retweet. You can also modify the time delay between likes/retweets by changing the `time.sleep()` parameter in the script.

## Acknowledgments

This project was inspired by [this tutorial](https://realpython.com/twitter-bot-python-tweepy/#what-is-a-twitter-bot) by Real Python.


