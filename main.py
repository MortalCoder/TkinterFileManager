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

        self.logo = tk.PhotoImage(file='Logo.png')
        tk.Label(self.root, image=self.logo, bd=0).pack(side="bottom", anchor="se")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(side='right', anchor='e')

        self.side_frame = tk.Frame(self.root)
        self.side_frame.pack(side='top', anchor='nw')

        self.bt_make_folder = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'], highlightcolor=color_scheme['hlt'], text='make_folder')
        self.bt_make_folder.pack(anchor='nw')

        print(settings)


if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.root.mainloop()
