import tkinter as tk
from os import urandom
from random import randint
from PIL import ImageTk, Image

def gen_part():
    s = ''
    for j in range(2):
        ind = randint(0, 35)
        if ind < 10:
            s += str(ind)
        else:
            s += chr(ind + 65 - 10)
    return s

def gen_code():
    HEX = str(int(urandom(5).hex(), 16))
    l = []
    for i in range(3):
        s = gen_part()
        s += HEX[i]
        s += gen_part()
        l.append(s)

    return '-'.join(l) + ' ' + HEX[-2:]

def copy_to_clickboard(rt, code):
    rt.clipboard_clear()
    rt.clipboard_append(code)

def show_image():
    root = tk.Tk()
    root.resizable(False, False)
    root.title('Key generation programme')
    img = Image.open(r"C:\Users\Рома\PycharmProjects\Lab-3\94fd1ff.jpeg")
    width = 600
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    imag = img.resize((width, height), Image.LANCZOS)
    image = ImageTk.PhotoImage(imag)
    code = gen_code()
    label = tk.Label(root, image=image, text=code, compound="center", bg='black', font=('Times', '20', 'bold'))
    label.pack()

    tk.Button(root, text='Quit', command=root.quit, width=10).place(x=265, y=330)
    tk.Button(root, text='Copy', command=copy_to_clickboard(root, code), width=10).place(x=265, y=300)
    root.mainloop()

show_image()