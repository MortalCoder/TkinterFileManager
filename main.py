import os
import json
import tkinter as tk


class FileManager:
    def __init__(self):

        with open("settings.json", "r") as read_file:
            self.settings = json.load(read_file)

        color_scheme = self.settings['color_themes']['standard']

        # Setting up the main window
        self.root = tk.Tk()
        self.root.configure(bg=color_scheme['bg'])
        self.root.title('Tkinter File Manager')
        self.root.geometry("900x600+300+100")
        self.root.resizable(False, False)

        # The frame for main functionality and input
        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg=color_scheme['fg'], width=400)
        self.main_frame.pack(side='left', anchor='e', fill='y')

        # The side frame for buttons
        self.side_frame = tk.Frame(self.root)
        self.side_frame.configure(bg=color_scheme['bg'])
        self.side_frame.pack(side='top', anchor='nw', fill='y')

        # The logo of Financial University
        self.logo = tk.PhotoImage(file='Logo.png')
        #tk.Label(self.side_frame, image=self.logo, bd=0).grid(row=4, column=0)

        os.chdir(self.settings['root_directory'])

        # The top text label
        self.lbl_main = tk.Label(self.main_frame, font='Terminal 24', fg=color_scheme['fg'], width=18,
                                 text='USE THE BOX BELOW\nFOR THE INPUT')
        self.lbl_main.grid(row=1, column=0, padx=10, pady=30)
        # The bottom text label
        self.lbl_info = tk.Label(self.main_frame, font='Terminal 24', width=18, fg=color_scheme['fg'])
        self.lbl_info.grid(row=4, column=0, padx=10, pady=30)
        # The bottom text label
        self.lbl_list = tk.Label(self.main_frame, font='Terminal 12', width=36, fg=color_scheme['fg'],
                                 text='\n'.join(os.listdir()))
        self.lbl_list.grid(row=5, column=0, padx=10, pady=30)
        # The input entry
        self.entry_main = tk.Entry(self.main_frame, font='Terminal 24', width=18, fg=color_scheme['fg'])
        self.entry_main.grid(row=2, column=0, padx=10, pady=10)

        # The make-folder button
        self.bt_make_folder = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.make_folder),
            text='Make folder', width=25, height=4)
        self.bt_make_folder.grid(row=0, column=0, padx=20, pady=15)
        # The delete-folder button
        self.bt_delete_folder = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.delete_folder),
            text='Delete folder', width=25, height=4)
        self.bt_delete_folder.grid(row=1, column=0, padx=20, pady=15)
        # The remove-file button
        self.bt_remove_file = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.remove_file),
            text='Remove file', width=25, height=4)
        self.bt_remove_file.grid(row=1, column=1, padx=20, pady=15)
        # The go-to button
        self.bt_go_to = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.go_to),
            text='Go to folder', width=25, height=4)
        self.bt_go_to.grid(row=2, column=0, padx=20, pady=15)
        # The go-up button
        self.bt_go_up = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.go_up),
            text='Go up', width=25, height=4)
        self.bt_go_up.grid(row=2, column=1, padx=20, pady=15)
        # The go-up button
        self.bt_rename_file = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.rename),
            text='Rename file/folder', width=25, height=4)
        self.bt_rename_file.grid(row=0, column=1, padx=20, pady=15)
        # The make-file button
        self.bt_make_file = tk.Button(
            self.side_frame, bg=color_scheme['fg'], fg=color_scheme['text'],
            command=lambda: self.set_active_function(self.make_file),
            text='Make file', width=25, height=4)
        self.bt_make_file.grid(row=3, column=0, padx=20, pady=15)
        # The confirm button
        self.bt_confirm = tk.Button(
            self.main_frame, bg=color_scheme['bg'], fg=color_scheme['text'], command=self.confirm,
            text='Confirm', width=25, height=4)
        self.bt_confirm.grid(row=3, column=0, padx=20, pady=15)

        print(self.settings)
        print(os.getcwd())

        self.active_function = None

    def set_active_function(self, function):
        self.active_function = function

    def confirm(self):
        if self.active_function:
            self.active_function()
        else:
            self.lbl_info['text'] = 'NOTHING TO DO'
        self.lbl_list['text'] = '\n'.join(os.listdir())
        self.entry_main['text'] = ''

    def make_folder(self):
        try:
            os.mkdir(self.entry_main.get() if self.entry_main.get() != '' else 'default')
            self.lbl_info['text'] = 'FOLDER MADE'
        except OSError:
            self.lbl_info['text'] = 'ERROR'

    def delete_folder(self):
        try:
            os.rmdir(self.entry_main.get() if self.entry_main.get() != '' else '')
            self.lbl_info['text'] = 'FOLDER DELETED'
        except OSError:
            self.lbl_info['text'] = 'ERROR'

    def rename(self):
        try:
            assert self.entry_main.get() != ''
            os.rename(self.entry_main.get().split('|')[0], self.entry_main.get().split('|')[1])
            self.lbl_info['text'] = 'RENAMED'
        except AssertionError:
            self.lbl_info['text'] = 'ERROR'

    def remove_file(self):
        try:
            assert self.entry_main.get() != ''
            os.remove(self.entry_main.get())
            self.lbl_info['text'] = 'FILE REMOVED'
        except:
            self.lbl_info['text'] = 'ERROR'

    def go_to(self):
        try:
            os.chdir(self.entry_main.get() if self.entry_main.get() != '' else '.')
            self.lbl_info['text'] = 'PATH CHANGED'
        except OSError:
            self.lbl_info['text'] = 'ERROR'

    def go_up(self):
        try:
            assert len(os.getcwd()) > 7
            os.chdir('..')
            self.lbl_info['text'] = 'PATH BACKED'
        except AssertionError:
            self.lbl_info['text'] = 'UNABLE TO\nGO FURTHER'

    def make_file(self):
        try:
            with open(f'{self.entry_main.get()}.txt' if self.entry_main.get() != '' else 'default.txt', 'w') as file:
                self.lbl_info['text'] = 'File made'
        except:
            self.lbl_info['text'] = 'ERROR'


if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.root.mainloop()
