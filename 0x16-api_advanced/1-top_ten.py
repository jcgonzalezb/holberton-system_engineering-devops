#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests

URL = 'https://www.reddit.com/r/{}/{}.json?limit={}&t={}'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
subreddit = 'python'
listing = 'hot'
limit = 10
timeframe = 'month'


def top_ten(subreddit):
    """
    Query reddit for the titles of the first 10 hot posts listed for a given subreddit.
    """
    resp = requests.get(
        URL.format(subreddit, listing, limit, timeframe),
        headers={'User-Agent': USER_AGENT},
        allow_redirects=False,
        timeout=10
    )

    if resp.status_code == 200:
        r = resp.json()
        for post in r['data']['children']:
            print(post['data']['title'])
    else:
        return print(None)
