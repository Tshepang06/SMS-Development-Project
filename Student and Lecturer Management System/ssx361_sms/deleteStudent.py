from db import Database
from tkinter import messagebox


db = Database("ms.db")


class DeleteStudent:
    def delete_student(self, GUIApp, st_id):
        # Check if any item is selected in the listbox
        if st_id():
            db.deleteStudentData(st_id)
            GUIApp.clear_textboxes()
        else:
            messagebox.showerror("No Selection", "Please select a student to delete.")
