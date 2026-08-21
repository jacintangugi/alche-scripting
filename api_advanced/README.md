# Web Infrastructure - API advanced

Python scripts that query the Reddit API, handle pagination, and
recursively parse and count data from hot post titles.

## Requirements

- Ubuntu 14.04 LTS, python3 (3.4.3)
- `requests` module (`pip3 install requests`)
- PEP 8 style
- A custom `User-Agent` header is required to avoid Reddit rate limits

## Files

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the subscriber count, or 0 if invalid. |
| `1-top_ten.py` | `top_ten(subreddit)` prints the first 10 hot post titles, or `None` if invalid. |
| `2-recurse.py` | `recurse(subreddit)` recursively paginates through all hot posts and returns a list of titles, or `None`. |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keyword occurrences across hot post titles and prints them sorted by count then alphabetically. |

## Usage

```bash
./0-subs.py <subreddit>
./1-top_ten.py <subreddit>
./2-recurse.py <subreddit>
./3-count.py <subreddit> "<keyword1> <keyword2> ..."
```
