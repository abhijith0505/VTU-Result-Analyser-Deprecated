from student import Student


NUM_OF_STUDENTS = 200

class Section(object):
    """docstring for Section."""
    def __init__(self, college_code='1MV', year='14', branch='IS'):
        super(Section, self).__init__()
        self.college_code = college_code
        self.year = year
        self.branch = branch

    def fetch_results(self):
        self.students = [Student(self.college_code+self.year+self.branch+str(student).zfill(3)) for student in range(NUM_OF_STUDENTS)]


    def clean_data(self):
        self.students = [self.students[student] for student in range(len(self.students)) if (self.students[student].get_name())]

    def print_names(self):
        for student in range(len(self.students)):
            print self.students[student].get_name()
