import tweepy, datetime, time
from os import environ as ENV
# using next line for testing environment and above one in deploy environment
from credentials import *

auth = tweepy.OAuthHandler(ENV['consumer_key'], ENV['consumer_secret'])
auth.set_access_token(ENV['access_token'], ENV['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

today = datetime.datetime.now()
inactivitytime = 1000  # in days
inactivefriends = []


def unfollow():
    print("\nchecking for inactives")
    friends = api.friends_ids(api.me().id)
    followers = api.followers_ids(api.me().id)

    for friend in friends:
        try:
            timeline = api.user_timeline(friend)
            time.sleep(60)
            if timeline:
                inactivity = today - timeline[0].created_at
            else:
                inactivity = None   # Might rethink this

            if inactivity is not None and friend not in followers and inactivity.days > inactivitytime:
                inactivefriends.append(friend)
                time.sleep(10)

            if inactivefriends:
                for friend in inactivefriends:
                    # unfollow
                    api.destroy_friendship(friend)
                    print('unfollowed ' + api.get_user(friend).screen_name + ' inactive for ' + str(inactivity.days))
                    inactivefriends.remove(friend)
                    time.sleep(60)
            else:
                pass

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
