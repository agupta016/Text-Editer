from tkinter import *
from tkinter import filedialog, messagebox
import os

class TextEditor:
    # file = None
    current_open_file =  None
    def __init__(self, master):

        self.master = master
        self.master.title("Textpad")
        self.main_menu = Menu(master)
        self.master.config(menu=self.main_menu)
        # *** filemenu
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="SaveAS", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)

        # ***** editmenu
        self.edit_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo" )
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)


        # *** helpmenu
        self.help_menu = Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        # **** textbox
        self.text_box = Text(master, wrap=WORD, undo=TRUE, autoseparators=True, maxundo=-1)
        self.text_box.pack(fill=BOTH, expand=1)

    def new(self):
        answer = messagebox.askyesnocancel('Message', ' Do You want to save it before quit?')

        if answer:
            if self.current_open_file:
                self.save()
            else:
                self.save_as()
        else:
            self.current_open_file = None
            self.master.title("Untitled - Text Editor")
            self.text_box.delete(1.0, END)


    def open(self):
        file = filedialog.askopenfile(initialdir='/home/ayushi/desktop/', title="select file to open", filetypes=(("text files", "*.txt"),("all files", "*.*")))
        # self.master.title(str(os.path.basename(result)) + " - Text Editor")
        if file:
            self.text_box.delete(1.0,END)
            for line in file:
                self.text_box.insert(END,line)
                self.current_open_file = file.name
            self.master.title(self.current_open_file + "  - Text Editor")
            file.close()

    def save(self):
        get_text = str(self.text_box.get('1.0', 'end-1c'))
        if self.current_open_file == None:
            self.save_as()
        else:
            f = open(self.current_open_file, 'w+')
            f.write(get_text)
            f.close()

    def save_as(self):
        get_text = str(self.text_box.get('1.0', 'end-1c'))
        file = filedialog.asksaveasfilename(initialdir='/home/ayushi/desktop/', title="select loaction", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if file:
            save_file = open(file, 'w')
            save_file.write(get_text)
            self.current_open_file = file.name
            self.master.title(self.current_open_file + "  - Text Editor")
            save_file.close()

    def cut(self):
        # self.text_box.event_generate("<<Cut>>")
        self.copy()
        self.text_box.delete("sel.first","sel.last")

    def copy(self):
        # self.text_box.event_generate("<<Copy>>")
        self.text_box.clipboard_clear()
        self.text_box.clipboard_append(self.text_box.selection_get())
    def paste(self):
        # self.text_box.event_generate("<<Paste>>")
        self.text_box.insert(INSERT,self.text_box.clipboard_get())


root = Tk()
t = TextEditor(root)
root.geometry('500x350+300+150')
root.mainloop()
