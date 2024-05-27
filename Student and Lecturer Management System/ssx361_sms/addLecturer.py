from tkinter import *
from db import Database
from tkinter import messagebox

db = Database("ms.db")


class AddLecturer:
    def add_lecturer(self, GUIApp):
        # Retrieve data from entry fields
        lecturer_id = GUIApp.l_idtxt.get()
        lecturer_name = GUIApp.lnametxt.get()
        lecturer_email = GUIApp.lemailtxt.get()
        department = GUIApp.departtxt.get()
        course_taught = GUIApp.lcoursetxt.get()
        qualifications = GUIApp.qualificationstextbox.get()

        if lecturer_id and lecturer_name and lecturer_email and department and course_taught and qualifications:
            GUIApp.list.delete(0, END)
            messagebox.showinfo("Successfully added")
            # send it to database
            db.insertLecturerData(lecturer_name, lecturer_email, department, course_taught, qualifications)
            GUIApp.clear_textboxes()
        else:
            messagebox.showerror("Error! You could not add")
