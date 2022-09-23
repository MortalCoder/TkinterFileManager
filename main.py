import os
import json
import tkinter as tk


class FileManager:
    def __init__(self):

        with open("settings.json", "r") as read_file:
            settings = json.load(read_file)


        color_scheme = settings['color_themes']['standard']

        # Setting up the main window
        self.root = tk.Tk()
        self.root.configure(bg=color_scheme['bg'])
        self.root.title('Tkinter File Manager')
        self.root.geometry("900x600+300+100")
        self.root.resizable(False, False)

        # The frame for main functionality
        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg=color_scheme['hlt'], width=400)
        self.main_frame.pack(side='left', anchor='e', fill='y')

        # The side frame for buttons
        self.side_frame = tk.Frame(self.root)
        self.side_frame.configure(bg=color_scheme['bg'])
        self.side_frame.pack(side='top', anchor='nw', fill='y')

        # The logo of Financial University
        self.logo = tk.PhotoImage(file='Logo.png')
        tk.Label(self.side_frame, image=self.logo, bd=0).grid(row=4, column=0)

        # The text label
        self.main_label = tk.Label(self.main_frame, width=50)
        self.main_label.pack(side='bottom', fill=tk.BOTH, expand='yes')
        # The text label
        self.main_entry = tk.Entry(self.main_frame, width=50)
        self.main_entry.pack(side='top', fill='both', expand='yes')

        #
        self.bt_make_folder = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'], command=self.make_folder,
            highlightcolor=color_scheme['hlt'], text='Make folder', width=50, height=4)
        self.bt_make_folder.grid(row=0, column=0, padx=10, pady=15)
        #
        self.bt_delete_folder = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            highlightcolor=color_scheme['hlt'], text='Delete folder', width=50, height=4)
        self.bt_delete_folder.grid(row=1, column=0, padx=10, pady=15)
        #
        self.bt_go_to = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            highlightcolor=color_scheme['hlt'], text='Go to folder', width=50, height=4)
        self.bt_go_to.grid(row=2, column=0, padx=10, pady=15)
        #
        self.bt_make_file = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            highlightcolor=color_scheme['hlt'], text='Make file', width=50, height=4)
        self.bt_make_file.grid(row=3, column=0, padx=10, pady=15)

        print(settings)
        print(os.getcwd())

    def make_folder(self):
        os.mkdir(self.main_entry.get() if self.main_entry.get() != '' else 'default')
        self.main_label['text'] = 'Folder made'


if __name__ == "__main__":
    file_manager = FileManager()
    os.chdir('C:/Root')
    file_manager.root.mainloop()
