import tkinter as tk

def button_click():
    print("Button clicked")

root = tk.Tk()
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()
root.mainloop()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import tkinter as tk

root = tk.Tk()
root.geometry("400x300") # set the size of the frame
root.title("My Frame")

# create a label widget
label = tk.Label(root, text="Welcome to My Frame!")
label.pack()

# create a button widget
button1 = tk.Button(root, text="Button 1")
button1.pack()

button2 = tk.Button(root, text="Button 2")
button2.pack()

button3 = tk.Button(root, text="Button 3")
button3.pack()

root.mainloop() # run the main event loop
