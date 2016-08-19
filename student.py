from lxml import etree, html
import requests
import urllib2

BASE_URL = 'http://results.vtu.ac.in'




class Student(object):
    """docstring for Student."""
    def __init__(self, usn='1MV14IS080'):
        super(Student, self).__init__()
        self.usn = usn
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'results.vtu.ac.in',
            'Referer': 'http://results.vtu.ac.in/'
        }

        payload = {
            'rid': self.usn,
            'submit': 'SUBMIT'
        }

        response = requests.post(BASE_URL + '/vitavi.php', payload, headers=headers)
        tree = html.fromstring(response.content)

        # xpath selector for subject name
        sub_xpath = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/i/text()'

        # xpath selector for subject external marks, internal marks and total marks
        sub_xpath2 = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/text()'

        # xpath selector for subject result
        sub_xpath3 = '/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tr[{}]/td[{}]/b/text()'

        response = requests.post(BASE_URL + '/vitavi.php', payload, headers=headers)
        tree = html.fromstring(response.content)

        # student details
        self.student_name_usn = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/b/text()')
        self.total_marks = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[3]/tr/td[4]/text()')
        self.semester = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tr/td[2]/b/text()')
        self.result = tree.xpath('/html/body/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table[1]/tr/td[4]/b/text()')

        # subject details
        self.sub1 = tree.xpath(sub_xpath.format('2', '1'))
        self.sub1_external = tree.xpath(sub_xpath2.format('2', '2'))
        self.sub1_internal = tree.xpath(sub_xpath2.format('2', '3'))
        self.sub1_total = tree.xpath(sub_xpath2.format('2', '4'))
        self.sub1_result = tree.xpath(sub_xpath3.format('2', '5'))

        self.sub2 = tree.xpath(sub_xpath.format('3', '1'))
        self.sub2_external = tree.xpath(sub_xpath2.format('3', '2'))
        self.sub2_internal = tree.xpath(sub_xpath2.format('3', '3'))
        self.sub2_total = tree.xpath(sub_xpath2.format('3', '4'))
        self.sub2_result = tree.xpath(sub_xpath3.format('3', '5'))

        self.sub3 = tree.xpath(sub_xpath.format('4', '1'))
        self.sub3_external = tree.xpath(sub_xpath2.format('4', '2'))
        self.sub3_internal = tree.xpath(sub_xpath2.format('4', '3'))
        self.sub3_total = tree.xpath(sub_xpath2.format('4', '4'))
        self.sub3_result = tree.xpath(sub_xpath3.format('4', '5'))

        self.sub4 = tree.xpath(sub_xpath.format('5', '1'))
        self.sub4_external = tree.xpath(sub_xpath2.format('5', '2'))
        self.sub4_internal = tree.xpath(sub_xpath2.format('5', '3'))
        self.sub4_total = tree.xpath(sub_xpath2.format('5', '4'))
        self.sub4_result = tree.xpath(sub_xpath3.format('5', '5'))

        self.sub5 = tree.xpath(sub_xpath.format('6', '1'))
        self.sub5_external = tree.xpath(sub_xpath2.format('6', '2'))
        self.sub5_internal = tree.xpath(sub_xpath2.format('6', '3'))
        self.sub5_total = tree.xpath(sub_xpath2.format('6', '4'))
        self.sub5_result = tree.xpath(sub_xpath3.format('6', '5'))

        self.sub6 = tree.xpath(sub_xpath.format('7', '1'))
        self.sub6_external = tree.xpath(sub_xpath2.format('7', '2'))
        self.sub6_internal = tree.xpath(sub_xpath2.format('7', '3'))
        self.sub6_total = tree.xpath(sub_xpath2.format('7', '4'))
        self.sub6_result = tree.xpath(sub_xpath3.format('7', '5'))

        self.sub7 = tree.xpath(sub_xpath.format('8', '1'))
        self.sub7_external = tree.xpath(sub_xpath2.format('8', '2'))
        self.sub7_internal = tree.xpath(sub_xpath2.format('8', '3'))
        self.sub7_total = tree.xpath(sub_xpath2.format('8', '4'))
        self.sub7_result = tree.xpath(sub_xpath3.format('8', '5'))

        self.sub8 = tree.xpath(sub_xpath.format('9', '1'))
        self.sub8_external = tree.xpath(sub_xpath2.format('9', '2'))
        self.sub8_internal = tree.xpath(sub_xpath2.format('9', '3'))
        self.sub8_total = tree.xpath(sub_xpath2.format('9', '4'))
        self.sub8_result = tree.xpath(sub_xpath3.format('9', '5'))


    def get_name(self):
        return self.student_name_usn
