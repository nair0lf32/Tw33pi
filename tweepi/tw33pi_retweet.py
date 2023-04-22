import tweepy
from time import sleep
from os import environ as ENV
# using next line for testing environment and above one in deploy environment
from credentials import *
from config import FOLLOW, LIKE, SLEEP_TIME, choose_interest, rate_limit

auth = tweepy.OAuthHandler(ENV['consumer_key'], ENV['consumer_secret'])
auth.set_access_token(ENV['access_token'], ENV['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def retw33t():
    QUERY = choose_interest()
    for tweet in tweepy.Cursor(api.search, q=QUERY).items(rate_limit):
        try:
            if tweet.favorite_count >= 100 and (tweet.lang == "en" or tweet.lang == "fr"):
                print('\nlooking for ' + QUERY)
                print('Tweet by: @' + tweet.user.screen_name)
                # retweet
                tweet.retweet()
                print('Retweeted the tweet')
                # like the tweet
                if LIKE:
                    tweet.favorite()
                    print('Liked the tweet')
                    # Follow the user who tweeted if not already following
                if FOLLOW:
                    if not tweet.user.following:
                        tweet.user.follow()
                        print('Followed the user')
                # Now we Choose another interest subject
                QUERY = choose_interest()
                sleep(SLEEP_TIME)
            elif LIKE and (tweet.favorite_count >= 50 and tweet.favorite_count <100)\
                    and (tweet.lang == "en" or tweet.lang == "fr"):
                print('\nlooking for ' + QUERY)
                print('Tweet by: @' + tweet.user.screen_name)
                # just like the tweet
                tweet.favorite()
                print('liked the tweet')
                sleep(SLEEP_TIME)
                # Now we Choose another interest subject
                QUERY = choose_interest()
                sleep(SLEEP_TIME)
            else:
                pass

        except tweepy.TweepError as e:
                print(e.reason)

        except StopIteration:
                break




