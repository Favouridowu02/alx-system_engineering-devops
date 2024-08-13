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
            subreddit: this is the subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {'User-Agent': 'Custom'}

    response = requests.get(url.format(subreddit), headers)
    data = response.json()

    if response.status_code != 200:
        return 0
    else:
        return data["data"]["subscribers"]
