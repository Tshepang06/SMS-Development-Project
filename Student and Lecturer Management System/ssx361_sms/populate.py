from tkinter import END
from db import Database
from tkinter import messagebox


db = Database("ms.db")


class PopulateListBox:
    # method to fetch data from DB
    def populateListBox(self, GUIApp):
        GUIApp.list.delete(0, END)
        if db.fetchStudentData():
            for row in db.fetchStudentData():
                GUIApp.list.insert(END, row)
        else:
            print("Could not fetch data")

    def populate_lecturer_ListBox(self, GUIApp):
        GUIApp.list.delete(0, END)
        if db.fetchLecturerData():
            for row in db.fetchLecturerData():
                GUIApp.list.insert(END, row)
        else:
            messagebox.showerror("Could not fetch data")






