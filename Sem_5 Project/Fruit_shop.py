from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime
from ttkthemes import ThemedTk

def fruits_quantity(event):
    selected_item = combobox_fruits.get()
    selected_qty = combobox_qty.get()

    if selected_item == "Banana":
        price_per_kg = 100
    elif selected_item == "Apple":
        price_per_kg = 220
    elif selected_item == "Mango":
        price_per_kg = 70
    elif selected_item == "Lemon":
        price_per_kg = 175
    elif selected_item == "Papaya":
        price_per_kg = 90
    elif selected_item == "Watermelon":
        price_per_kg = 50
    elif selected_item == "Blueberry":
        price_per_kg = 1000
    elif selected_item == "Orange":
        price_per_kg = 70
    elif selected_item == "Kiwi":
        price_per_kg = 300
    else:
        price_per_kg = 0

    try:
        total_price = price_per_kg * int(selected_qty)
        total_pricevalue.set(f"{total_price} Rs")
    except ValueError:
        total_pricevalue.set("")

    kg_value.set(f"{price_per_kg} Rs")

def create_bill():
    name_value = namevalue.get()
    phone_value = phonevalue.get()
    selected_fruit = combobox_fruits.get()
    kg_price = kg_value.get()
    selected_quantity = combobox_qty.get()
    total_price_value = total_pricevalue.get()

    # Get current date and time
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Write data to CSV file
    with open('bill_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date_Time', 'Name', 'Phone', 'Fruit', 'Price_Per_Kg', 'Quantity', 'Total_Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'Date_Time': current_date_time,
            'Name': name_value,
            'Phone': phone_value,
            'Fruit': selected_fruit,
            'Price_Per_Kg': kg_price,
            'Quantity': selected_quantity,
            'Total_Price': total_price_value
        })

    # Clear input fields
    namevalue.set('')
    phonevalue.set('')
    combobox_fruits.set('Select a Fruits')
    combobox_qty.set('Select a Quantity')
    kg_value.set('')
    total_pricevalue.set('')

    # Display success message
    # message_label.config(text="Successfully created bill!")

root = ThemedTk(theme="arc")  # You can choose other themes like "breeze" or "equilux"
root.title("Hashtag Shop")
root.geometry("700x600")
root.minsize(700, 600)
root.maxsize(700, 600)

title = Label(root, text="Fruits And Vegetable's Shop", font=("", 18), foreground="black")
title.grid(row=0, column=7, pady=(20, 0))

fruit_checkbutton = ttk.Checkbutton(root, text="Fruit's", style="TButton")
fruit_checkbutton.grid(row=1, column=3, pady=(10, 0))
vegetable_checkbutton = ttk.Checkbutton(root, text="Vegetable's", style="TButton")
vegetable_checkbutton.grid(row=1, column=9, pady=(10, 0))

name = Label(root, text="Name : ", font=("", 14))
name.grid(row=2, columnspan=5, pady=(10, 0))
namevalue = StringVar()
nameEntry = Entry(root, textvariable=namevalue, width=20, font=("", 14))
nameEntry.grid(row=2, column=1, pady=(10, 0), ipady=8, columnspan=11)

phone = Label(root, text="Phone  : ", font=("", 14))
phone.grid(row=4, columnspan=5, pady=(10, 0))
phonevalue = StringVar()
phoneEntry = Entry(root, textvariable=phonevalue, width=20, font=("", 14))
phoneEntry.grid(row=4, column=1, pady=(10, 0), ipady=8, columnspan=13)

fruit = Label(root, text="Fruits : ", font=("", 14))
fruit.grid(row=5, column=0, columnspan=5, pady=(10, 0))
fruits = ["Apple", "Banana", "Mango", "Lemon","Papaya", "Watermelon", "Blueberry", "Orange", "Kiwi"]
combobox_fruits = ttk.Combobox(root, width=19, font=("", 14), values=fruits)
combobox_fruits.set("Select a Fruits")
combobox_fruits.grid(row=5, column=1, pady=(10, 0), ipady=8, columnspan=15)
combobox_fruits.bind("<<ComboboxSelected>>", fruits_quantity)

price_per_1kg = Label(root, text="Price_Per_1Kg : ", font=("", 14))
price_per_1kg.grid(row=6, column=0, columnspan=5, pady=(10, 0))
kg_value = StringVar()
kg_entry = Entry(root,textvariable=kg_value, font=("", 14), width=20, state="readonly")
kg_entry.grid(row=6, column=1, pady=(10, 0), ipady=9, columnspan=15)

fruits_qty = Label(root, text="Fruits Quantity In Kg: ", font=("", 14))
fruits_qty.grid(row=7, column=0, columnspan=5, pady=(10, 0))

fruits_qty_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
combobox_qty = ttk.Combobox(root, width=19, font=("", 14), values=fruits_qty_values)
combobox_qty.set("Select a Quantity")
combobox_qty.grid(row=7, column=1, pady=(10, 0), ipady=8, columnspan=15)
combobox_qty.bind("<<ComboboxSelected>>", fruits_quantity)

total_price = Label(root, text="Total Price : ", font=("", 14))
total_price.grid(row=8, columnspan=5, pady=(10, 0))

total_pricevalue = StringVar()
total_priceEntry = Entry(root, textvariable=total_pricevalue, font=("", 14), width=20, state="readonly")
total_priceEntry.grid(row=8, column=1, pady=(10, 0), ipady=9, columnspan=15)

button = ttk.Button(root, text="Create Bill",style="TButton", command=create_bill)
button.grid(row=10, column=7, pady=(20, 0))

# message_label = Label(root, text="Successfully created bill!", font=("", 14), fg="green")
# message_label.grid(row=11, column=7, pady=(20, 0))

root.mainloop()

