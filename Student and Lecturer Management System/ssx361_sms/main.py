import tkinter as tk
from widgets import GUIApp


def main():
    root = tk.Tk()
    my_gui = GUIApp(root)
    my_gui.add_widgets()
    my_gui.populate_lecturer_ListBox()
    my_gui.populateListBox()
    root.mainloop()


if __name__ == "__main__":
    main()
