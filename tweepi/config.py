# Tw33pi Config File
import random

interests = ['Gaming', 'Riot Games', 'Jeux-vidéos', 'Videogames', 'Coding', 'Health', 'python', 'League of legends',
             'Legends of Runneterra', 'Meme', 'Humour', 'funny', '9gag', 'Reddit', 'Cotonou', 'Medecine',
             'Santé', 'Benin']


# Function to choose what to retweet about, called in retw33t function
def choose_interest():
    chosen_interest = '# ' + random.choice(interests)
    return chosen_interest


# Rate limit to not trigger twitter's sensitivity
rate_limit = 20
# Tw33pi setting for liking Tweets
LIKE = True
# Tw33pi setting for following user who tweeted
FOLLOW = False
# Twitter bot sleep time settings in seconds.
# Use long sleep times to avoid bans
SLEEP_TIME = 600  # 5mins
