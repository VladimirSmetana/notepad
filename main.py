from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

current_file_path = None


def update_title():
    if current_file_path:
        root.wm_title(f"Редактор - {current_file_path}")
    else:
        root.wm_title("Редактор")

def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']

def show_popup(event):
    popup_menu.tk_popup(event.x_root, event.y_root)

def create_popup_menu(root):
    popup_menu = Menu(root, tearoff=0)
    popup_menu.add_command(label="Копировать")
    popup_menu.add_command(label="Вставить")
    popup_menu.add_command(label="Вырезать")
    return popup_menu

def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']

def change_font_size(event):
    # Проверяем, удерживается ли Ctrl
    if event.state & 0x4:
        current_size = int(text_fild.cget("font").split()[1])
        if event.delta > 0:
            new_size = current_size + 1
        else:
            new_size = current_size - 1
        text_fild.config(font=("Arial", new_size))


def notepad_exit(window):
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        window.destroy()

    

def open_new_window(event=None):
    # Создаем главное окно, если оно еще не создано
    if 'root' not in globals():
        global root
        root = Tk()
        root.title('Текстовый редактор')
        root.geometry('600x700')
        root.iconbitmap('notepad.ico')
    
    new_window = Toplevel(root)
    new_window.geometry('600x700')
    new_window.iconbitmap('notepad.ico')

    # Копируем виджеты из основного окна
    new_text_fild = Text(new_window, wrap='word', font=text_fild.cget("font"))
    new_text_fild.pack(expand=1, fill='both')

    # Копируем настройки темы
    new_text_fild['bg'] = text_fild['bg']
    new_text_fild['fg'] = text_fild['fg']
    new_text_fild['insertbackground'] = text_fild['insertbackground']
    new_text_fild['selectbackground'] = text_fild['selectbackground']

    # Копируем меню
    new_menu = Menu(new_window)
    
    # Файл
    file_menu = Menu(new_menu, tearoff=0)
    file_menu.add_command(label="Создать", command=open_new_window)
    file_menu.add_command(label='Открыть', command=open_file)
    file_menu.add_command(label='Сохранить', command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label='Закрыть', command=lambda: notepad_exit(new_window))
    new_window.protocol("WM_DELETE_WINDOW", lambda: notepad_exit(new_window))
    new_menu.add_cascade(label='Файл', menu=file_menu)

    # Вид
    view_menu = Menu(new_menu, tearoff=0)
    view_menu_sub = Menu(view_menu, tearoff=0)
    font_menu_sub = Menu(view_menu, tearoff=0)
    view_menu_sub.add_command(label='Тёмная', command=lambda: chenge_theme('dark'))
    view_menu_sub.add_command(label='Светлая', command=lambda: chenge_theme('light'))
    view_menu.add_cascade(label='Тема', menu=view_menu_sub)

    font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
    font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
    font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
    view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
    
    new_menu.add_cascade(label='Вид', menu=view_menu)

    new_window.config(menu=new_menu)
    popup_menu = create_popup_menu(new_window)
    new_text_fild.bind("<Button-3>", show_popup)


def open_file(event=None):
    global current_file_path
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        current_file_path = file_path
        text_fild.delete('1.0', END)
        with open(file_path, encoding='utf-8') as file:
            text_fild.insert('1.0', file.read())
        update_title()

def save_file(event=None):
    global current_file_path
    if current_file_path:
        with open(current_file_path, 'w', encoding='utf-8') as file:
            text = text_fild.get('1.0', END)
            file.write(text)
        update_title()
    else:
        save_file_as()


def save_file_as():
    global current_file_path
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        current_file_path = file_path
        with open(file_path, 'w', encoding='utf-8') as file:
            text = text_fild.get('1.0', END)
            file.write(text)
        update_title()

root = Tk()

root.title('Текстовый редактор')
root.geometry('600x700')
root.iconbitmap('notepad.ico')

main_menu = Menu(root)
root.config(menu=main_menu)


popup_menu = create_popup_menu(root)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

root.protocol("WM_DELETE_WINDOW", lambda: notepad_exit(root))

view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

fonts = {
    'Arial': {
        'font':'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

text_fild = Text(f_text,
                 bg='#FFFACD',
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Arial 14',
                 undo=True
                 )
                 
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

text_fild.bind("<MouseWheel>", change_font_size)
text_fild.bind("<Button-3>", show_popup)
# Добавляем кнопку для открытия нового окна

# open_window_button = Tk.Button(root, text="Создать", command=open_new_window)
# open_window_button.pack(pady=10)

def bind_shortcuts():
    root.bind('<Control-s>', save_file)
    root.bind('<Control-o>', open_file)
    root.bind('<Control-n>', open_new_window)
    root.bind('<Control-z>', lambda event: text_fild.edit_undo())
    root.bind('<Control-y>', lambda event: text_fild.edit_redo())

open_new_window()
bind_shortcuts()
update_title()
root.mainloop()