#!/usr/bin/python3
"""contains a function that returns the number of subscirbers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscirbers"""
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit),
        headers={'User-agent': 'cli:api_advanced:v1.0.0 (by /u/dereje77'},
        allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json().get('data').get('subscribers')
