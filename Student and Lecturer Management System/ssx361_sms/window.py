from tkinter import *


class MainApplication(Tk):
    def __init__(self, GUIApp):
        super().__init__()
        self.title("Student and Lecturer Management System")
        self.geometry("600x400")

        self.gui_app = GUIApp(self)
