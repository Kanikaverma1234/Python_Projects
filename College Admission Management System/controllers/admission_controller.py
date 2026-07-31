from services.admission_service import AdmissionService

class AdmissionController:

    def __init__(self):
        self.service = AdmissionService()

    def add_student(self, student):
        return self.service.add_student(student)

    def get_all_students(self):
        return self.service.get_all_students()

    def search_student(self, student_id):
        return self.service.search_student(student_id)

    def update_student(self, student):
        return self.service.update_student(student)

    def delete_student(self, student_id):
        return self.service.delete_student(student_id)

    def get_courses(self):
        return self.service.get_courses()

    def get_course_id(self, course_name):
        return self.service.get_course_id(course_name)