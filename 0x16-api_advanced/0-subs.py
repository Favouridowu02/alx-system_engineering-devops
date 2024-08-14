#!/usr/bin/python3
"""
    This Module contains a function That queries the reddit API
    and returns the number of subscribers.

    Function_name: name_of_subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
        This function queries the reddit api and tries to list the
        total amount of subscribers. It retunrs zero if no
        subrredit is given

        Arguments:
            subreddit: the name of the subreddit

        Returns:
            int: The number of subscribers, or 0 if the subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom'}

    response = requests.get(url, headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data["data"]["subscribers"]
