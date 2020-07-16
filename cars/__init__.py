# coding=utf-8

import cars.config as config
import cars.db as db

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

import datetime


window = Tk()
window.title(config.app_title)
window.geometry(config.app_geom)



# --------------------Actions--------------------------

#create a dict "field: meaning"
def create_dict(model, bodyType, transmition, color, mileage, engineCapacity, year, price):
    car_dict = {'Model_idModel': model, 'Body_type_idBody_type':bodyType, 'Transmition':transmition,
            'Color_idColor':color, 'Mileage':mileage, 'Engine_capacity':engineCapacity,
            'Year_of_issue':year, 'Price':price
            }
    return car_dict


def between_markers(text, begin, end):
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0

    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index: end_index]


def display_cars(car_data):
    modified_data = between_markers(str(car_data), '(',')')
    values = str(modified_data).split(',')
    idColor, idBody_type, idModel = values[-3:]
    color_name = db.get_colorname(int(idColor))
    body_type = db.get_body_type(int(idBody_type))
    model_name = db.get_model_name(int(idModel))
    values = values[:-3] + [color_name, body_type, model_name] + ['\n']
    key = ['№: ', "Коробка передач: ", "Пробег: ",
           "№РТС: ", "Цена: ", "Год выпуска: ",
           "Объем двигателя: ", "Цвет: ", "Тип кузова: ",
           "Модель: "]
    cars_row = {key[i]: values[i] for i in range(len(key))}
    car_string = ' '
    for key in cars_row.keys():
        car_string += key + cars_row[key] + ' '
    return car_string

def search_color_in_db(value):
    if not(value == ''):
        return db.get_idcolor(color_input_s.get())
    else:
        return ''


# search a car
def search_car():
    where_clauses = []

    idColor = db.search_color_in_db(color_input_s.get())
    idModel = db.search_model_in_db(model_name_input_s.get())
    idBody_type = db.search_body_type_in_db(body_type_input_s.get())
    transmition = transmition_input_s.get()
    mileage = mileage_input_s.get()
    engineCapacity = engine_capacity_input_s.get()
    year = year_issue_input_s.get()
    price = price_input_s.get()

    car_dict = create_dict(idModel, idBody_type, transmition,
                           idColor, mileage, engineCapacity,
                           year, price)
    for key in car_dict.keys():
        if not(car_dict.get(key) == None or car_dict.get(key) == ''):
            where_clauses.append(key + "=" + "'" + car_dict.get(key) + "'")
    where_clauses = ' AND '.join(where_clauses)

    cars = [car for car in db.look_for_cars(where_clauses)]
    print(cars)
    if cars:
        for car in cars:
            if db.check_availability(car) == None:
                txt.insert(INSERT, display_cars(car) + '\n')
    else:
        messagebox.showinfo('Ошибка',"Машина с такими характеристиками отсутствует!")


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
    all_car_text.delete(1.0,END)


def clear():
    txt.delete(1.0,END)


# submit car to database
def add_car():
    idColor = db.get_idcolor(color_input.get())
    idModel = db.get_idModel(model_name_input.get())
    idBody_type = db.get_idBody_type(body_type_input.get())

    values = (transmition_input.get(), mileage_input.get(),
              num_ptc_input.get(), price_input.get(),
              year_issue_input.get(), float(engine_capacity_input.get()),
              int(idColor), int(idBody_type), int(idModel))
    db.add_car(values)
    messagebox.showinfo('','Машина добавлена!')


'''def get_idcar(value):
    idCar = None
    db.execute('SELECT idOrders FROM Orders WHERE Cars_idCars="%s"' % (value))
    for x in mycursor:
        idCar = ''.join([str(i) for i in list(x)])
    return idCar'''


def check_car(idcar):
    print(db.get_idcar(idcar))
    if db.get_idcar(idcar) == None:
        return True
    else:
        return False

def make_order():
    sql_command = "INSERT INTO Orders(Data_of_sale, Cars_idCars, \
                                      Clients_idClients, Customers_idCustomers, \
                                      Form_of_payment_idForm_of_payment) VALUES(%s, %s, %s, %s, %s)"

    customer_firstName = customer_firstName_input.get()
    customer_lastName = customer_lastName_input.get()
    passport_data = passport_data_input.get()
    phone = phone_input.get()
    seller_firstName = seller_firstName_input.get()
    seller_lastName = seller_lastName_input.get()
    seller_position = seller_position_input.get()
    payment_form = payment_form_input.get()
    idseller = idseller_input.get()

    date = datetime.date.today().year

    if  not check_car(idCar_input.get()):
        idCar = None
        messagebox.showinfo('Ошибка', 'Машина уже продана')
    else:
        idCar = idCar_input.get()

    idClient = db.get_idClients(passport_data)
    if idClient == None:
        db.add_client(passport_data, customer_firstName, customer_lastName, phone)
        idClient = db.get_idClients(passport_data)

    idForm_of_payment = db.get_idform_payment(payment_form)
    values = (date, idCar, idClient, idForm_of_payment, idseller)
    val = []
    for data in values:
        if  not data == None:
            val.append(data)
    if len(val) == len(values):
        db.execute(sql_command, values)
        db.commit()
        messagebox.showinfo("", "Заказ оформлен!")
    else:
        messagebox.showinfo("Ошибка!", "Все поля должны быть заполнены!")


def watch_all_cars():
    all_car_text.delete("1.0", END)
    cars = db.get_all_cars()
    for car in cars:
        all_car_text.insert(INSERT, display_cars(car) + '\n')


def modify_str(order_data):
    modified_data = between_markers(str(order_data), '(',')')
    values = str(modified_data).split(',')
    idCar, idClient, idCustomer, idform_payment = values[-4:]
    idModel = db.get_model_from_tCars(idCar)
    models_name = db.get_model_name(int(idModel))
    client_firstName = db.get_client_firstname(int(idClient))
    customer_firstName = db.get_customer_firstname(int(idCustomer))
    payment_name = db.get_payment_name(int(idform_payment))

    values = values[:-4] + [models_name, client_firstName, customer_firstName, payment_name] + ['\n']
    key = ['№: ', "Год продажи: ", "Марка: ",
           "Фамилия клиента: ", "Фамилия продавца: ", "Форма оплаты: "]
    order_row = {key[i]: values[i] for i in range(len(key))}
    order_string = ' '
    for key in order_row.keys():
        order_string += key + order_row[key] + ' '
    return order_string


def show_all_orders():
    orders = db.get_all_orders()
    for order in orders:
        orders_txt.insert(INSERT, modify_str(order) + '\n')


def update_car():
    idCar = idCar_input_c.get()
    idColor = db.search_color_in_db(color_input.get())
    idModel = db.search_model_in_db(model_name_input.get())
    idBody_type = db.search_body_type_in_db(body_type_input.get())

    set_clauses = []

    transmition = transmition_input.get()
    mileage = mileage_input.get()
    engineCapacity = engine_capacity_input.get()
    year = year_issue_input.get()
    price = price_input.get()

    car_dict = create_dict(idModel, idBody_type, transmition,
                           idColor, mileage, engineCapacity,
                           year, price)
    for key in car_dict.keys():
        if not(car_dict.get(key) == None or car_dict.get(key) == ''):
            set_clauses.append(key + "=" + "'" + car_dict.get(key) + "'")
    set_clauses = ', '.join(set_clauses)
    if idCar:
        db.change_cardata(set_clauses, idCar)
        messagebox.showinfo('', 'Данные успешно изменены!')
    else:
        messagebox.showinfo('Ошибка!', 'Для изменения необходимо ввести номер машины!')


def delete_car():
    confirmation = messagebox.askyesno(title='Подтверждение',
                                       message='Вы действительно хотите удалить машину с № %s' % (idCar_input_c.get()))
    if confirmation:
        db.delete_car(idCar_input_c.get())
        messagebox.showinfo('', 'Данные успешно удалены!')




# --------------------Interface--------------------------
tab_control = ttk.Notebook(window)
catalog_tab = ttk.Frame(tab_control)
search_tab = ttk.Frame(tab_control)
order_tab = ttk.Frame(tab_control)
all_orders_tab = ttk.Frame(tab_control)
tab_control.add(catalog_tab, text='Каталог')
tab_control.add(search_tab, text='Поиск')
tab_control.add(order_tab, text='Заказать')
tab_control.add(all_orders_tab, text='Заказы')


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
idCar_label = Label(catalog_tab, text='№ машины: ')

model_name_array = ['BMW', 'Lexus', 'Volvo', 'HONDA']

# Create entry boxes
model_name_input = Combobox(catalog_tab)
model_name_input['values'] = model_name_array
model_name_input.current(1)

body_type_input = Combobox(catalog_tab)
body_type_input['values'] = (
    'Hatchback', 'Sedan',
    'MUV/SUV', 'Coupe', 'Convertible',
    'Wagon', 'Van', 'Jeep'
)
body_type_input.current(1)

transmition_input = Combobox(catalog_tab)
transmition_input['values'] = ('МКПП', 'АКПП')
transmition_input.current(1)

color_array = ['Black', 'White', 'Grey', 'Red', 'Green', 'Blue']
color_input = Combobox(catalog_tab)
color_input['values'] = color_array
color_input.current(1)

mileage_input = Entry(catalog_tab)
engine_capacity_input = Entry(catalog_tab)
num_ptc_input = Entry(catalog_tab)
year_issue_input = Entry(catalog_tab)
price_input = Entry(catalog_tab)
idCar_input_c = Entry(catalog_tab)

# Create buttons
add_car_button = Button(catalog_tab, text='Добавить', command=add_car)
add_car_button.grid(row=9, column=0)

update_car_button = Button(catalog_tab, text='Изменить', command=update_car)
update_car_button.grid(row=10, column=2)

delete_car_button = Button(catalog_tab, text='Удалить', command=delete_car)
delete_car_button.grid(row=10, column=3)


clear_fields_button = Button(catalog_tab,
                             text='Очистить поля',
                             command=clear_fields)
clear_fields_button.grid(row=9, column=1)

watchAll_button = Button(catalog_tab, text='Посмотреть все', command=watch_all_cars)
watchAll_button.grid(row=9, column=2)

# create a window with text
all_car_text = scrolledtext.ScrolledText(catalog_tab, width=40, height=15)
all_car_text.grid(row=0, column=2, padx=20, rowspan=8, columnspan=2)


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
idCar_label.grid(row=10, column=0, sticky=W, padx=10)

model_name_input.grid(row=0, column=1, pady=2)
body_type_input.grid(row=1, column=1, pady=2)
transmition_input.grid(row=2, column=1, pady=2)
color_input.grid(row=3, column=1, pady=2)
mileage_input.grid(row=4, column=1, pady=2)
engine_capacity_input.grid(row=5, column=1, pady=2)
num_ptc_input.grid(row=6, column=1, pady=2)
year_issue_input.grid(row=7, column=1, pady=2)
price_input.grid(row=8, column=1, pady=2)
idCar_input_c.grid(row=10, column=1, pady=2)

# ----------------------SEARCH TAB-------------------------
# create labels
model_name_label = Label(search_tab, text='Модель:')
body_type_label = Label(search_tab, text='Тип кузова:')
transmition_label = Label(search_tab, text='Коробка передач:')
color_label = Label(search_tab, text='Цвет:')
mileage_label = Label(search_tab, text='Пробег:')
engine_capacity_label = Label(search_tab, text='Объем двигателя:')
year_issue_label = Label(search_tab, text='Год выпуска:')
price_label = Label(search_tab, text='Цена:')

# create inputs
model_name_input_s = Entry(search_tab)
body_type_input_s = Entry(search_tab)
transmition_input_s = Entry(search_tab)
color_input_s = Entry(search_tab)
mileage_input_s = Entry(search_tab)
engine_capacity_input_s = Entry(search_tab)
year_issue_input_s = Entry(search_tab)
price_input_s = Entry(search_tab)

# create button
search_button = Button(search_tab, text='Поиск',command=search_car)
search_button.grid(row=4, column=1, pady=5)

clear_button = Button(search_tab, text='Очистить',command=clear)
clear_button.grid(row=4, column=2, pady=5)

txt = scrolledtext.ScrolledText(search_tab,width=70,height=10)
txt.grid(column=0,row=5, columnspan=4)

# display on screen
model_name_label.grid(row=0, column=0, sticky=W, padx=10)
body_type_label.grid(row=0, column=2, sticky=W, padx=10)
transmition_label.grid(row=1, column=0, sticky=W, padx=10)
color_label.grid(row=1, column=2, sticky=W, padx=10)
mileage_label.grid(row=2, column=0, sticky=W, padx=10)
engine_capacity_label.grid(row=2, column=2, sticky=W, padx=10)
year_issue_label.grid(row=3, column=0, sticky=W, padx=10)
price_label.grid(row=3, column=2, sticky=W, padx=10)

model_name_input_s.grid(row=0, column=1, padx=10, pady=5)
body_type_input_s.grid(row=0, column=3, padx=10, pady=5)
transmition_input_s.grid(row=1, column=1, padx=10, pady=5)
color_input_s.grid(row=1, column=3, padx=10, pady=5)
mileage_input_s.grid(row=2, column=1, padx=10, pady=5)
engine_capacity_input_s.grid(row=2, column=3, padx=10, pady=5)
year_issue_input_s.grid(row=3, column=1, padx=10, pady=5)
price_input_s.grid(row=3, column=3, padx=10, pady=5)


#----------------------ORDER TAB--------------------------
# create labels for customer
customer_label = Label(order_tab, text='Заказчик: ')
customer_firstName_label = Label(order_tab, text='Фамилия: ')
customer_lastName_label = Label(order_tab, text='Имя: ')
passport_data_label = Label(order_tab, text='Паспортные данные: ')
phone_label = Label(order_tab, text='Телефон: ')

#create labels for seller
seller_label = Label(order_tab, text='Продавец: ')
seller_firstName_label = Label(order_tab, text='Фамилия: ')
seller_lastName_label = Label(order_tab, text='Имя: ')
seller_position_label = Label(order_tab,text='Должность: ')
idseller_label = Label(order_tab, text='ID Продавца: ')
payment_form_label = Label(order_tab, text='Форма оплаты: ')

# create idCar
idCar_label = Label(order_tab, text='id Машины: ')
idCar_input = Entry(order_tab)

#create inputs for customer
customer_firstName_input = Entry(order_tab)
customer_lastName_input = Entry(order_tab)
passport_data_input = Entry(order_tab)
phone_input = Entry(order_tab)

# create inputs for seller
seller_firstName_input = Entry(order_tab)
seller_lastName_input = Entry(order_tab)
seller_position_input = Entry(order_tab)
idseller_input = Entry(order_tab)

# create order button
make_order_button = Button(order_tab, text='Сделать заказ', command=make_order)
make_order_button.grid(row=6, column=3)

#create notification label
notification = Label(order_tab)#, textvariable=text)
notification.grid(row=7, column=0)

# create spinbox for payment
payment_form_input = Combobox(order_tab)
payment_form_input['values'] = ('Cash', 'Cashless')
payment_form_input.current(1)

# display on screen
customer_label.grid(row=0, column=1)
customer_firstName_label.grid(row=1, column=0, sticky=W)
customer_lastName_label.grid(row=2, column=0, sticky=W)
passport_data_label.grid(row=3, column=0, sticky=W)
phone_label.grid(row=4, column=0, sticky=W)

customer_firstName_input.grid(row=1, column=1, padx=10, pady=5)
customer_lastName_input.grid(row=2, column=1, padx=10, pady=5)
passport_data_input.grid(row=3, column=1, padx=10, pady=5)
phone_input.grid(row=4, column=1, pady=5)

seller_label.grid(row=0, column=3)
seller_firstName_label.grid(row=1, column=2, sticky=E)
seller_lastName_label.grid(row=2, column=2, sticky=E)
seller_position_label.grid(row=3, column=2, sticky=E)
idseller_label.grid(row=4, column=2)

seller_firstName_input.grid(row=1, column=3, pady=5)
seller_lastName_input.grid(row=2, column=3, pady=5)
seller_position_input.grid(row=3, column=3, pady=5)
idseller_input.grid(row=4, column=3, pady=5)

idCar_label.grid(row=5, column=0, sticky=W)
idCar_input.grid(row=5, column=1, pady=5)

payment_form_label.grid(row=5, column=2)
payment_form_input.grid(row=5, column=3)

# ------------------ALL ORDERS TAB------------------------
show_orders_button = Button(all_orders_tab, text='Показать все заказы',command=show_all_orders)
show_orders_button.grid(row=1, column=2, pady=5)

orders_txt = scrolledtext.ScrolledText(all_orders_tab,width=70,height=15)
orders_txt.grid(column=0,row=0, columnspan=4)

# ask_idorder = messagebox.askquestion('title', 'content')


tab_control.pack(expand=1, fill='both')
window.mainloop()
