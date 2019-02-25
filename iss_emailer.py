# learning: APIs, automating email and string functions

import requests
from gmail_function import gmail_function
from iss_pass_function import iss_pass_function

# calling the open-notify API
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
x = data['people']

# constructing the message
message = ("""\
Subject: ISS Personnel Update!

There are currently {} people on the ISS!
They are: \n
""").format(len(x))

for i in x:
    message += i['name']
    message += ' '
    message += i['craft']
    message += '\n'

# user input for ISS pass checking
check = input("Would you like to know when the next pass of the ISS will occur? y/n:")
if check == 'y':
    lat = input("Please input the latitude of your location to two decimal places:")
    lon = input("please input the longitude of your location to two decimal places:")
    nextPass = iss_pass_function(lat, lon)
    message += '\n'
    message += nextPass

# user input for emailing
sender_email = input("Please insert the email account of the sender:")
password = input("Please insert the password for this account:")
receiver_email = input("Please insert the email account of the receiver:")

# calling a wrapper function to send an email
gmail_function(password, sender_email, receiver_email, message)
