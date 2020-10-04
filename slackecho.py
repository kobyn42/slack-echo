import requests
import json
import secret
import sys


def say(text):
    WEB_HOCK_URL = secret.TOKEN
    post_data = json.dumps({
        "text": "{}".format(text),
        "username": "home bot",
        "icon_emoji": "robot_face",
        "link_names": 1,
    })
    requests.post(WEB_HOCK_URL, post_data)


def main():
    if 1 < len(sys.argv):
        print("too many arguments...", file=sys.stderr)
        say("faild to send messages...")
        exit(1)

    text = sys.stdin.read()
    say(text)


if __name__ == "__main__":
    main()
