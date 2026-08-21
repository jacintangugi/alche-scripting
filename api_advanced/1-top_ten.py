#!/usr/bin/python3
"""Query the Reddit API and print the top ten hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit.
    """
    headers = {"User-Agent": "alche_api_advanced:v1.0 (by /u/jacintangugi)"}
    params = {"limit": 10}

    for domain in ("https://www.reddit.com", "https://old.reddit.com"):
        url = "{}/r/{}/hot.json".format(domain, subreddit)
        try:
            response = requests.get(
                url, headers=headers, params=params,
                allow_redirects=False, timeout=10)
        except requests.exceptions.RequestException:
            continue

        if response.status_code != 200:
            continue

        try:
            posts = response.json().get("data", {}).get("children", [])
        except ValueError:
            continue

        if posts:
            for post in posts:
                print(post.get("data", {}).get("title"))
            return

    print(None)
