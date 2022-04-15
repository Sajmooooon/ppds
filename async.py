import datetime
import asyncio


async def ping(url):
    response = await asyncio.create_subprocess_exec(
                            "ping", url,
                            stdout=asyncio.subprocess.PIPE,
                            stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await response.communicate()
    print(stdout.decode())
    error_message = "Ping request could not find host"

    if error_message not in stdout.decode():
        print(f"{url} was found!\n")
    else:
        print(f"{url} wasn't found!\n")


async def main():
    start = datetime.datetime.now()
    await asyncio.gather(ping("google.com"),
                         ping("facebook.com"),
                         ping("youtube.com"),
                         ping("meet.google.com"))
    end = datetime.datetime.now()

    print(f"--------------------\n"
          f"Time: {(end - start).total_seconds():5.2f} seconds"
          f"\n--------------------")


asyncio.run(main())
