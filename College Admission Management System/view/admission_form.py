import tkinter as tk
from tkinter import ttk, messagebox
from controllers.admission_controller import AdmissionController
from model.student import Student


class AdmissionForm(tk.LabelFrame):

    def __init__(self, parent, student_table=None):

        super().__init__(
            parent,
            text=" Student Admission Form ",
            font=("Segoe UI", 12, "bold"),
            padx=15,
            pady=10,
        )
        # DAO object
        self.controller = AdmissionController()

        self.student_table = student_table

        # Functions
        self.create_variables()
        self.create_widgets()
        self.load_courses()
        # self.table_refresh()

    # ==========================================================
    # Variables
    # ==========================================================

    def create_variables(self):

        # Student Details
        # When we search or select a student from the table, this variable will hold the data.
        self.student_id = tk.StringVar()
        self.student_name = tk.StringVar()
        self.father_name = tk.StringVar()
        self.gender = tk.StringVar()
        self.dob = tk.StringVar()
        self.mobile = tk.StringVar()
        self.email = tk.StringVar()
        self.address = tk.StringVar()
        self.admission_date = tk.StringVar()
        self.course = tk.StringVar()
        self.fee_paid = tk.StringVar()
        self.pending_fee = tk.StringVar()
        self.fee_status = tk.StringVar()

        # Stores the selected course fee
        self.course_fee = 0

        # Stores course name -> course_id mapping
        self.course_dict = {}

    # ==========================================
    # Create Widgets
    # ==========================================

    def create_widgets(self):

        label_font = ("Arial", 11)
        entry_width = 30

        # ================== Title ================== #

        title = tk.Label(
            self,
            text="College Admission Management System",
            font=("Arial", 18, "bold"),
            bg="#2C3E50",  # Background color
            fg="white",  # Text color
            padx=10,
            pady=10,
        )

        title.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(10, 20))

        # ================ Student Id ============== #

        lbl_student_id = tk.Label(self, text="Student ID", font=("Arial", 11))

        lbl_student_id.grid(row=1, column=0, padx=10, pady=8, sticky="w")

        txt_student_id = tk.Entry(
            self, textvariable=self.student_id, width=30, state="readonly"
        )

        txt_student_id.grid(row=1, column=1, padx=10, pady=8, sticky="w")

        # ============= Student Name ============= #

        lbl_student_name = tk.Label(self, text="Student Name", font=("Arial", 11))

        lbl_student_name.grid(row=2, column=0, padx=10, pady=8, sticky="w")

        self.txt_student_name = tk.Entry(self, textvariable=self.student_name, width=30)

        self.txt_student_name.grid(row=2, column=1, padx=10, pady=8, sticky="w")

        # ============== Father Name =============== #

        lbl_father_name = tk.Label(self, text="Father Name", font=("Arial", 11))
        lbl_father_name.grid(row=2, column=2, padx=10, pady=8, sticky="w")

        self.txt_father_name = tk.Entry(self, textvariable=self.father_name, width=30)
        self.txt_father_name.grid(row=2, column=3, padx=10, pady=8, sticky="w")

        # ================ Gender ================ #

        lbl_gender = tk.Label(self, text="Gender", font=("Arial", 11))

        lbl_gender.grid(row=3, column=0, padx=10, pady=8, sticky="w")

        self.cmb_gender = ttk.Combobox(
            self,
            textvariable=self.gender,
            values=["Male", "Female", "Other"],
            state="readonly",
            width=27,
        )

        self.cmb_gender.grid(row=3, column=1, padx=10, pady=8, sticky="w")

        # ============== DOB ================== #

        lbl_dob = tk.Label(self, text="Date of Birth", font=label_font)

        lbl_dob.grid(row=3, column=2, padx=10, pady=8, sticky="w")

        self.txt_dob = tk.Entry(self, textvariable=self.dob, width=entry_width)

        self.txt_dob.grid(row=3, column=3, padx=10, pady=8, sticky="w")

        # ============ Mobile ============= #

        lbl_mobile = tk.Label(self, text="Mobile", font=label_font)

        lbl_mobile.grid(row=4, column=0, padx=10, pady=8, sticky="w")

        self.txt_mobile = tk.Entry(self, textvariable=self.mobile, width=entry_width)

        self.txt_mobile.grid(row=4, column=1, padx=10, pady=8, sticky="w")

        # ============= Email =============== #

        lbl_email = tk.Label(self, text="Email", font=label_font)

        lbl_email.grid(row=4, column=2, padx=10, pady=8, sticky="w")

        self.txt_email = tk.Entry(self, textvariable=self.email, width=entry_width)

        self.txt_email.grid(row=4, column=3, padx=10, pady=8, sticky="w")

        # ============= Adress ================ #

        lbl_address = tk.Label(self, text="Address", font=label_font)

        lbl_address.grid(row=5, column=0, padx=10, pady=8, sticky="w")

        self.txt_address = tk.Entry(self, textvariable=self.address, width=entry_width)

        self.txt_address.grid(row=5, column=1, padx=10, pady=8, sticky="w")

        # ============= Admission Date ========== #

        lbl_admission_date = tk.Label(self, text="Admission Date", font=label_font)

        lbl_admission_date.grid(row=5, column=2, padx=10, pady=8, sticky="w")

        self.txt_admission_date = tk.Entry(
            self, textvariable=self.admission_date, width=entry_width
        )

        self.txt_admission_date.grid(row=5, column=3, padx=10, pady=8, sticky="w")

        # =============== Course Combobox =============== #

        lbl_course = tk.Label(self, text="Course", font=label_font)

        lbl_course.grid(row=6, column=0, padx=10, pady=8, sticky="w")

        self.cmb_course = ttk.Combobox(
            self, textvariable=self.course, state="readonly", width=27
        )

        self.cmb_course.grid(row=6, column=1, padx=10, pady=8, sticky="w")

        # Whenever the user selects a course,
        # calculate the pending fee.
        # bind() is a method provided by tkinter to connect an event with a function.
        self.cmb_course.bind("<<ComboboxSelected>>", self.calculate_pending_fee)

        # ============== Fee Paid ============== #

        lbl_fee_paid = tk.Label(self, text="Fee Paid", font=label_font)

        lbl_fee_paid.grid(row=6, column=2, padx=10, pady=8, sticky="w")

        self.txt_fee_paid = tk.Entry(
            self, textvariable=self.fee_paid, width=entry_width
        )

        self.txt_fee_paid.grid(row=6, column=3, padx=10, pady=8, sticky="w")

        # Whenever the user types the fee,
        # calculate the pending fee.
        self.txt_fee_paid.bind("<KeyRelease>", self.calculate_pending_fee)

        # ================ Pending Fees============= #

        lbl_pending_fee = tk.Label(self, text="Pending Fee", font=label_font)

        lbl_pending_fee.grid(row=7, column=0, padx=10, pady=8, sticky="w")

        self.txt_pending_fee = tk.Entry(
            self, textvariable=self.pending_fee, width=entry_width, state="readonly"
        )

        self.txt_pending_fee.grid(row=7, column=1, padx=10, pady=8, sticky="w")

        # ================== Fees Status ===================== #

        lbl_fee_status = tk.Label(self, text="Fee Status", font=label_font)

        lbl_fee_status.grid(row=7, column=2, padx=10, pady=8, sticky="w")

        self.cmb_fee_status = ttk.Combobox(
            self,
            textvariable=self.fee_status,
            values=["Paid", "Pending"],
            state="readonly",
            width=27,
        )

        self.cmb_fee_status.grid(row=7, column=3, padx=10, pady=8, sticky="w")

        # ================ BUTTONS FRAMES ============== #

        button_frame = tk.Frame(self)

        button_frame.grid(row=8, column=0, columnspan=4, pady=15)

        btn_save = tk.Button(
            button_frame,
            text="Save",
            width=12,
            bg="#28A745",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.save_student,
        )

        btn_save.grid(row=0, column=0, padx=5)

        btn_search = tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#17A2B8",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.search_student,
        )

        btn_search.grid(row=0, column=1, padx=5)

        btn_update = tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#FFC107",
            fg="black",
            font=("Arial", 10, "bold"),
            command=self.update_student,
        )

        btn_update.grid(row=0, column=2, padx=5)

        btn_delete = tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#DC3545",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.delete_student,
        )

        btn_delete.grid(row=0, column=3, padx=5)

        btn_clear = tk.Button(
            button_frame,
            text="Clear",
            width=12,
            bg="#6C757D",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.clear_form,
        )

        btn_clear.grid(row=0, column=4, padx=5)

        # ==========================================

    # Load Courses
    # ==========================================

    def load_courses(self):

        # Get all courses from database
        courses = self.controller.get_courses()

        # Empty list for course names
        course_names = []

        # Clear dictionary
        self.course_dict.clear()

        # Loop through all courses
        for course in courses:

            course_id = course[0]
            course_name = course[1]
            course_fee = float(course[3])

            # Add course name in Combobox
            course_names.append(course_name)

            # Store course id and fee
            self.course_dict[course_name] = {"id": course_id, "fee": course_fee}

        # Display course names in Combobox
        self.cmb_course["values"] = course_names

        # Select first course automatically (By default)
        if course_names:
            self.cmb_course.current(0)
            # current() selects an item from the combobox
            
            self.calculate_pending_fee()
            # when the course is selected then it immediately calculates pending fees

    # ================ Calculate Pending Fee ======================= #

    def calculate_pending_fee(self, event=None):

        try:

            # Get selected course
            selected_course = self.course.get()

            # If no course selected
            if selected_course == "":
                return

            # Get course fee from dictionary
            course_data = self.course_dict[selected_course]

            self.course_fee = course_data["fee"]

            # Get fee paid
            fee_paid = self.fee_paid.get().strip()

            if fee_paid == "":
                fee_paid = 0
            else:
                fee_paid = float(fee_paid)

            # Calculate pending fee
            pending_fee = self.course_fee - fee_paid

            # Prevent negative value
            if pending_fee < 0:
                pending_fee = 0

            # Show pending fee
            self.pending_fee.set(pending_fee)

            # Set fee status automatically
            if pending_fee == 0:
                self.fee_status.set("Paid")
            else:
                self.fee_status.set("Pending")

        except ValueError:

            self.pending_fee.set("")

            self.fee_status.set("")

        # ============ Save Methods ============ #

    def save_student(self):

        # Check required fields
        if self.student_name.get() == "":
            messagebox.showerror("Error", "Enter Student Name")
            return

        if self.father_name.get() == "":
            messagebox.showerror("Error", "Enter Father Name")
            return

        if self.course.get() == "":
            messagebox.showerror("Error", "Select Course")
            return

        # Create Student Object
        student = Student()

        # Set Student Details
        student.set_student_name(self.student_name.get())
        student.set_father_name(self.father_name.get())
        student.set_gender(self.gender.get())
        student.set_dob(self.dob.get())
        student.set_mobile(self.mobile.get())
        student.set_email(self.email.get())
        student.set_address(self.address.get())
        student.set_admission_date(self.admission_date.get())

        # Get Course ID
        course_data = self.course_dict[self.course.get()]
        student.set_course_id(course_data["id"])

        student.set_fee_paid(float(self.fee_paid.get() or 0))
        student.set_pending_fee(float(self.pending_fee.get() or 0))
        student.set_fee_status(self.fee_status.get())

        # Save into Database
        self.controller.add_student(student)

        messagebox.showinfo("Success", "Student Added Successfully.")

        # Clear Form
        self.clear_form()

        print("Before Refresh")

        if self.student_table:
            self.student_table.load_students()

        print("After Refresh")

        # ============ Search Student =========== #

    def search_student(self):

        # Check Student ID
        if self.student_id.get() == "":
            messagebox.showerror("Error", "Enter Student ID")
            return

        # Search Student
        result = self.controller.search_student(self.student_id.get())

        # Student Found
        if result:
            self.student_id.set(result[0])
            self.student_name.set(result[1])
            self.father_name.set(result[2])
            self.gender.set(result[3])
            self.dob.set(result[4])
            self.mobile.set(result[5])
            self.email.set(result[6])
            self.address.set(result[7])
            self.admission_date.set(result[8])

            # Course Name
            self.course.set(result[10])

            self.fee_paid.set(result[12])
            self.pending_fee.set(result[13])
            self.fee_status.set(result[14])

        else:

            messagebox.showinfo("Not Found", "Student not found.")

        # ============ Update Student ================ #

    def update_student(self):

        # Check Student ID
        if self.student_id.get() == "":
            messagebox.showerror("Error", "Please select a student to update.")
            return

        # Create Student Object
        student = Student()

        # VERY IMPORTANT
        # Set the existing Student ID
        student.set_student_id(int(self.student_id.get()))

        # Set Student Details
        student.set_student_name(self.student_name.get())
        student.set_father_name(self.father_name.get())
        student.set_gender(self.gender.get())
        student.set_dob(self.dob.get())
        student.set_mobile(self.mobile.get())
        student.set_email(self.email.get())
        student.set_address(self.address.get())
        student.set_admission_date(self.admission_date.get())

        # Course ID
        course_data = self.course_dict[self.course.get()]
        student.set_course_id(course_data["id"])

        student.set_fee_paid(float(self.fee_paid.get() or 0))
        student.set_pending_fee(float(self.pending_fee.get() or 0))
        student.set_fee_status(self.fee_status.get())

        # Update Database
        self.controller.update_student(student)

        messagebox.showinfo("Success", "Student Updated Successfully.")

        # Clear Form
        self.clear_form()

        # Refresh Student Table
        if self.student_table:
            self.student_table.load_students()
            

    # ============ Delete Student ============ #

    def delete_student(self):

        # Check Student ID
        if self.student_id.get() == "":
            messagebox.showerror("Error", "Please select a student to delete.")
            return

        # Confirmation
        answer = messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this student?"
        )

        if answer:

            # Delete Student
            self.controller.delete_student(int(self.student_id.get()))

            messagebox.showinfo("Success", "Student Deleted Successfully.")

            # Clear Form
            self.clear_form()

            # Refresh Student Table
            print("Before Refresh")

            if self.student_table:
                self.student_table.load_students()

            print("After Refresh")

    # =============== Clear Form ================= #

    def clear_form(self):

        self.student_id.set("")
        self.student_name.set("")
        self.father_name.set("")
        self.gender.set("")
        self.dob.set("")
        self.mobile.set("")
        self.email.set("")
        self.address.set("")
        self.admission_date.set("")
        self.course.set("")
        self.fee_paid.set("")
        self.pending_fee.set("")
        self.fee_status.set("")

        # Load courses again
        if self.cmb_course["values"]:
            self.cmb_course.current(0)
            self.calculate_pending_fee()
