from tkinter import END
from db import Database
from tkinter import messagebox

db = Database("ms.db")


class AddStudent:
    def add_student(self,  GUIApp):
        st_id = GUIApp.st_idtxt.get()
        name = GUIApp.nametxt.get()
        surname = GUIApp.surnametxt.get()
        st_cell = GUIApp.st_celltxt.get()
        email = GUIApp.emailtxt.get()
        course = GUIApp.coursetxt.get()

        if name and surname and st_cell and email and course:
            GUIApp.list.delete(0, END)
            # send it to database
            db.insertStudentData(name, surname, st_cell, email, course)
            GUIApp.clear_textboxes()
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showerror("Please fill in all the fields!")
