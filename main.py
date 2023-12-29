from tkinter import *
from tkinter import filedialog, colorchooser
import os
import Functions


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Select Programm')
        self.root.geometry('345x50')
        self.button_input = Button(self.root, text='Image Magnifier', command=self.GUI_IM, width=20)
        self.button_input.grid(row=1, column=1, padx=10, pady=10)

        self.button_output = Button(self.root, text='Delete Background', command=self.GUI_DB, width=20)
        self.button_output.grid(row=1, column=2, padx=10, pady=10)

        self.root.mainloop()

    def GUI_IM(self):
        self.root.destroy()
        GUI_IM()

    def GUI_DB(self):
        self.root.destroy()
        GUI_DB()


def check_files(fol):
    if not list(filter(lambda i: i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"),
                       os.listdir(fol))):  # Check files in "Input images" folder
        return False
    return True


class GUI_IM:
    def __init__(self):
        self.root = Tk()
        self.root.title('Image Magnifier')
        self.root.geometry('330x175')

        self.F_input = False
        self.F_output = False
        self.folder_input = "Select folder with input images"
        self.button_input = Button(self.root, text=self.folder_input, command=self.set_input_folder, width=40)
        self.button_input.grid(row=1, columnspan=4, padx=5, pady=5)

        self.folder_output = "Select folder with output images"
        self.button_output = Button(self.root, text=self.folder_output, command=self.set_output_folder, width=40)
        self.button_output.grid(row=3, columnspan=4, padx=5, pady=5)

        self.entry_x = Entry(self.root, width=30)
        self.label_x = Label(self.root, text="X: ")
        self.entry_x.grid(row=4, column=1, padx=5, pady=5)
        self.label_x.grid(row=4, column=0)

        self.entry_y = Entry(self.root, width=30)
        self.label_y = Label(self.root, text="Y: ")
        self.entry_y.grid(row=5, column=1, padx=5, pady=5)
        self.label_y.grid(row=5, column=0)

        self.button_enter = Button(self.root, text="Enter Image size", command=self.enter)
        self.button_enter.grid(row=4, rowspan=2, column=3, padx=5, pady=5)

        self.x = self.entry_x.get()
        self.y = self.entry_y.get()
        self.F_x = bool(self.x)
        self.F_y = bool(self.y)

        self.button_start = Button(self.root, text="Start", command=self.start, state="disabled")
        self.button_start.grid(row=7, columnspan=4, padx=5, pady=5)

        self.label = Label(self.root, text="Done! :)")
        self.label.grid(row=7, columnspan=4, padx=5, pady=5)

        self.root.mainloop()

    def enter(self):
        self.x = self.entry_x.get()
        self.y = self.entry_y.get()
        if self.x.isdigit() and self.x != 0 and self.y.isdigit() and self.y != 0:
            self.F_x = True
            self.F_y = True
            self.check_button_start()

    def start(self):
        Functions.IM(self.folder_input, self.folder_output).magnifier(int(self.x), int(self.y))
        self.label.config(text="Done! :)")
        self.label.grid(row=7, columnspan=4, padx=5, pady=5)

    def check_button_start(self):
        self.label.config(text="")
        if self.F_input and self.F_output and self.F_x and self.F_y:
            self.button_start.config(state="normal")
        else:
            self.button_start.config(state="disabled")

    def set_input_folder(self):
        self.folder_input = filedialog.askdirectory()
        if self.folder_input != "" and check_files(self.folder_input):
            self.F_input = True
            self.button_input.config(text=".../" + "/".join(self.folder_input.split("/")[-2:]))
            self.check_button_start()

    def set_output_folder(self):
        self.folder_output = filedialog.askdirectory()
        if self.folder_output != "":
            self.F_output = True
            self.button_output.config(text=".../" + "/".join(self.folder_output.split("/")[-2:]))
            self.check_button_start()


class GUI_DB:
    def __init__(self):
        self.root = Tk()
        self.root.title('Image Magnifier')
        self.root.geometry('330x175')
        self.root.after(10)

        self.F_input = False
        self.F_output = False
        self.folder_input = "Select folder with input images"
        self.button_input = Button(self.root, text=self.folder_input, command=self.set_input_folder, width=40)
        self.button_input.grid(row=1, columnspan=4, padx=5, pady=5)

        self.folder_output = "Select folder with output images"
        self.button_output = Button(self.root, text=self.folder_output, command=self.set_output_folder, width=40)
        self.button_output.grid(row=3, columnspan=4, padx=5, pady=5)

        self.button_color = Button(self.root, text="Select color", command=self.sel_color)
        self.button_color.grid(row=4, columnspan=4, padx=5, pady=5)
        self.F_color = False
        self.color = 0

        self.button_start = Button(self.root, text="Start", command=self.start, state="disabled")
        self.button_start.grid(row=5, columnspan=4, padx=5, pady=5)

        self.label = Label(self.root, text="")
        self.label.grid(row=7, columnspan=4, padx=5, pady=5)

        self.root.mainloop()

    def sel_color(self):
        self.color = colorchooser.askcolor(title="Choose color")[0]
        self.F_color = bool(self.color)
        self.check_button_start()

    def start(self):
        Functions.IM(self.folder_input, self.folder_output).deleter(self.F_color)
        self.label.config(text="Done! :)")

    def check_button_start(self):
        self.label.config(text="")
        if self.F_input and self.F_output and self.F_color:
            self.button_start.config(state="normal")
        else:
            self.button_start.config(state="disabled")

    def set_input_folder(self):
        self.folder_input = filedialog.askdirectory()
        if self.folder_input != "" and check_files(self.folder_input):
            self.F_input = True
            self.button_input.config(text=".../" + "/".join(self.folder_input.split("/")[-2:]))
            self.check_button_start()

    def set_output_folder(self):
        self.folder_output = filedialog.askdirectory()
        if self.folder_output != "":
            self.F_output = True
            self.button_output.config(text=".../" + "/".join(self.folder_output.split("/")[-2:]))
            self.check_button_start()


if __name__ == '__main__':
    GUI()
