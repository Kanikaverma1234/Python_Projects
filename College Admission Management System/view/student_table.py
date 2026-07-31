import tkinter as tk
from tkinter import ttk

from controllers.admission_controller import AdmissionController


class StudentTable(tk.LabelFrame):

    def __init__(self, parent, admission_form=None):
        # if admission_form object is passed, the table can send selected data to the from.

        super().__init__(
            # super is used to call the constructor of the parent class.
            parent,
            text=" Student Records ",
            font=("Segoe UI", 12, "bold"),
            padx=10,
            pady=10,
        )

        # DAO Object
        self.controller = AdmissionController()

        # Admission Form Reference
        self.admission_form = admission_form

        # Create Widgets
        self.create_widgets()

        # Load Students
        self.load_students()

    # ================ Create Widgets ================= #

    def create_widgets(self):

        columns = (
            "ID",
            "Student Name",
            "Father Name",
            "Gender",
            "DOB",
            "Mobile",
            "Email",
            "Course",
            "Paid Fee",
            "Pending Fee",
            "Status",
        )

        self.student_tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15,
        )

        # ================= Headings ================= #

        for column in columns:
            self.student_tree.heading(column, text=column)
            self.student_tree.column(column, width=120, anchor="center")

        # Make some columns wider
        self.student_tree.column("Student Name", width=180)
        self.student_tree.column("Father Name", width=180)
        self.student_tree.column("Email", width=220)

        # ================= Scrollbars ================= #

        y_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.student_tree.yview,
        )

        x_scroll = ttk.Scrollbar(
            self,
            orient="horizontal",
            command=self.student_tree.xview,
        )

        self.student_tree.configure(
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set,
        )

        # ================= Grid ================= #

        self.student_tree.grid(
            row=0,
            column=0,
            sticky="nsew",  # the widgets stretches all four directions
        )
        self.student_tree.update_idletasks()
        # This will update the display of windows

        y_scroll.grid(
            row=0,
            column=1,
            sticky="ns",  # top to bottom
        )

        x_scroll.grid(
            row=1,
            column=0,
            sticky="ew",  # left to right
        )

        # Expand Treeview with Window
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Row Selection Event
        self.student_tree.bind(
            "<<TreeviewSelect>>",
            self.on_row_select,
        )

    # ================= Load Students ================== #

    def load_students(self):

        try:

            # Remove old records
            for row in self.student_tree.get_children():
                # get_children() returns IDs of all rows currently present in the Treeview.

                self.student_tree.delete(row)
                # we are deleting rows before insertion, to ensure the Treeview always displays the latest data and prevents duplicate rows.

            students = self.controller.get_all_students()
            # It will stored the list of tuples

            for student in students:
                self.student_tree.insert(
                    "",
                    tk.END,
                    values=(
                        # based on the indexing
                        student[0],
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5],
                        student[6],
                        student[9],
                        student[11],
                        student[12],
                        student[13],
                    ),
                )
                self.student_tree.update_idletasks()
                self.update_idletasks()
                # update_idletaks: process all pending GUI updates at real time so that the new row become visible without missing.

        except Exception:
            import traceback

            # Its job is to show where the error happened and what caused it.

            traceback.print_exc()

    # ==========================================================
    # Row Selection
    # ==========================================================
    # It explains how data moves from the Treeview back into the Admission Form
    def on_row_select(self, event):

        # No AdmissionForm linked
        if self.admission_form is None:
            return

        # Get selected row and returns it's ID of the currently selected row.
        selected = self.student_tree.focus()

        if not selected:
            return

        # It returns the data stored in a row.
        values = self.student_tree.item(selected, "values")

        # Student ID
        self.admission_form.student_id.set(values[0])

        # Instead of filling only the visible columns,
        # fetch the complete student record from database.
        result = self.controller.search_student(values[0])

        if result:
            # .set() updates the Entry widget automatically.

            self.admission_form.student_name.set(result[1])
            self.admission_form.father_name.set(result[2])
            self.admission_form.gender.set(result[3])
            self.admission_form.dob.set(result[4])
            self.admission_form.mobile.set(result[5])
            self.admission_form.email.set(result[6])
            self.admission_form.address.set(result[7])
            self.admission_form.admission_date.set(result[8])

            # Course Name
            self.admission_form.course.set(result[10])

            self.admission_form.fee_paid.set(result[12])
            self.admission_form.pending_fee.set(result[13])
            self.admission_form.fee_status.set(result[14])

            # ============= Refresh Table ================ #

    def refresh_table(self):

        self.load_students()
