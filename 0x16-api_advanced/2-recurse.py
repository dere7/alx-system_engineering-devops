#!/usr/bin/python3
"""contains a function that returns top ten hot posts"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns top tens"""
    headers = {
        'User-agent': 'cli:api_advanced:v1.0.0 (by /u/dereje77'
    }
    if after is None:
        return hot_list

    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     params={'limit': 100, 'after': after},
                     headers=headers,
                     allow_redirects=False)
    if r.status_code != 200:
        return None
    json = r.json()
    for post in json['data']['children']:
        hot_list.append(post['data']['title'])
    return recurse(subreddit, hot_list, json['data']['after'])
