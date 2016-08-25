import os.path
from pymongo import MongoClient
import pymongo
from collections import OrderedDict
from helpers import insert_region_results_multithreaded
from twilio.rest import TwilioRestClient
import threading



account_sid = " " # Your Account SID from www.twilio.com/console
auth_token  = " "  # Your Auth Token from www.twilio.com/console
usn = "" # Your USN



BENGALURU_COLLEGE_CODES = ['1mv', '1ay', '1ap', '1aa', '1ao', '1ah', '1aj', '1ak', '1ac', '1am', '1as', '1ar', '1at', '1au', '1bg', '1bt', '1bc', '1bi', '1bh', '1bs', '1bm', '1by', '1bo', '1ck', '1cr', '1cd', '1cg', '1ce', '1dt', '1ds', '1db', '1da', '1cc', '1gv', '1ec', '1ep', '1ew', '1gs', '1gc', '1ga', '1gd', '1sk', '1gg', '1hk', '1hm', '1ic', '1ii', '1jv', '1js', '1jt', '1ks', '1ki', '1kn', '1me', '1mj', '1nj', '1nc', '1nh', '1ox', '1pn', '1pe', '1ri', '1rl', '1rr', '1rg', '1re', '1rn', '1sj', '1va', '1st', '1sz', '1sg', '1sc', '1sp', '1hs', '1sb', '1sv', '1jb', '1sw', '1bn', '1kt', '1kh', '1rc', '1ve', '1tj', '1vi', '1vj', '1vk', '1yd']
MYSURU_COLLEGE_CODES = ['4ad', '4ai', '4al', '4bw', '4bb', '4bd', '4bp', '4cb', '4ci', '4dm', '4ek', '4mg', '4gm', '4ge', '4gh', '4gl', '4gk', '4gw', '4jn', '4kv', '4km', '4mh', '4mt', '4mk', '4nn', '4pa', '4pm', '4pr', '4ra', '4sf', '4sh', '4mw', '4sm', '4su', '4sn', '4es', '4so', '4ub', '4vv', '4vm', '4vp', '4yg']
BELAGAVI_COLLEGE_CODES = ['2av', '2ag', '2ab', '2ae', '2bv', '2bl', '2gp', '4go', '2gb', '2hn', '2ji', '2kd', '2ke', '2kl', '2gi', '2mb', '2mm', '2rh', '2bu', '2sr', '2sa', '2ha', '2ka', '2tg', '2vs', '2vd']
KALABURGI_COLLEGE_CODES = ['3ae', '3bk', '3br', '3gf', '3gu', '3gn', '3kc', '3kb', '3la', '3na', '3pg', '3vc', '3rb', '3sl', '3vn']

#COLLEGE_CODES = BENGALURU_COLLEGE_CODES+MYSURU_COLLEGE_CODES+BELAGAVI_COLLEGE_CODES+KALABURGI_COLLEGE_CODES
COLLEGE_CODES = ['1mv']
insert_region_results_multithreaded(COLLEGE_CODES)



'''
threads = []

for college_code in COLLEGE_CODES:
	t = threading.Thread(target=insert_college_results, args=(college_code,))
	threads.append(t)
	t.start()



thread1 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[:16],))
thread1.start()
thread2 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[17:33],))
thread2.start()
thread3 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[34:50],))
thread3.start()
thread4 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[51:67],))
thread4.start()
thread5 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[68:84],))
thread5.start()
thread6 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[85:101],))
thread6.start()
thread7 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[102:118],))
thread7.start()
thread8 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[119:135],))
thread8.start()
thread9 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[136:152],))
thread9.start()
thread10 = threading.Thread(target=insert_region_results, args=(COLLEGE_CODES[153:],))
thread10.start()





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
