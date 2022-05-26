from webserver import keep_alive
import requests

channelID = 915943507141730346
headers = {
    "authorization":
    "{"872074930689310730":"ODcyMDc0OTMwNjg5MzEwNzMw.GiK60r.gm0zneqAdT9uJDlgaDGOoVEYWp31fIKlwUn5-4"}"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
