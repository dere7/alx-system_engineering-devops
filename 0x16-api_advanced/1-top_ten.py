#!/usr/bin/python3
"""contains a function that returns top ten hot posts"""
import requests


def top_ten(subreddit):
    """returns top tens"""
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit),
        headers={'User-agent': 'cli:api_advanced:v1.0.0 (by /u/dereje77'},
        allow_redirects=False)
    if r.status_code != 200:
        return None
    for post in r.json().get('data').get('children'):
        print(post['data']['title'])
