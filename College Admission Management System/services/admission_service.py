from dao.admission_dao import AdmissionDAO

# It basically a middle layer between GUI(view) and dao layer. It is used because in future if we change the logic the database logic so we did not need to modify our GUI file.

class AdmissionService:

    def __init__(self):
        self.dao = AdmissionDAO()

    def add_student(self, student):
        return self.dao.add_student(student)

    def get_all_students(self):
        return self.dao.get_all_students()

    def search_student(self, student_id):
        return self.dao.search_student(student_id)

    def update_student(self, student):
        return self.dao.update_student(student)

    def delete_student(self, student_id):
        return self.dao.delete_student(student_id)

    def get_courses(self):
        return self.dao.get_courses()

    def get_course_id(self, course_name):
        return self.dao.get_course_id(course_name)