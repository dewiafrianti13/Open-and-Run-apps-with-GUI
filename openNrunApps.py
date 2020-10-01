import tkinter as tk
from tkinter import filedialog, Text
import os
#Python memiliki banyak modul bawaan, misalnya modul math, os, sys dan lain sebagainya. Modul – modul tersebut berada di dalam direktori Lib ditempat Python terinstall.

root = tk.Tk()
apps =[]
#apps =[x for x in tempApps if x.strip()]

if os.path.isfile('save.txt'):
    #isfile= return True jika filenya ada
    with open('save.txt','r') as f:
        #f=with open('save.txt','r')
        tempApps = f.read()
        tempApps = tempApps.split(',')
        #split memisahkan pathname dengan tanda koma
        apps =[x for x in tempApps if x.strip()]
        #strip () mengembalikan salinan string dengan menghapus karakter di depan dan di belakangnya (berdasarkan argumen string yang diteruskan)
        

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()
        #untuk menghapus widget tkinter dari frame
        #.winfo_children()=mengembalikan daftar semua widget dalam frame, kemudian mengulanginya dan destroy() semuanya.

    filename=filedialog.askopenfilename(initialdir='/', title='select File', filetypes=(('executables','*.exe'),('all files','*.*')))
    #Ekstensi askopenfilename: Dialog yang meminta pemilihan file yang sudah ada

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

#Canvas Tkinter yang keseluruhan (warna ungu)
canvas = tk.Canvas(root, height=500, width=500, bg='#822e73')
canvas.pack()

#untuk bingkai/frame dengan layar putih
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1)
#frame.place(relwidth=0.8, relheight=0.8, relx=0.1)= untuk posisi bingkai di tengah

#menu tombol
openFile =tk.Button(root, text='Open File', padx=15, pady=10, fg='#570609', bg='#7f8077', command=addApp)
openFile.pack()

runApps =tk.Button(root, text='Run Apps', padx=10, pady=5, fg='#94a31d', bg='#000000', command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#mainloop () adalah loop tak terbatas yang digunakan untuk menjalankan aplikasi
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')