import tw33pi_retweet, tw33pi_followBack, tw33pi_unfollowinactives
from config import FOLLOW, LIKE


def tw33p():
    print("Tw33pi")
    print("Bot Settings:")
    print("Like Tweets :", LIKE)
    print("Follow users :", FOLLOW)

def retweep():
    tw33pi_retweet.retw33t()


def followBacc():
    tw33pi_followBack.follow_back()


def yeetInactives():
    tw33pi_unfollowinactives.unfollow()


if __name__ == '__main__':
    tw33p()
    retweep()


