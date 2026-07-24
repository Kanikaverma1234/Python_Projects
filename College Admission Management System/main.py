import tkinter as tk

from view.admission_form import AdmissionForm
from view.student_table import StudentTable


class CollegeManagementSystem:

    def __init__(self, root):

        self.root = root

        self.root.title("College Admission Management System")
        self.root.geometry("1400x800")
        self.root.state("zoomed")

        self.create_ui()

    def create_ui(self):

        # ================= Main Container ================= #

        main_frame = tk.Frame(self.root)

        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # ================= Admission Form ================= #

        self.admission_form = AdmissionForm(main_frame)

        self.admission_form.pack(fill="x", padx=10, pady=10)

        # ================= Student Table ================= #

        self.student_table = StudentTable(main_frame, self.admission_form)

        self.student_table.pack(fill="both", expand=True, padx=10, pady=10)

        # ================= Connect Both ================= #

        self.admission_form.student_table = self.student_table


# ================= Main ================= #

if __name__ == "__main__":

    root = tk.Tk()

    app = CollegeManagementSystem(root)

    root.mainloop()
