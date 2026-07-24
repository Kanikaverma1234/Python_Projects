class Student:

    def __init__(
        self,
        student_id=None,
        student_name="",
        father_name="",
        gender="",
        dob="",
        mobile="",
        email="",
        address="",
        admission_date="",
        course_id=None,
        fee_paid=0,
        fee_status="",
        pending_fee=0,
    ):

        self.__student_id = student_id
        self.__student_name = student_name
        self.__father_name = father_name
        self.__gender = gender
        self.__dob = dob
        self.__mobile = mobile
        self.__email = email
        self.__address = address
        self.__admission_date = admission_date
        self.__course_id = course_id
        self.__fee_paid = fee_paid
        self.__fee_status = fee_status
        self.pending_fee = pending_fee

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, student_name):
        self.__student_name = student_name

    def get_father_name(self):
        return self.__father_name

    def set_father_name(self, father_name):
        self.__father_name = father_name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_mobile(self):
        return self.__mobile

    def set_mobile(self, mobile):
        self.__mobile = mobile

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_admission_date(self):
        return self.__admission_date

    def set_admission_date(self, date):
        self.__admission_date = date

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_fee_paid(self):
        return self.__fee_paid

    def set_fee_paid(self, fee):
        self.__fee_paid = fee

    def get_pending_fee(self):
        return self.pending_fee

    def set_pending_fee(self, fee):
        self.pending_fee = fee

    def get_fee_status(self):
        return self.__fee_status

    def set_fee_status(self, status):
        self.__fee_status = status
