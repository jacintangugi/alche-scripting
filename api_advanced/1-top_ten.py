#!/usr/bin/python3
"""Query the Reddit API and print the top ten hot post titles."""
import time

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alche_api_advanced:v1.0 (by /u/jacintangugi)"}
    params = {"limit": 10}

    response = None
    for _ in range(3):
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 429:
            time.sleep(2)
            continue
        break

    if response is None or response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
