VTU Result Notifier 
===================


Tired of checking the VTU Website everyday for your results? 
The curiosity killing you? 
Use this script and stop worrying about it (until it comes, of course).

----------


Prerequisite
-------------------

* Install BeautifulSoup, which is used for scraping the website.
	` $ apt-get install python-bs4`
	
	**Beautiful Soup 4** is published through PyPi, so if you can’t install it with the system packager, you can install it with **easy_install** or **pip**. The package name is *beautifulsoup4*, and the same package works on Python 2 and Python 3.
	
	`$ easy_install beautifulsoup4`
	
	` $ pip install beautifulsoup4`

	* If you do not have **pip** installed, install it using:   
	`$ easy_install pip`
	
*  The SMS to your number is sent using **twilio**. 
	* Install twilio module. The easiest way to install twilio-python is from PyPi using **pip**, a package manager for Python. Simply run this in the terminal:
   `$ pip install twilio`
	
	If you get a *pip: command not found* error, you can also use **easy_install**. Run this in your terminal:
	`$ easy_install twilio`


Usage
-------------------

- Sign up for a free twilio account from http://twilio.com. You will be assigned with an account sid and auth token. You may also have to verify the mobile number to which you will send the message. Once this is successful, you will also get a sender twilio mobile number that can be used in your code.

- **$ git clone** the repository and edit the **resultScraper.py** file. 

- Follow the comments present in the file to set up the script to send the SMS to your number.


> **Note:**
	The script has to be executed regularly for it to check the website and send the SMS. For this to happen, schedule the execution of this script using a **crontab**. (Redirect errors to /dev/null to keep terminal clean)
> Example: 	
> `* * * * * python resultScraper.py 2>/dev/null`

----------
> **Note:**
	The free twilio account allows practically unlimited SMS to your own verified number. However, if you want to send SMS to other numbers, you have to upgrade to a paid plan.
	

