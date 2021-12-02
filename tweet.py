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


def setup_conn() -> None:
    """
    Return API connection object.
    """
    assert all((CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)), \
        "All credentials must be set"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    
    return tweepy.API(auth)


def post_tweet(msg: str) -> None:
    api = setup_conn()

    print(f"Tweeting message:")
    print(msg)

    tweet = api.update_status(msg)
    print(tweet)


def main(args: list[str]) -> None:
    """
    Command-line entrypoint to post a tweet message to Twitter.
    """
    if not args:
        print("Provide a message on the CLI as the first argument.")
        print("It must be a single string. Multiple lines are allowed.")

        sys.exit(1)

    msg = args[0]
    if not msg:
        print("Message must not be an empty value")
        sys.exit(1)

    post_tweet(msg)


if __name__ == "__main__":
    main(sys.argv[1:])
