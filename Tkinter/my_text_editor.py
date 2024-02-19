from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as tmb
import os 
# Create top level window 
root = Tk()
root.title('My Text Editor')
file_name = None
color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious':'#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue':'#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

# Frame widget to hold the shortcut icons
frame = Frame(root, height=20, bg='khaki')
frame.pack(expand=0, fill=X)

# Text widget to the left to display line numbers
line_numbers = Text(root, width=2, padx=3, bg='khaki', border=0)
line_numbers.pack(fill=Y, side=LEFT)

# main Text widget and Scrollbar widget
content_text = Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

# Create Menu 
menu_bar = Menu(root)
# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

# View Menu
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)

# About Menu
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)

root.config(menu=menu_bar)

# Callbacks
# Cut function
def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()

# Copy function
def copy():
    content_text.event_generate("<<Copy>>")
    on_content_changed()

# Paste function
def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()

# Undo function
def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()

# Redo function
def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break'
# Select All function
def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"
# Find function
def search_output(needle, if_ignore_case, content_text,search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
            nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config('match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))
def find(event=None):
    search_toplevel = Toplevel()
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='IgnoreCase',variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0, command=lambda: search_output(search_entry_widget.get(), ignore_case_value.get(), content_text, search_toplevel, search_entry_widget)).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=2)
    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
        search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
        return "break"
# open_file function
def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{}'.format(os.path.basename(file_name)))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())
    on_content_changed()

# Save function
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
# Save as function
def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{}'.format(os.path.basename(file_name)))
    return "break"
def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:the_file.write(content)
    except IOError:
        pass
    # pass for now but we show some warning - we do this in next iteration
# new_file function
def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0,END)
# about function
def about(event=None):
    tmb.showinfo(title='About page', message="{}".format('Tkinter GUI Application\n Development Blueprints"'))

# help function
def helper(event=None):
    tmb.showinfo(title='Help page', message='Help page')

# exit function
def exit_file(event=None):
    if tmb.askokcancel("Quit?", "Really quit?"):
        root.destroy()
root.protocol('WM_DELETE_WINDOW', exit_file)
def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i)+ '\n'
    return output

def update_line_numbers(event = None):
    pass
    # line_numbers = get_line_numbers()    
    # line_number_bar.config(state='normal')
    # line_number_bar.delete('1.0', 'end')
    # line_number_bar.insert('1.0', line_numbers)
    # line_number_bar.config(state='disabled')
def on_content_changed(event=None):
    update_line_numbers()

def change_theme(event=None):
    selected_theme = theme_name.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(background=background_color, fg=foreground_color)
# Event Binding
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-f>', find)
content_text.bind('<Control-F>', find)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<KeyPress-F1>', help)
content_text.bind('<Any-KeyPress>', on_content_changed)
# Adding menuItems

# File Menu menuItems
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', underline=0, command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', underline=0, command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', underline=0, command=save)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S', compound='left', underline=0, command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=0, command=exit_file)
# Edit Menu menuItems
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', underline=0, command=find)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=7, command=select_all)
# View Menu menuItems
show_line_number = IntVar()
cursor_location = BooleanVar()
theme_name = StringVar()
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number)
view_menu.add_checkbutton(label='Show Cursor LOcation at Bottom', variable=cursor_location)
view_menu.add_checkbutton(label='Highlight Current Line')
# Theme Menu
theme_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_radiobutton(label='Default', variable=theme_name)
theme_menu.add_radiobutton(label='AquaMarine', variable=theme_name)
theme_menu.add_radiobutton(label='Bold Beige', variable=theme_name)
theme_menu.add_radiobutton(label='Cobalt Blue', variable=theme_name)
theme_menu.add_radiobutton(label='Graygarious', variable=theme_name)
theme_menu.add_radiobutton(label='Night Mode', variable=theme_name)
theme_menu.add_radiobutton(label='Olive Green', variable=theme_name, command=change_theme)

# About Menu menuItems
about_menu.add_command(label='About', command=about)
about_menu.add_command(label='Help', command=helper)

root.mainloop()