from db import Database
from tkinter import messagebox


db = Database("ms.db")


class UpdateLecturer:
    def update_lecturer(self, lecturer_form, l_id):
        lecturer_id = lecturer_form.lnametxt.get()
        lecturer_name = lecturer_form.lnametxt.get()
        lecturer_email = lecturer_form.lemailtxt.get()
        department = lecturer_form.departtxt.get()
        course_taught = lecturer_form.lcoursetxt.get()
        qualifications = lecturer_form.qualificationstextbox.get()

        if lecturer_name and lecturer_email and department and course_taught and qualifications and lecturer_id:
            db.updateLecturerData(lecturer_name, lecturer_email, department,
                                  lecturer_email, qualifications, lecturer_id)
            messagebox.showinfo("Successfully updated")
            lecturer_form.clear_textboxes()
            messagebox.showinfo("Successfully updated")
        else:
            messagebox.showerror("Sorry, but could not update!")
