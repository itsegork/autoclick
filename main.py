import pyautogui
import tkinter as tk
from tkinter import messagebox
import random
import threading
import time
from pynput import keyboard

# Флаг для управления автокликером
clicking = False

def start_clicking(cps, random_move):
    global clicking
    delay = 1 / cps
    while clicking:
        pyautogui.click()
        if random_move:
            x_move = random.randint(-10, 10)
            y_move = random.randint(-10, 10)
            pyautogui.moveRel(x_move, y_move)
        time.sleep(delay)

def toggle_clicking(cps, random_move):
    global clicking
    if clicking:
        clicking = False
    else:
        clicking = True
        threading.Thread(target=start_clicking, args=(cps, random_move)).start()

def on_activate():
    try:
        cps = 999 # TO DO: исправить! реальный cps сейчас примерно = 10 кликов/с
        random_move = move_var.get()
        toggle_clicking(cps, random_move)
    except ValueError:
        messagebox.showerror("Ошибка", "Обратитесь в поддержку (Telegram): @itsegorkhelp")

def for_canonical(f):
    return lambda k: f(l.canonical(k))

# Настройка слушателя горячих клавиш
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<cmd>+<shift>'),
    on_activate)

def on_press(key):
    try:
        hotkey.press(key)
    except AttributeError:
        pass

def on_release(key):
    try:
        hotkey.release(key)
    except AttributeError:
        pass

# Создание основного окна
root = tk.Tk()
root.title("Автокликер")


# Текст по центру
center_text1 = tk.Label(root, text="Используйте Win + Shift", font=("Helvetica", 12))
center_text1.pack(pady=10)

# Флажок случайного перемещения
move_var = tk.BooleanVar()
move_checkbox = tk.Checkbutton(root, text="Случайное перемещение", variable=move_var, font=("Helvetica", 10))
move_checkbox.pack(pady=5)

center_text2 = tk.Label(root, text="by itsegork", font=("Helvetica", 12))
center_text2.pack(pady=10)

# Запуск слушателя клавиатуры
l = keyboard.Listener(on_press=on_press, on_release=on_release)
l.start()

# Запуск основного цикла Tkinter
root.mainloop()
