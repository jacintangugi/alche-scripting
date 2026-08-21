#!/usr/bin/python3
"""Recursively count keyword occurrences in Reddit hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keyword occurrences in hot post titles.

    Args:
        subreddit (str): the name of the subreddit.
        word_list (list): list of keywords to count (case-insensitive).
        after (str): pagination token for the next page of results.
        counts (dict): accumulator dict mapping keyword to count.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts.setdefault(word.lower(), 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alche_api_advanced:v1.0 (by /u/jacintangugi)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        for token in title.split():
            clean_token = token.lower()
            if clean_token in counts:
                counts[clean_token] += 1

    after = data.get("after")
    if after and posts:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0]))
    for word, word_count in sorted_counts:
        if word_count > 0:
            print("{}: {}".format(word, word_count))
