"""
Tweet application.

Minimal script to post a tweet to the Twitter API using a given message.
"""
import os
import sys

import tweepy


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')


def main(args):
    """
    Command-line entrypoint to post a tweet message to Twitter.
    """
    if not args:
        print("Provide a message on the CLI as the first argument.")
        print("It must a single string. Multiple lines are allowed.")

        return None

    msg = args[0]

    assert all((CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)), \
        "Credentials must be set"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    print(f"Tweeting message: {msg}")
    tweet = api.update_status(msg)


if __name__ == "__main__":
    main(sys.argv[1:])
