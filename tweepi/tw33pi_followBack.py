import tweepy,time
from os import environ as ENV
# using next line for testing environment and above one in deploy environment
from credentials import *
auth = tweepy.OAuthHandler(ENV['consumer_key'], ENV['consumer_secret'])
auth.set_access_token(ENV['access_token'], ENV['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def follow_back():
    print('\nlooking for unfollowed followers')
    followers = api.followers_ids(api.me().id)
    friends = api.friends_ids(api.me().id)

    for follower in followers:
        if follower not in friends:
            try:
                api.create_friendship(follower)
                print('followed ' + api.get_user(follower).screen_name + ' Back')
                time.sleep(60)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break



