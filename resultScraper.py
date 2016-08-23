import os.path
from pymongo import MongoClient
import pymongo
from collections import OrderedDict
from helpers import insert_section_results
from twilio.rest import TwilioRestClient

account_sid = " " # Your Account SID from www.twilio.com/console
auth_token  = " "  # Your Auth Token from www.twilio.com/console
usn = "" # Your USN

#result = student_results()
insert_section_results()
'''
client = MongoClient(document_class=OrderedDict)
db = client.results
db.students.ensure_index('usn', unique=True)
db.students.insert_one(result)



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
