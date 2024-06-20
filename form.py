from tkinter import *
import customtkinter as ctk


root = ctk.CTk()
root.geometry("1000x500")
root.title("Possession Form")


logo = ctk.CTkLabel(root, text='LOGO')
logo.place(x=20, y=10, relx=0.01, rely=0.01)

# Data 

Company = ['Select','DT Infrastructure', 'Downer']
Project = ['Select','Metro', 'TAP', 'EBP - Early Works']
Stations = ['Select','Package 5 & 6', 'Tuggerah', 'Epping']
Possession_type = ['Select','WE', 'WK', 'non-Possession']
#

# Functions 

def button_click():
    print("button clicked")
    company_select.set('')
    project_select.set('')
    station_select.set('')
    possession_select.set('')
    enter_possession_num.delete(0, "end")


def return_value():
    print(company_select)

## clear Combox values

def clear():
    company_select.set('')
    project_select.set('')
    station_select.set('')
    possession_select.set('')
    enter_possession_num.delete(0, "end")



# Test Buttons

test = ctk.CTkButton(root, text='test', command=clear)
test.place(x=480, y=450, relx=0.01, rely=0.01)


# Widgets 

# 0. ID (Title - Company_Project_Station_PossessionType_PossessionNo._Year)

# 1. Drop down Menu - Select Company 

company_select = ctk.CTkComboBox(root, values = Company)
company_select.place(x=20, y=100, relx=0.01, rely=0.01)

# 2. Drop down Menu - Select Project

project_select = ctk.CTkComboBox(root, values = Project)
project_select.place(x=20, y=150, relx=0.01, rely=0.01)

# 3. Drop down Menu - Select Station

station_select = ctk.CTkComboBox(root, values = Stations)
station_select.place(x=20, y=200, relx=0.01, rely=0.01)

# 4. Drop down Menu - Select Possession Type

possession_select = ctk.CTkComboBox(root, values = Possession_type)
possession_select.place(x=20, y=250, relx=0.01, rely=0.01)

# 5. Enter - Select Possession No.

enter_possession_num = ctk.CTkEntry(root)
enter_possession_num.place(x=20, y=300, relx=0.01, rely=0.01)

# 6. Select Start Date

# 7. Finish Date

# 8. Button - Form Submmission

submit_button = ctk.CTkButton(root, text='Submit', command=button_click)
submit_button.place(x=20, y=350, relx=0.01, rely=0.01)

# 9. Button - Update data

update_button = ctk.CTkButton(root, text='Update', command=button_click)
update_button.place(x=480, y=40, relx=0.01, rely=0.01)

# 10. Button - Delete data

delete_button = ctk.CTkButton(root, text='Delete', command=button_click)
delete_button.place(x=680, y=40, relx=0.01, rely=0.01)

# 10. Button - Reset Form Clear Values

reset_button = ctk.CTkButton(root, text='Reset Form', command=clear)
reset_button.place(x=20, y=50, relx=0.01, rely=0.01)

# List Box - Display data
    # Scroll bar

yScroll = Scrollbar(root)
yScroll.pack(side=RIGHT, fill=Y)

xScroll = Scrollbar(root, orient=HORIZONTAL)
xScroll.pack(side=BOTTOM, fill=X)

list = Listbox(root, height=20, width=80, bg='white', yscrollcommand=yScroll.set, xscrollcommand=xScroll.set)
list.place(x=480, y=80, relx=0.01, rely=0.01)
yScroll.config(command=list.yview)
xScroll.config(command=list.xview)



























root.mainloop()