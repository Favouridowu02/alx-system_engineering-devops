#!/usr/bin/python3
"""
    This is a Module that contains a function that queries the Reddit API
    and returns a list containing the titles of all hot articles for a
    given subreddit

    Function_name: recurse
    Usage: recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        A recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.

        Arguments:
            subreddit: the subreddit account name
            hot_list: an array of titles to be returned

        Returns:
            None: it no results are found
            hot_list: array of list containing the tiles of all hot articles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers={"User-Agent": "Custom"}

    response = requests.get(url, headers=headers, params={"after": after},)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        for i in range(0, len(children)):
            child = children[i]["data"]["title"]
            hot_list.append(child)
        after = data["data"]["after"]

        if after is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, after)
    else:
        return None
