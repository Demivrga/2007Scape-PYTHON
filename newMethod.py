#!/bin/python
import requests
import json
from random import randint
from time import sleep

swear = ["homo", "fucc", "nigger", "bitch", "penis", "pussy", "fuck", "asshole", "bastard", "damn", "shit", "cock", "slut", "douche"]

def checkUsername(username):
    print(username)
    try:
        sleep(randint(0, 5))
        url = 'https://secure.runescape.com/m=account-creation/g=oldscape/check_displayname.ajax'
        data ={'displayname': username}
        headers = {'Referer': 'https://secure.runescape.com/m=account-creation/g=oldscape/create_account?trialactive=true'}
        r = requests.post(url, data=data, headers=headers)
        data = r.text.strip()
        data = json.loads(data)
        data = data["displayNameIsValid"]
    except:
        return "ERR"

    if data == "false":
        return "NOK"
    if data == "true":
        for line in swear:
            if line in username.lower():
                return "UGLY"
        return "OK"
    if data == "":
        return "ERR"
    else:
        return "ERR"
