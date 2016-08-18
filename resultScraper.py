import urllib2
import os.path
from lxml import etree, html
import requests
from student import Student

#from twilio.rest import TwilioRestClient

#account_sid = " " # Your Account SID from www.twilio.com/console
#auth_token  = " "  # Your Auth Token from www.twilio.com/console
usn = "1MV14IS045" # Your USN
#using lxml to access data through xpath selectors

Sharath = Student()
print Sharath.get_name()
'''
if os.path.isfile('rctmp') == True:
	file = open('rctmp','r+')
	flag = file.read(1)
else:
        file = open('rctmp','w')
        file.write('0')
        file = open('rctmp','r+')
        flag = file.read(1)

if flag == "0":
	if complete_text.find("Results are not yet available")==-1:
		client = TwilioRestClient(account_sid, auth_token)

		message = client.messages.create(body=" ",		#Messgage body you want to receive as SMS
			to=" ",   #Replace with your number to which you want to send the message
			from_=" ") # Replace with your Twilio number
		file = open('rctmp','w')
		file.write('1')
'''
