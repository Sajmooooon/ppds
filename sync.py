import os
import datetime


def ping(url):
    response = os.system(f"ping {url}")
    if response == 0:
        print(f"{url} was found!\n")
    else:
        print(f"{url} wasn't found!\n")


def main():
    urls = ["google.com", "facebook.com", "youtube.com", "meet.google.com"]

    start = datetime.datetime.now()
    for i in urls:
        ping(i)
    end = datetime.datetime.now()

    print(f"--------------------\n"
          f"Time: {(end - start).total_seconds():5.2f} seconds"
          f"\n--------------------")


main()
