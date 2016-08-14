import urllib2
import os.path
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient

account_sid = " " # Your Account SID from www.twilio.com/console
auth_token  = " "  # Your Auth Token from www.twilio.com/console

vtu = "http://results.vtu.ac.in/"
page = urllib2.urlopen(vtu)
soup = BeautifulSoup(page,"html.parser")

complete_text = soup.getText()

if os.path.isfile('rctmp') == True:
	file = open('rctmp','r+')
	flag = file.read(1)
else:
        file = open('rctmp','w')
        file.write('0')
        file = open('rctmp','r+')
        flag = file.read(1)

if flag == "0":
	if complete_text.find(" ")!=-1:  #The text you want to search for | "B.E/B.Tech IV Semester" for 4th sem results
		client = TwilioRestClient(account_sid, auth_token)
         	message = client.messages.create(body=" ",		#Messgage body you want to receive as SMS
				to=" ",   #Replace with your number to which you want to send the message
				from_=" ") # Replace with your Twilio number

        file = open('rctmp','w')
        file.write('1')
