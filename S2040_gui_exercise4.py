"""
Exercise "GUI step 4":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.
use what you've learned in the GUI example files and build the GUI depicted in images/gui_2040.png

Reuse your code from "GUI step 3".

Fill the treeview with test data.
Play with the color values. Find a color combination that you like.

Functionality:
    clicking on the button "clear entry boxes" deletes the text in all entry boxes.
    clicking on a data row in the treeview copies the data of this row into the entry fields.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import tkinter as tk
from tkinter import ttk

padx = 5
pady = 5

#styling colors
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "blue"  # color of selected row in treeview
oddrow = "#7c70b5"
evenrow = "#a6a2ba"




#test data
test_data_list = []
test_data_list.append(("1", "hello", 7000))
test_data_list.append(("2", "data!", 3000))
test_data_list.append(("3", "tests", 3000))
test_data_list.append(("4", "users", 8000))
test_data_list.append(("1", "hello", 6000))
test_data_list.append(("2", "data!", 2000))
test_data_list.append(("3", "tests", 1000))
test_data_list.append(("4", "users", 3000))
test_data_list.append(("1", "hello", 4000))
test_data_list.append(("2", "data!", 5000))
test_data_list.append(("3", "tests", 9000))
test_data_list.append(("4", "users", 7000))

#only prints a user. cannot save yet.
def create():
    print(f"you made a new user. {id_entry.get()} {weight_entry.get()} {destination_entry.get()} {weather_entry.get()}")

def clear_entry_boxes():
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)
    print("All entries have been cleared")


def data_in_treeview(tree):  # fill tree with test data
    count = 0  # Use counter to keep track of odd and even rows, because these will be colored differently. (2)
    for record in test_data_list:
        if count % 2 == 0:  # even
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))  # Insert one row into the data table
        else:  # odd
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))  # Insert one row into the data table
        count += 1

def edit_record(event, tree):  # Copy data from selected row into entry box. Parameter event is mandatory but we don't use it. (1)
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    id_entry.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    id_entry.insert(0, values[0])  # write data into entry box

padx = 10
pady = 10
entry_width = 5
main_window = tk.Tk()
main_window.title('my first GUI')
main_window.geometry("500x150")

# labelframe
lable_frame1 = tk.LabelFrame(main_window, text="Container", padx=padx, pady=pady)
lable_frame1.grid(row=0, column=0)


# frames
scrollbar_and_treeview_frame = tk.Frame(lable_frame1)
labels_and_entries_frame = tk.Frame(lable_frame1)
labels_and_entries_frame.grid(row=1, column=0)
buttons_frame = tk.Frame(lable_frame1)
buttons_frame.grid(row=2, column=0)
scrollbar_and_treeview_frame.grid(row=0, column=0)

#scrollbar
tree_1_scrollbar_1 = tk.Scrollbar(scrollbar_and_treeview_frame) # might be better to put in scrollbar frame

#scrollbar grids
tree_1_scrollbar_1.grid(row=0, column=1, padx=padx, pady=pady, sticky="ns") # why is sticky used?

#treeview
tree_1 = ttk.Treeview(scrollbar_and_treeview_frame, yscrollcommand=tree_1_scrollbar_1.set, selectmode="browse") # why is selectmode used?

#treeview grid
tree_1.grid(row=0, column=0)

#scrollbar config
tree_1_scrollbar_1.config(command=tree_1.yview())



# lambda
tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))  # Define function to be called, when an item is selected. (2)

#treeview columns
tree_1['columns'] = ("Id", "Weight", "Destination")  # define column names
tree_1.column("#0", width=0, stretch=tk.NO)  # Suppress the annoying first empty column.
tree_1.column("Id", anchor=tk.E, width=30)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_1.column("Weight", anchor=tk.W, width=65)
tree_1.column("Destination", anchor=tk.W, width=180)
# Create treeview column headings
tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("Id", text="Id", anchor=tk.CENTER)
tree_1.heading("Weight", text="Weight", anchor=tk.CENTER)
tree_1.heading("Destination", text="Destination", anchor=tk.CENTER)

# row color configure
tree_1.tag_configure('oddrow', background=oddrow)
tree_1.tag_configure('evenrow', background=evenrow)


# Labels
id_label = tk.Label(labels_and_entries_frame, text="id")
weight_label = tk.Label(labels_and_entries_frame, text="weight")
destination_label = tk.Label(labels_and_entries_frame, text="Destination")
weather_label = tk.Label(labels_and_entries_frame, text="Weather")

#treeview styling
style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])  # Define color of selected row in treeview

# label grids
id_label.grid(row=0, column=0, padx=(padx, padx))
weight_label.grid(row=0, column=1, padx=(padx, padx))
destination_label.grid(row=0, column=2,padx=(0, padx))
weather_label.grid(row=0, column=3,padx=(0, padx))

# entries
id_entry = tk.Entry(labels_and_entries_frame, width=entry_width, )
weight_entry = tk.Entry(labels_and_entries_frame, width=entry_width * 2)
destination_entry = tk.Entry(labels_and_entries_frame)
weather_entry = tk.Entry(labels_and_entries_frame, width=entry_width * 3)

# entry grids
id_entry.grid(row=1, column=0, padx=(padx*5, padx))
weight_entry.grid(row=1, column=1, padx=(padx, padx))
destination_entry.grid(row=1, column=2, padx=(padx, padx))
weather_entry.grid(row=1, column=3, padx=(padx, padx))

# buttons
create_button = tk.Button(buttons_frame, text="Create", command=create)
update_button = tk.Button(buttons_frame, text="Update")
delete_button = tk.Button(buttons_frame, text="Delete")
clear_button = tk.Button(buttons_frame, text="Clear Entry Boxes", command=clear_entry_boxes)

# button grids
create_button.grid(row=2, column=0, padx=(padx, padx), pady=(pady,pady))
update_button.grid(row=2, column=1, padx=(padx, padx), pady=(pady,pady))
delete_button.grid(row=2, column=2, padx=(padx, padx), pady=(pady,pady))
clear_button.grid(row=2, column=3, padx=(padx, padx), pady=(pady,pady))

data_in_treeview(tree_1)
if __name__ == "__main__":
    main_window.mainloop()


