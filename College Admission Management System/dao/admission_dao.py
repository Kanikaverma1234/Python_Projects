from config.db_connection import DBConnection


class AdmissionDAO:

    def __init__(self):

        self.db = DBConnection()

        self.connection = self.db.get_connection()

        self.cursor = self.connection.cursor()

    # ========== Add Student ========== #

    def add_student(self, student):

        query = """
    INSERT INTO student
    (
        student_name,
        father_name,
        gender,
        dob,
        mobile,
        email,
        address,
        admission_date,
        course_id,
        fee_paid,
        pending_fee,
        fee_status
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

        values = (
            student.get_student_name(),
            student.get_father_name(),
            student.get_gender(),
            student.get_dob(),
            student.get_mobile(),
            student.get_email(),
            student.get_address(),
            student.get_admission_date(),
            student.get_course_id(),
            student.get_fee_paid(),
            student.get_pending_fee(),
            student.get_fee_status(),
        )

        self.cursor.execute(query, values)
        self.connection.commit()

    # ========== Get All Students ========== #

    def get_all_students(self):
        self.connection.commit()

        query = """
    SELECT
        s.student_id,
        s.student_name,
        s.father_name,
        s.gender,
        s.dob,
        s.mobile,
        s.email,
        s.address,
        s.admission_date,
        c.course_name,
        c.course_fee,
        s.fee_paid,
        s.pending_fee,
        s.fee_status
    FROM student s
    INNER JOIN course c
        ON s.course_id = c.course_id
    """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # ========== Search Student ========== #

    def search_student(self, student_id):

        query = """
    SELECT
        s.student_id,
        s.student_name,
        s.father_name,
        s.gender,
        s.dob,
        s.mobile,
        s.email,
        s.address,
        s.admission_date,
        s.course_id,
        c.course_name,
        c.course_fee,
        s.fee_paid,
        s.pending_fee,
        s.fee_status
    FROM student s
    INNER JOIN course c
        ON s.course_id = c.course_id
    WHERE s.student_id=%s
    """

        self.cursor.execute(query, (student_id,))

        return self.cursor.fetchone()

    # ========== Update Student ========== #

    def update_student(self, student):

        query = """

        UPDATE student SET

        student_name=%s,

        father_name=%s,

        gender=%s,

        dob=%s,

        mobile=%s,

        email=%s,

        address=%s,

        admission_date=%s,

        course_id=%s,

        fee_paid=%s,

        pending_fee=%s,

        fee_status=%s


        WHERE student_id=%s

        """

        values = (
            student.get_student_name(),
            student.get_father_name(),
            student.get_gender(),
            student.get_dob(),
            student.get_mobile(),
            student.get_email(),
            student.get_address(),
            student.get_admission_date(),
            student.get_course_id(),
            student.get_fee_paid(),
            student.get_pending_fee(),
            student.get_fee_status(),
            student.get_student_id(),
        )

        self.cursor.execute(query, values)

        self.connection.commit()

    # ========== Delete Student ========== #

    def delete_student(self, student_id):

        query = """

        DELETE FROM student

        WHERE student_id=%s

        """

        self.cursor.execute(query, (student_id,))

        self.connection.commit()

        # ========== Get Courses ========== #

    def get_courses(self):

        query = """
     SELECT
        course_id,
        course_name,
        duration,
        course_fee
    FROM course
    """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_course_id(self, course_name):

        query = """
    SELECT course_id
    FROM course
    WHERE course_name=%s
    """

        self.cursor.execute(query, (course_name,))

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None
