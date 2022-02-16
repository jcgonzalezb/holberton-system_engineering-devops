#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Query reddit for the titles of the first 10 hot posts listed for a given subreddit.
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'
    USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'

    resp = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        params={'limit': 10},
        allow_redirects=False,
        timeout=10
    )

    if resp.status_code == 200:
        for post in resp.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
