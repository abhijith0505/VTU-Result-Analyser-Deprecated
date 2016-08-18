VTU Result Notifier
===================

[![Build Status](https://travis-ci.org/abhijith0505/VTU-Result-Notifier.svg?branch=master)](https://travis-ci.org/abhijith0505/VTU-Result-Notifier)




Tired of checking the VTU Website everyday for your results?
The curiosity killing you?
Use this script and stop worrying about it (until it comes, of course).

----------


Prerequisite
-------------------


* **$ git clone** the repository.

	` $ git clone https://github.com/abhijith0505/VTU-Result-Notifier.git`

* Install the required modules using,

	`$ pip install -r requirements.txt`

	- Installs BeautifulSoup, which is used for scraping the website. The package name is *beautifulsoup4*, and the same package works on Python 2 and Python 3.
	
	- The SMS to your number is sent using **twilio**. Installs twilio module.

> If you do not have pip installed, install it using:  
	> `$ easy_install pip`

 

Usage
-------------------

- Sign up for a free twilio account from http://twilio.com. You will be assigned with an account sid and auth token. You may also have to verify the mobile number to which you will send the message. Once this is successful, you will also get a sender twilio mobile number that can be used in your code.

- Follow the comments present in the file to set up the script to send the SMS to your number.


> **Note:**
        The script has to be executed regularly for it to check the website and send the SMS. For this to happen, schedule the execution of this script using a **crontab**. (Redirect errors to /dev/null to keep terminal clean)
> Example:
> `* * * * * python resultScraper.py 2>/dev/null`

----------
> **Note:**
        The free twilio account allows practically unlimited SMS to your own verified number. However, if you want to send SMS to other numbers, you have to upgrade to a paid plan.


-----

#LICENSE

```
MIT License

Copyright (c) 2016 Abhijith C

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
