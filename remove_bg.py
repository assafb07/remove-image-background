from rembg import remove
from PIL import ImageTk, Image
import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import os



bg = 'orange' ; fg = "#4f4646" ; button_bg = "#ffb303" ; abg = '#806b71'
afg = '#3b2e70' ; fnt = 'gisha' ; fnt_size = '12'
hi = '1' #buttons height;
wid = '21' #buttons width

def remove_bg(filename):
    input_path = filename
    global output_path
    output_path = "output.png"
    input = PIL.Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    showImage(output_path, "right_frame")

def select_file():
    global filename
    filename = fd.askopenfilename()
    showImage(image_resize(filename), "left_frame")

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

def clear_frame(where):
    if where == "left_frame":
        for widgets in left_frame.winfo_children():
            widgets.destroy()
    else:
        for widgets in right_frame.winfo_children():
            widgets.destroy()

def showImage(filename, where):
    clear_frame(where)
    img = ImageTk.PhotoImage(PIL.Image.open(image_resize(filename)))
    if where == "left_frame":
        label = Label(left_frame, image = img)
    else:
        label = Label(right_frame, image = img)
    label.image = img
    label.grid(row = 0, column = 0)


def image_resize(filename):
    basewidth = 300
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


before_img = "before.png"
after_img = "after.png"

root = Tk()
root.configure(bg="orange")
root.title("Remove Image Background")
top_frame = Frame(root)
top_frame.grid(row = 1, column = 0, columnspan = 3)
top_frame.configure(bg = bg)

left_frame = Frame(root)
left_frame.grid(row = 0, column = 0, padx = "3", pady = "3")
img = ImageTk.PhotoImage(PIL.Image.open(before_img))
label = Label(left_frame, image = img)
label.image = img
label.grid(row = 0, column = 0, padx = "3", pady = "3")

right_frame = Frame(root)
right_frame.grid(row = 0, column = 1, padx = "3", pady = "3")
img = ImageTk.PhotoImage(PIL.Image.open(after_img))
label = Label(right_frame, image = img)
label.image = img
label.grid(row = 0, column = 0, padx = "3", pady = "3")

#top_label = Label(top_frame, text="Background Remover", font=(fnt,'18'), fg="black", bg = label_bg)
#top_label.grid(row = 0, column = 0, columnspan = 3)

open_button = Button(top_frame,text='Open Image', font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=select_file)
open_button.grid(row = 1, column = 0, padx = "3", pady = "5")

rm_bg_button = Button(top_frame, text='Remove Background',font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=lambda:remove_bg(filename))
rm_bg_button.grid(row = 1, column = 1, padx = "3", pady = "5")

rm_bg_button = Button(top_frame, text='Save Image',font=(fnt,fnt_size), fg=fg, bg=button_bg, activebackground = abg,
activeforeground = afg, height = hi, width = wid, command=lambda:save_image())
rm_bg_button.grid(row = 1, column = 2, padx = "3", pady = "5")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
