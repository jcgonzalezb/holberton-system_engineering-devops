#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests

URL = 'https://www.reddit.com/r/{}/hot.json'
USER_AGENT = 'Mozilla/5.0 (Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'


def recurse(subreddit, hot_list=[], **kwargs):
    """
    Query reddit for the the titles of all hot articles
    for a given subreddit. If no results are found for
    the given subreddit, the function should return None.
    """
    params = {
        'after': kwargs.setdefault('after'),
        'count': kwargs.setdefault('count', 0),
        'limit': kwargs.setdefault('limit', 100)
    }

    resp = requests.get(
        URL.format(subreddit),
        headers={'User-Agent': USER_AGENT},
        allow_redirects=False,
        timeout=10,
        params=params
    )
    if resp.status_code == 200:
        results = resp.json()['data']
        hot_list.extend(post['data']['title'] for post in results['children'])
        if results['after'] is not None:
            kwargs['after'] = results['after']
            kwargs['count'] += kwargs['limit']
            return recurse(subreddit, hot_list, **kwargs)
        return hot_list
    return None
