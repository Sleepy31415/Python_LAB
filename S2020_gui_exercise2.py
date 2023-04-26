"""
Exercise "GUI step 2":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2020.png

Reuse your code from "GUI step 1".

The GUI structure should be this:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import tkinter as tk


def clear_entry_boxes():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)
    print("All entries have been cleared")

#only prints a user. cannot save yet.
def create():
    print(f"you made a new user. {id_entry.get()} {weight_entry.get()} {destination_entry.get()} {weather_entry.get()}")


padx = 10
pady = 10
padding_left_x = 5
padding_ud_down_y = 15
entry_width = 5
main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x150")

# labelframe
lable_frame1 = tk.LabelFrame(main_window, text="Container")
lable_frame1.grid(row=0, column=0)

# frames
labels_and_entries_frame = tk.Frame(lable_frame1)
labels_and_entries_frame.grid(row=0, column=0)
buttons_frame = tk.Frame(lable_frame1)
buttons_frame.grid(row=1, column=0)

# Labels
id_label = tk.Label(labels_and_entries_frame, text="id")
weight_label = tk.Label(labels_and_entries_frame, text="weight")
destination_label = tk.Label(labels_and_entries_frame, text="Destination")
weather_label = tk.Label(labels_and_entries_frame, text="Weather")

# label grids
id_label.grid(row=0, column=0, padx=(padding_left_x*5, padx))
weight_label.grid(row=0, column=1, padx=(padding_left_x, padx))
destination_label.grid(row=0, column=2,padx=(0, padx))
weather_label.grid(row=0, column=3,padx=(0, padx))

# entries
id_entry = tk.Entry(labels_and_entries_frame, width=entry_width, )
weight_entry = tk.Entry(labels_and_entries_frame, width=entry_width * 2)
destination_entry = tk.Entry(labels_and_entries_frame)
weather_entry = tk.Entry(labels_and_entries_frame, width=entry_width * 3)

# entry grids
id_entry.grid(row=1, column=0, padx=(padding_left_x*5, padx))
weight_entry.grid(row=1, column=1, padx=(padding_left_x, padx))
destination_entry.grid(row=1, column=2, padx=(padding_left_x, padx))
weather_entry.grid(row=1, column=3, padx=(padding_left_x, padx))

# buttons
create_button = tk.Button(buttons_frame, text="Create", command=create)
update_button = tk.Button(buttons_frame, text="Update")
delete_button = tk.Button(buttons_frame, text="Delete")
clear_button = tk.Button(buttons_frame, text="Clear Entry Boxes", command=clear_entry_boxes)

# button grids
create_button.grid(row=2, column=0, padx=(padding_left_x, padx), pady=(padding_ud_down_y,padding_ud_down_y))
update_button.grid(row=2, column=1, padx=(padding_left_x, padx), pady=(padding_ud_down_y,padding_ud_down_y))
delete_button.grid(row=2, column=2, padx=(padding_left_x, padx), pady=(padding_ud_down_y,padding_ud_down_y))
clear_button.grid(row=2, column=3, padx=(padding_left_x, padx), pady=(padding_ud_down_y,padding_ud_down_y))

if __name__ == "__main__":
    main_window.mainloop()
