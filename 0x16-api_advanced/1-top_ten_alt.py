#!/usr/bin/python3
"""
    This Module contains a function that queries the Reddit API and
    prints the title of the first 10 hot posts listed for a given
    subreddit

    Function_name: top_ten
"""
import requests


def top_ten(subreddit):
    """
        This function queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit.

        Arguments:
            subreddit: The subreddit account name

        Returns:
            None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("None")
        return
    data = response.json()

    i = 0
    while i < 10:
        print("{}".format(data["data"]["children"][i]["data"]["title"]))
        i += 1
