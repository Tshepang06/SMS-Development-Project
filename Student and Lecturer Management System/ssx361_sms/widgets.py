from tkinter import *
from tkinter import END
from addStudent import AddStudent
from updateStudent import UpdateStudent
from deleteStudent import DeleteStudent
from populate import PopulateListBox
from addStudent import AddStudent
from updateLecturer import UpdateLecturer
from tkinter import messagebox


class GUIApp:
    def __init__(self, master):
        self.master = None
        self.list = Listbox(height=15, width=50)
        self.master = master
        self.master.title("Student and Lecturer Management System")
        self.master.geometry("600x400")

    def add_widgets(self):
        label = Label(self.master, text="Welcome to Student and Lecturer Management System", font=("Helvetica", 16))
        label.grid(pady=10)

        student_button = Button(self.master, text="Manage Students", command=self.open_student_form)
        student_button.grid(pady=70)

        lecturer_button = Button(self.master, text="Manage Lecturers", command=self.open_lecturer_form)
        lecturer_button.grid(pady=70)

    def open_student_form(self):
        # Create separate window for student records
        student_form = Toplevel(self.master)
        student_records = AddStudent

        # Adding text variables
        self.st_idtxt = StringVar()
        self.nametxt = StringVar()
        self.surnametxt = StringVar()
        self.st_celltxt = StringVar()
        self.emailtxt = StringVar()
        self.coursetxt = StringVar()

        # Add input fields for student records
        idlabel = Label(student_form, text="Student id", font=('bold', 12), pady=20)
        idlabel.grid(row=0, column=0, sticky=W)
        self.st_idtextbox = Entry(student_form, textvariable=self.st_idtxt)
        self.st_idtextbox.grid(row=0, column=1)

        namelabel = Label(student_form, text="Name", font=('bold', 12), pady=20)
        namelabel.grid(row=1, column=0, sticky=W)
        self.nametextbox = Entry(student_form, textvariable=self.nametxt)
        self.nametextbox.grid(row=1, column=1)

        surnamelabel = Label(student_form, text="Surname", font=('bold', 12), pady=20)
        surnamelabel.grid(row=2, column=0, sticky=W)
        self.surnametextbox = Entry(student_form, textvariable=self.surnametxt)
        self.surnametextbox.grid(row=2, column=1)

        st_celllabel = Label(student_form, text="Cell Number", font=('bold', 12), pady=20)
        st_celllabel.grid(row=3, column=0, sticky=W)
        self.st_celltextbox = Entry(student_form, textvariable=self.st_celltxt)
        self.st_celltextbox.grid(row=3, column=1)

        emaillabel = Label(student_form, text="Email", font=('bold', 12), pady=20)
        emaillabel.grid(row=4, column=0, sticky=W)
        self.emailtextbox = Entry(student_form, textvariable=self.emailtxt)
        self.emailtextbox.grid(row=4, column=1)

        courselabel = Label(student_form, text="Course", font=('bold', 12), pady=20)
        courselabel.grid(row=5, column=0, sticky=W)
        self.coursetextbox = Entry(student_form, textvariable=self.coursetxt)
        self.coursetextbox.grid(row=5, column=1)

        # Add buttons for CRUD operations
        add_button = Button(student_form, text="Add", command=self.add_student)
        add_button.grid(row=6, column=0)

        update_button = Button(student_form, text="Update", command=self.update_student)
        update_button.grid(row=6, column=1)

        delete_button = Button(student_form, text="Delete", command=self.delete_student)
        delete_button.grid(row=6, column=2)

        # Add listbox for students
        student_form.list = Listbox(student_form, height=15, width=50)
        student_form.list.grid(row=0, column=2, columnspan=4, rowspan=7, pady=20, padx=20)
        student_form.list.bind("<<ListboxSelect>>", self.on_select)

    # Function to clear all textboxes
    def clear_textboxes(self):
        self.st_idtxt.set("")
        self.nametxt.set("")
        self.surnametxt.set("")
        self.st_celltxt.set("")
        self.emailtxt.set("")
        self.coursetxt.set("")

    def on_select(self, event):
        global selected_item
        index = self.list.curselection()[0]
        selected_item = self.list.get(index)

        self.st_idtextbox.delete(0, END)
        self.st_idtextbox.insert(END, selected_item[1])
        self.nametextbox.delete(0, END)
        self.nametextbox.insert(END, selected_item[2])
        self.surnametextbox.delete(0, END)
        self.surnametextbox.insert(END, selected_item[3])
        self.st_celltextbox.delete(0, END)
        self.st_celltextbox.insert(END, selected_item[4])
        self.emailtextbox.delete(0, END)
        self.emailtextbox.insert(END, selected_item[5])
        self.coursetextbox.delete(0, END)
        self.coursetextbox.insert(END, selected_item[6])

    def add_student(self):
        try:
            AddStudent().add_student(self)
            GUIApp.populate_lecturer_ListBox(self)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        global selected_item
        UpdateStudent().update_student(self, selected_item[0])

    def delete_student(self):
        global selected_item
        DeleteStudent().delete_student(self, selected_item[0])

    def populateListBox(self):
        PopulateListBox().populateListBox(self)

    def open_lecturer_form(self):
        # Create separate window for lecturer records
        lecturer_form = Toplevel(self.master)
        lecturer_form.title("Manage Lecturers")

        # Adding text variables
        self.l_idtxt = StringVar()
        self.lnametxt = StringVar()
        self.lemailtxt = StringVar()
        self.lcoursetxt = StringVar()
        self.qualificationstxt = StringVar()
        self.departmenttxt = StringVar()

        # Add input fields for student records
        l_idlabel = Label(lecturer_form, text="Lecturer id", font=('bold', 12), pady=20)
        l_idlabel.grid(row=0, column=0, sticky=W)
        self.l_idtextbox = Entry(lecturer_form, textvariable=self.l_idtxt)
        self.l_idtextbox.grid(row=0, column=1)

        lnamelabel = Label(lecturer_form, text="Lecturer Name", font=('bold', 12), pady=20)
        lnamelabel.grid(row=1, column=0, sticky=W)
        self.lnametextbox = Entry(lecturer_form, textvariable=self.lnametxt)
        self.lnametextbox.grid(row=1, column=1)

        lemaillabel = Label(lecturer_form, text="Lecturer Email", font=('bold', 12), pady=20)
        lemaillabel.grid(row=2, column=0, sticky=W)
        self.lemailtextbox = Entry(lecturer_form, textvariable=self.lemailtxt)
        self.lemailtextbox.grid(row=2, column=1)

        lcourselabel = Label(lecturer_form, text="Course Taught", font=('bold', 12), pady=20)
        lcourselabel.grid(row=3, column=0, sticky=W)
        self.lcoursetextbox = Entry(lecturer_form, textvariable=self.lcoursetxt)
        self.lcoursetextbox.grid(row=3, column=1)

        qualificationslabel = Label(lecturer_form, text="Qualifications", font=('bold', 12), pady=20)
        qualificationslabel.grid(row=4, column=0, sticky=W)
        self.qualificationstextbox = Entry(lecturer_form, textvariable=self.qualificationstxt)
        self.qualificationstextbox.grid(row=4, column=1)

        departmentlabel = Label(lecturer_form, text="Department", font=('bold', 12), pady=20)
        departmentlabel.grid(row=5, column=0, sticky=W)
        self.departmenttextbox = Entry(lecturer_form, textvariable=self.departmenttxt)
        self.departmenttextbox.grid(row=5, column=1)

        # Add buttons for CRUD operations
        add_button = Button(lecturer_form, text="Add", command=self.add_lecturer)
        add_button.grid(row=6, column=0)

        update_button = Button(lecturer_form, text="Update", command=self.update_lecturer)
        update_button.grid(row=6, column=1)

        # Add listbox for students
        lecturer_form.list = Listbox(lecturer_form, height=15, width=50)
        lecturer_form.list.grid(row=0, column=2, columnspan=4, rowspan=7, pady=20, padx=20)
        lecturer_form.list.bind("<<ListboxSelect>>", self.on_selectLecturer)

        # Function to clear all textboxes

    def clear_textboxesLecturer(self):
        self.l_idtxt.set("")
        self.lnametxt.set("")
        self.lemailtxt.set("")
        self.lcoursetxt.set("")
        self.qualificationstxt.set("")
        self.departmenttxt.set("")

    def on_selectLecturer(lecturer_form, event):
        global selected_item
        index = lecturer_form.list.curselection()[0]
        selected_item = lecturer_form.list.get(index)

        lecturer_form.l_idtextbox.delete(0, END)
        lecturer_form.l_idtextbox.insert(END, selected_item[1])
        lecturer_form.lnametextbox.delete(0, END)
        lecturer_form.lnametextbox.insert(END, selected_item[2])
        lecturer_form.lemailtextbox.delete(0, END)
        lecturer_form.lemailtextbox.insert(END, selected_item[3])
        lecturer_form.lcoursetextbox.delete(0, END)
        lecturer_form.lcoursetextbox.insert(END, selected_item[4])
        lecturer_form.qualificationstextbox.delete(0, END)
        lecturer_form.qualificationstextbox.insert(END, selected_item[5])
        lecturer_form.departmenttextbox.delete(0, END)
        lecturer_form.departmenttextbox.insert(END, selected_item[6])

    def add_lecturer(self):
        AddStudent().add_student(self)
        GUIApp.populate_lecturer_ListBox(self)

    def update_lecturer(self):
        global selected_item
        UpdateStudent().update_student(self, selected_item[0])

    def populate_lecturer_ListBox(self):
        global selected_item
        PopulateListBox().populate_lecturer_ListBox(self)
