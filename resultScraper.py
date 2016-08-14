import urllib2
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

account_sid = " " # Your Account SID from www.twilio.com/console
auth_token  = " "  # Your Auth Token from www.twilio.com/console

vtu = "http://results.vtu.ac.in/"
page = urllib2.urlopen(vtu)
soup = BeautifulSoup(page)

complete_text = soup.getText()

file = open('rctmp','r+')

flag = file.read(1)

if flag == "0":
    if complete_text.find(" ")!=-1: #The text you want to find, "B.E/B.Tech IV Semester" - For 4th sem results
            client = TwilioRestClient(account_sid, auth_token)
            message = client.messages.create(body="Hey! Your Results are out!",
                            to=" ",   #Replace with your number to which you want to send the message (with Country Code)
                            from_=" ") # Replace with your Twilio number

            file = open('rctmp','w')
            file.write('1')
