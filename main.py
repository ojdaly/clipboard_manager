import customtkinter

# Text parameters
FONT_NAME="arial"
FONT_SIZE=16

# Creates window
root = customtkinter.CTk()
root.title('Clipboard Manager')

# Creates scrollable frame within window.
my_frame = customtkinter.CTkScrollableFrame(root, height=400, width=475)
my_frame.grid()

row = 0
text_length = 50
label_list = []
copy_button_list = []
delete_button_list = []
text_list = []

# Reads clipboard
def read_clipboard():
    global row
    global text_length
    try:
        gather = root.clipboard_get()
    except:
        gather = "Your next copy will show here."
    # If you haven't already copied, and copied text not over 75 digits
    if gather not in text_list and len(gather) <= 75:
        # Will diden frame if necessary
        if len(gather) > text_length:
            new_width = len(gather) + 630
            my_frame.configure(width=new_width)
            text_length = len(gather)
        text_list.append(gather)
        #Create text and copy and delete buttons
        label_create(gather, row)
        copy_button_create(gather,row)
        delete_button_create(gather, row)
        row += 1
    # Scans clipboard every 2 seconds
    root.after(2000, read_clipboard)

# Creates text (called label in tkinter)
def label_create(gather, row):
    label = customtkinter.CTkLabel(my_frame, text=gather, font=(FONT_NAME, FONT_SIZE, "bold"))
    label.grid(row=row, column=0, pady=4)
    label_list.append(label)

#Creates copy button
def copy_button_create(gather, row):
    copy_button = customtkinter.CTkButton(my_frame, text="copy", width=25, command=lambda: copy_button_push(gather))
    copy_button.grid(row=row, column=1, padx=8)
    copy_button.text_value = gather
    copy_button_list.append(copy_button)

# When you push copy button moves text and buttons to bottom.
def copy_button_push(gather):
    global row
    root.clipboard_clear()
    root.clipboard_append(gather)
    delete_button_push(gather)
    label_create(gather, row)
    copy_button_create(gather, row)
    delete_button_create(gather, row)
    row += 1

# Creates delete button
def delete_button_create(gather, row):
    delete_button = customtkinter.CTkButton(my_frame, text="delete", width=25, command=lambda: delete_button_push(gather))
    delete_button.grid(row=row, column=2)
    delete_button.text_value = gather
    delete_button_list.append(delete_button)

# Deletes everything when you push delete button
def delete_button_push(gather):
    for i in label_list:
        if i.cget("text") == gather:
            label_list.remove(i)
            i.destroy()
    for i in copy_button_list:
        if i.text_value == gather:
            copy_button_list.remove(i)
            i.destroy()
    for i in delete_button_list:
        if i.text_value == gather:
            delete_button_list.remove(i)
            i.destroy()

read_clipboard()

root.mainloop()