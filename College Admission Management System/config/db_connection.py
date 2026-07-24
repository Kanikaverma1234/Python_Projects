import mysql.connector


class DBConnection:

    def get_connection(self):

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kanika1234@",
            database="college_admission_db",
        )

        return connection
