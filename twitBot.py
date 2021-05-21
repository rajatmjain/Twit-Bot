import tweepy
import time

class TwitBot:
    auth = tweepy.OAuthHandler('<CONSUMER_API-KEY>', 'CONSUMER_API-SECRET')
    auth.set_access_token('<BEARER-TOKEN>','')
    auth.access_token = '<ACCESS-TOKEN>'
    auth.access_token_secret = '<ACCESS-SECRET>'
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    user = api.me()

    # Get all followers names
    def getAllFollower(self):
        for follower in tweepy.Cursor(self.api.followers).items():
            print(follower.name)

    #Search tweets and like them
    def likeTweet(self,hashtag,noOfTweets):

        for tweet in tweepy.Cursor(self.api.search,hashtag).items(noOfTweets):
            try:
                print('Tweet liked')
                tweet.favorite()
                time.sleep(10)
            except tweepy.TweepError as err:
                print(e.reason)
            except StopIteration:
                break

    #Search tweets and retweet them
    def retweet(self,hashtag,noOfTweets):
        for tweet in tweepy.Cursor(self.api.search,hashtag).items(noOfTweets):
            try:
                print('Retweeted')
                tweet.retweet()
                time.sleep(10)
            except tweepy.TweepError as err:
                print(e.reason)
            except StopIteration:
                break


bot = TwitBot()
bot.likeTweet(input('Enter a hashtag: #'),int(input('Enter the number of tweets you wish to like: ')))
