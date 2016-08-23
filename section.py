from student import student_results
from pymongo import MongoClient
import pymongo
from collections import OrderedDict


NUM_OF_STUDENTS = 200

def insert_section_results(college_code='1MV', year='14', branch='IS'):
    client = MongoClient(document_class=OrderedDict)
    db = client.results
    db.students.ensure_index('usn', unique=True)
    for student in range(NUM_OF_STUDENTS):
        result = student_results(college_code='1MV', year='14', branch='IS', regno=student)
        if (result != None):
            db.students.insert_one(result)
