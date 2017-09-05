#!/bin/python

import random

def AccountPicker():
	account_information = {}

	account_information['isaaccow5@yahoo.com'] = 'abc123abc'
	account_information['osrschecker1@gmail.com'] = 'abc123abc'
	account_information['osrschecker2@gmail.com'] = 'abc123abc'
	account_information['osrschecker3@gmail.com']= 'abc123abc'

	random_account = random.choice(list(account_information))
	return random_account +"|"+account_information[random_account]
