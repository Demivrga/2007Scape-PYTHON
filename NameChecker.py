#!/bin/python

#### IF YOU ARE READING THIS
#### THIS IS AN OLDER VERSION OF THE 2007SCAPE PYTHON CHECKER
#### PLEASE SEE NEWMETHOD

import sys
import os
import twill
import account
import subprocess
browser = twill.commands.browser

letters = {}
releasednames = []
letters["a"]="released1"
letters["b"]="released2"
letters["c"]="released3"
letters["d"]="released4"
letters["e"]="released5"
letters["f"]="released6"
letters["g"]="released7"
letters["h"]="released8"
letters["i"]="released9"
letters["j"]="released10"
letters["k"]="released11"
letters["l"]="released12"
letters["m"]="released13"

def Builder(username):
    subprocess.call("/home/Runescape/cleanup.sh", shell=True)
    Account = account.AccountPicker()
    Account = Account.split('|')
    print("Using account: "+Account[0])
    twill.commands.go("https://secure.runescape.com/m=weblogin/loginform.ws?mod=displaynames&ssl=1&expired=0&dest=check_name.ws?displayname="+username.strip())
    twill.commands.fv("1", "login-username", Account[0])
    twill.commands.fv("1", "login-password", Account[1])
    twill.commands.submit()
    status = browser.get_html()
    status = status.strip()

    if status == "NOK":
        letter = username[:1]
        letter = letter.lower()
        if letter in letters:
            print(username)
            print("LETTER: "+letters[letter])
            released = open("/home/Runescape/RELEASED/"+letters[letter], "r+")
            for line in released:
                line = line.strip().lower()
                releasednames.append(line)
            released.close()
            if username.strip().lower() in releasednames:
                print("FOUND IN RELEASED!")
                return "RNOK"
            else:
                return(status)
        else:
            return(status)

    return(status)
