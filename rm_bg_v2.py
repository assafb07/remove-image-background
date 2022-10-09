from rembg import remove
from PIL import ImageTk, Image
import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import os



bg = 'orange' ; fg = "#4f4646" ; button_bg = "#ffb303" ; abg = '#806b71'
afg = '#3b2e70' ; fnt = 'gisha' ; fnt_size = '8'
hi = '1' #buttons height;
#wid = '21' #buttons width
wid = '16'

def remove_bg(filename):
    input_path = filename
    global output_path
    output_path = "output.png"
    input = PIL.Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    showImage(output_path)

def select_file():
    global filename
    filename = fd.askopenfilename()
    showImage(image_resize(filename))

def save_image():
    filename = fd.asksaveasfilename(initialfile = 'output01.png',
    defaultextension=".png",filetypes=[("All Files","*.*"),("Image File","*.png")])
    if filename == "":
        pass
    else:
        try:
            original = PIL.Image.open("output.png")
            original.save(filename, format="png")
        except:
            pass

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def showImage(filename):
    clear_frame()
    img = ImageTk.PhotoImage(PIL.Image.open(image_resize(filename)))
    label = Label(frame, image = img)
    label.image = img
    label.pack(side = LEFT)


def image_resize(filename):
    basewidth = 350
    img = PIL.Image.open(filename)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), resample=PIL.Image.BICUBIC)
    img.save('resized_image.png')
    return 'resized_image.png'

def on_closing():
    try:
        os.remove("resized_image.png")
        os.remove("output.png")
        root.destroy()
        print ("See you soon!")
    except:
        print ("See you soon!")
        root.destroy()

def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

before_img = image_resize("resized_image.jpg")
filename = before_img

root = Tk()
root.configure(bg=bg)
#root.geometry()
root.overrideredirect(True)

title_bar = Frame(root, bg=bg)
title_bar.pack(fill=X)
title_bar.bind("<B1-Motion>", move_app)

title_label = Label(title_bar, bg=bg, fg='#f00')
title_label.pack()




frame = Frame(root)
frame.pack()
img = ImageTk.PhotoImage(PIL.Image.open(before_img))
label = Label(frame, image = img)
label.image = img
label.pack(side=LEFT)



top_frame = Frame(root)
top_frame.pack(side=BOTTOM, pady=2)
top_frame.configure(bg = bg)

#top_label = Label(top_frame, text="Background Remover", font=(fnt,'18'), fg="black", bg = label_bg)
#top_label.grid(row = 0, column = 0, columnspan = 3)

open_button = Button(top_frame,text='Open Image', font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=select_file)
open_button.pack(side=LEFT, pady=2)

rm_bg_button = Button(top_frame, text='Remove Background',font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=lambda:remove_bg(filename))
rm_bg_button.pack(side=LEFT, pady=2)

rm_bg_button = Button(top_frame, text='Save Image',font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=lambda:save_image())
rm_bg_button.pack(side=LEFT, pady=2)

rm_bg_button = Button(top_frame, text='Exit',font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=on_closing)
rm_bg_button.pack(side=LEFT, pady=2)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
