#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""

import requests

URL = 'https://www.reddit.com/r/{}/about.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'


def number_of_subscribers(subreddit):
    """
    Query reddit for the number of subscribers to a subreddit
    """
    resp = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        allow_redirects=False,
        timeout=10
    )
    if resp.status_code == 200:
        return resp.json()['data']['subscribers']
    else:
        return 0
