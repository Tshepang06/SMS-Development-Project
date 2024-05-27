from db import Database


db = Database("ms.db")


class UpdateStudent:
    def update_student(self, GUIApp, st_id):
        name = GUIApp.nametextbox.get()
        surname = GUIApp.surnametextbox.get()
        st_cell = GUIApp.st_celltextbox.get()
        email = GUIApp.emailtextbox.get()
        course = GUIApp.coursetextbox.get()

        if name and surname and st_cell and email and course:
            db.updateStudentData(name, surname, st_cell, email, course, st_id)
            GUIApp.clear_textboxes()
        else:
            print("Sorry, but could not update!")
