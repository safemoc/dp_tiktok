from customtkinter import *

class App(object):
    def __init__(self):
        self.window = CTk()
        self.__create_window()
        self.button_clicked()

    def __create_window(self):
        self.window.title('my app')
        self.window.geometry('800x600')
        ...

    def button_clicked(self):
        CTkButton(master=self.window, text='click', corner_radius=32, width=50, height=30).place(relx=.5, rely=.7,
                                                                                                 anchor='center')

    def start(self):
        self.window.mainloop()
