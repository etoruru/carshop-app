import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


window = Tk()
window.title('CarShop App')
window.geometry('700x400')


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='9884Nadya',
    database='mydb')
mycursor = mydb.cursor()


# Commit changes
mydb.commit()

# --------------------Functions--------------------------

# Add new models into table


# Clear fields function
def clear_fields():
    model_name_input.delete(0, END)
    body_type_input.delete(0, END)
    transmition_input.delete(0, END)
    color_input.delete(0, END)
    mileage_input.delete(0, END)
    engine_capacity_input.delete(0, END)
    num_ptc_input.delete(0, END)
    year_issue_input.delete(0, END)
    price_input.delete(0, END)


# submit car to database
def add_car():
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (color_input.get()))
    for x in mycursor:
        idColor = ''.join([str(i) for i in list(x)])

    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (model_name_input.get()))
    for x in mycursor:
        idModel = ''.join([str(i) for i in list(x)])

    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (body_type_input.get()))
    for x in mycursor:
        idBody_type = ''.join([str(i) for i in list(x)])

    sql_command = 'INSERT INTO Cars(Transmition, Mileage, PTC, Price, Year_of_issue, Engine_capacity, Color_idColor, Body_type_idBody_type, Model_idModel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (transmition_input.get(), mileage_input.get(),
              num_ptc_input.get(), price_input.get(),
              year_issue_input.get(), float(engine_capacity_input.get()),
              int(idColor), int(idBody_type), int(idModel))
    mycursor.execute(sql_command, values)

    # commit changes
    mydb.commit()


# --------------------Interface--------------------------
tab_control = ttk.Notebook(window)
catalog_tab = ttk.Frame(tab_control)
search_tab = ttk.Frame(tab_control)
order_tab = ttk.Frame(tab_control)
tab_control.add(catalog_tab, text='Каталог')
tab_control.add(search_tab, text='Поиск')
tab_control.add(order_tab, text='Заказать')


# ----------------CATALOG-------------------
# create labels
model_name_label = Label(catalog_tab, text='Модель:')
body_type_label = Label(catalog_tab, text='Тип кузова:')
transmition_label = Label(catalog_tab, text='Коробка передач:')
color_label = Label(catalog_tab, text='Цвет:')
mileage_label = Label(catalog_tab, text='Пробег:')
engine_capacity_label = Label(catalog_tab, text='Объем двигателя:')
num_ptc_label = Label(catalog_tab, text='№ РТС:')
year_issue_label = Label(catalog_tab, text='Год выпуска:')
price_label = Label(catalog_tab, text='Цена:')

model_name_array = ['BMW', 'Lexus', 'Volvo']

# Create entry boxes
model_name_input = Combobox(catalog_tab)
model_name_input['values'] = model_name_array

body_type_input = Combobox(catalog_tab)
body_type_input['values'] = (
    'Hatchback', 'Hatchback', 'Sedan',
    'MUV/SUV', 'Coupe', 'Convertible',
    'Wagon', 'Van', 'Jeep'
)


transmition_input = Combobox(catalog_tab)
transmition_input['values'] = ('МКПП', 'АКПП')
transmition_input.current(1)

color_array = ['Black', 'White', 'Grey', 'Red', 'Green', 'Blue']
color_input = Combobox(catalog_tab)
color_input['values'] = color_array


mileage_input = Entry(catalog_tab)
engine_capacity_input = Entry(catalog_tab)
num_ptc_input = Entry(catalog_tab)
year_issue_input = Entry(catalog_tab)
price_input = Entry(catalog_tab)


# Create buttons
add_car_button = Button(catalog_tab, text='Добавить', command=add_car)
add_car_button.grid(row=9, column=0)

clear_fields_button = Button(catalog_tab,
                             text='Очистить поля',
                             command=clear_fields)
clear_fields_button.grid(row=9, column=1)

# display on screen
model_name_label.grid(row=0, column=0, sticky=W, padx=10)
body_type_label.grid(row=1, column=0, sticky=W, padx=10)
transmition_label.grid(row=2, column=0, sticky=W, padx=10)
color_label.grid(row=3, column=0, sticky=W, padx=10)
mileage_label.grid(row=4, column=0, sticky=W, padx=10)
engine_capacity_label.grid(row=5, column=0, sticky=W, padx=10)
num_ptc_label.grid(row=6, column=0, sticky=W, padx=10)
year_issue_label.grid(row=7, column=0, sticky=W, padx=10)
price_label.grid(row=8, column=0, sticky=W, padx=10)

model_name_input.grid(row=0, column=1, pady=5)
body_type_input.grid(row=1, column=1, pady=5)
transmition_input.grid(row=2, column=1, pady=5)
color_input.grid(row=3, column=1, pady=5)
mileage_input.grid(row=4, column=1, pady=5)
engine_capacity_input.grid(row=5, column=1, pady=5)
num_ptc_input.grid(row=6, column=1, pady=5)
year_issue_input.grid(row=7, column=1, pady=5)
price_input.grid(row=8, column=1, pady=5)

# ----------------------SEARCH TAB-------------------------
# create labels
model_name_label = Label(search_tab, text='Модель:')
body_type_label = Label(search_tab, text='Тип кузова:')
transmition_label = Label(search_tab, text='Коробка передач:')
color_label = Label(search_tab, text='Цвет:')
mileage_label = Label(search_tab, text='Пробег:')
engine_capacity_label = Label(search_tab, text='Объем двигателя:')
num_ptc_label = Label(search_tab, text='№ РТС:')
year_issue_label = Label(search_tab, text='Год выпуска:')
price_label = Label(search_tab, text='Цена:')

# create inputs
model_name_input = Entry(search_tab)
body_type_input = Entry(search_tab)
transmition_input = Entry(search_tab)
color_input = Entry(search_tab)
mileage_input = Entry(search_tab)
engine_capacity_input = Entry(search_tab)
year_issue_input = Entry(search_tab)
price_input = Entry(search_tab)

# create button
search_button = Button(search_tab, text='Поиск')


# display on screen
model_name_label.grid(row=0, column=0, sticky=W, padx=10)
body_type_label.grid(row=0, column=2, sticky=W, padx=10)
transmition_label.grid(row=1, column=0, sticky=W, padx=10)
color_label.grid(row=1, column=2, sticky=W, padx=10)
mileage_label.grid(row=2, column=0, sticky=W, padx=10)
engine_capacity_label.grid(row=2, column=2, sticky=W, padx=10)
year_issue_label.grid(row=3, column=0, sticky=W, padx=10)
price_label.grid(row=3, column=2, sticky=W, padx=10)

model_name_input.grid(row=0, column=1, padx=10)
body_type_input.grid(row=0, column=3, padx=10)
transmition_input.grid(row=1, column=1, padx=10)
color_input.grid(row=1, column=3, padx=10)
mileage_input.grid(row=2, column=1, padx=10)
engine_capacity_input.grid(row=2, column=3, padx=10)
year_issue_input.grid(row=3, column=1, padx=10)
price_input.grid(row=3, column=3, padx=10)

search_button.grid(row=4, column=1, pady=5)





tab_control.pack(expand=1, fill='both')
window.mainloop()