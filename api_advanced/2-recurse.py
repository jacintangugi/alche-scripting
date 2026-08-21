#!/usr/bin/python3
"""Recursively query the Reddit API for all hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Return a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit.
        hot_list (list): accumulator list of titles gathered so far.
        after (str): pagination token for the next page of results.
        count (int): number of posts already fetched.

    Returns:
        list: all hot post titles, or None if the subreddit is invalid
            or has no results.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alche_api_advanced:v1.0 (by /u/jacintangugi)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    posts = data.get("children", [])
    if not posts and count == 0:
        return None

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after, count + len(posts))
