import urllib2
import os.path
from lxml import etree, html
import requests


#from twilio.rest import TwilioRestClient

#account_sid = " " # Your Account SID from www.twilio.com/console
#auth_token  = " "  # Your Auth Token from www.twilio.com/console
usn = "1MV14IS045" # Your USN
BASE_URL = 'http://results.vtu.ac.in'
#using lxml to access data through xpath selectors

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'results.vtu.ac.in',
    'Referer': 'http://results.vtu.ac.in/'
}

payload = {
    'rid': usn,
    'submit': 'SUBMIT'
}

response = requests.post(BASE_URL + '/vitavi.php', payload, headers=headers)

tree = html.fromstring(response.content)

student_name_usn = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/b/text()')


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
