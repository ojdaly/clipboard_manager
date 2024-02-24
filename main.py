from tkinter import *

# Open window
window = Tk()
window.title("Clipboard Manager")
window.minsize(width=200, height=100)

FONT_NAME="arial"
FONT_SIZE=16

# old_gather = ""
row_num = 0
button_list = []
label_list = []
delete_list = []
text_list = []

def read_clipboard():
    # global old_gather
    global label_num
    global row_num
    try:
        gather = window.clipboard_get()
    except:
        print("error")
        gather = None
    #If copied text wasn't just copied, and is less than a number of characters.
    #if gather != old_gather and len(gather) <= 75:
    if gather not in text_list and len(gather) <= 75:
        text_list.append(gather)
        print(text_list)
        print(row_num)
        # Print copied text in window.
        label = str(row_num)
        label = Label(text=gather, font=(FONT_NAME, FONT_SIZE, "bold"))
        label.grid(row=row_num, column=0)
        label_list.append(label)
        # Create button to copy text.
        button = str(row_num)
        button = Button(text="Copy", command=lambda:write_clipboard(gather))
        button.text_value = gather
        button.grid(row=row_num, column=1)
        button_list.append(button)
        # Write to text file if desired.
        # with open("clipboard.txt", "a") as data:
        #     data.write(f"{gather}\n")
        #
        #Create delete button.
        delete = str(row_num)
        delete = Button(text="Delete", command=lambda: delete_command(gather))
        delete.text_value = gather
        delete.grid(row=row_num, column=2)
        delete_list.append(delete)
        row_num += 1
    window.after(2000, read_clipboard)

# Deletes text and both buttons.
def delete_command(gather):
    global button_list
    global label_list
    global delete_list
    row_num_d = 0
    button_list_d = button_list.copy()
    for b in button_list:
        if b.text_value == gather:
            b.destroy()
            button_list_d.remove(b)
        else:
            b.grid(row=row_num_d, column=1)
            row_num_d += 1
    button_list = button_list_d
    row_num_d = 0
    label_list_d = label_list.copy()
    for l in label_list:
        if l['text'] == gather:
            l.destroy()
            label_list_d.remove(l)
        else:
            l.grid(row=row_num_d, column=0)
            row_num_d += 1
    label_list = label_list_d
    row_num_d = 0
    delete_list_d = delete_list.copy()
    for d in delete_list:
        if d.text_value == gather:
            d.destroy()
            delete_list_d.remove(d)
        else:
            d.grid(row=row_num_d, column=2)
            row_num_d += 1
    delete_list = delete_list_d
    # NEED TO REMOVE TEXT FROM TEXT LIST!!!!!!!
    for t in text_list:
        if t == gather:
            text_list.remove(t)
    delete_list = delete_list_d

# If you use the copy button, it removes text and buttons and places at bottom.
def write_clipboard(gather):
    window.clipboard_clear()
    window.clipboard_append(gather)
    for b in button_list:
        if b.text_value == gather:
            b.destroy()
            button_list.remove(b)
            for l in label_list:
                if l['text'] == gather:
                    l.destroy()
                    label_list.remove(l)
                    for d in delete_list:
                        if d.text_value == gather:
                            d.destroy()
                            delete_list.remove(d)
                            return

read_clipboard()
window.mainloop()