# slack-echo
You can send messages to slack with a pipe.

# how to use
You have to create "secret.py" in same directory.
Then, write the slack webhock URL as `TOKEN = "WEBHOCK URL". `

```sh
echo "hello" | python3 slackecho.py
```
You can send a message to slack by typing it into the shell like this.
