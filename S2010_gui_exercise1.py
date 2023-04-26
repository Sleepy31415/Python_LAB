"""
Exercise "GUI step 1":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2010.png

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

# I had trouble centralizing the widgets and getting button to be lower in the labelframe
import tkinter as tk

padx = 10
pady = 5
main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("125x170")

label_frame1 = tk.LabelFrame(main_window, text="Container")
label_frame1.grid(row=0, columnspan=1, padx= padx, pady=pady, ipadx=padx, ipady=pady*3)

id_label = tk.Label(lable_frame1, text="id", justify="center")
id_label.grid(row=1, column=0, padx=padx*2, pady=pady*1.75)

id_entry = tk.Entry(label_frame1, width=5, justify="center")
id_entry.grid(row=2, column=0, padx = padx*2.5, pady= pady)

id_button = tk.Button(label_frame1, text="create")
id_button.grid(row= 4, column=0, padx= padx, pady = pady*0.25)

if __name__ == "__main__":
    main_window.mainloop()