#!/usr/bin/env python

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient #Twilio rest API need install sudo pip install twilio
 
# Find these values at https://twilio.com/user/account
account_sid = "__ACbde3ae0895cf6e2836c27db1356e84be" #Unique for each account equivalent to twilio username
auth_token = "__b2466fc7618a64d73c85ae12d9c9a4fe"   #unique to twilio account password
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+977984317589", from_="+16066539735",
                                     body="Hello Bhusan Dai, Best of Luck for EXAM!")
