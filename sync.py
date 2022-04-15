"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Implementation of the simple sync ping function.
"""


import os
import datetime


def ping(url):
    """
    Function to ping given url and print if was found or not.

    Parameter:
        url: URL link of website.
    """

    response = os.system(f"ping {url}")
    if response == 0:
        print(f"{url} was found!\n")
    else:
        print(f"{url} wasn't found!\n")


def main():
    """This function is for program initialization."""

    urls = ["google.com", "facebook.com", "youtube.com", "meet.google.com"]

    start = datetime.datetime.now()
    for i in urls:
        ping(i)
    end = datetime.datetime.now()

    print(f"--------------------\n"
          f"Time: {(end - start).total_seconds():5.2f} seconds"
          f"\n--------------------")


main()
