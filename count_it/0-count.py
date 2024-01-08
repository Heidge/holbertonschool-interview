#!/usr/bin/python3
"""Module to count the occurrences of words in the titles of hot posts"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Count occurrences of specific words in the titles of posts from a Reddit subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to search for in post titles.
        after (str, optional): A parameter for pagination in Reddit API.
        counts (dict, optional): A dictionary to store the counts of each word.

    Returns:
        None: The results are printed, and counts are stored in the 'counts' parameter.
    """
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'YourUserAgent'}  # Add your own User-Agent header

    params = {'t': 'day', 'limit': 100, 'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    if response.status_code != 200:
        print(f"Error: Invalid subreddit or no posts match (Status Code: {response.status_code})")
        return

    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        print("Error: Invalid response format from Reddit API.")
        return

    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            keyword = word.lower()
            if keyword in title:
                counts[keyword] = counts.get(keyword, 0) + 1

    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_results(counts)

def print_results(counts):
    """
    Print the word counts in descending order.

    Args:
        counts (dict): A dictionary containing word counts.

    Returns:
        None: The results are printed.
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

