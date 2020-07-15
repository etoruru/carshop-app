# coding=utf-8

import cars.config as config
import mysql.connector


mydb = mysql.connector.connect(
    host=config.db_host,
    #port=config.db_port,
    user=config.db_user,
    passwd=config.db_pass,
    database=config.db_name
)

mycursor = mydb.cursor()


def execute(*args, **kwargs):
    return mycursor.execute(*args, **kwargs)


def commit(*args, **kwargs):
    return mydb.commit(*args, **kwargs)


def get_first_id():
    row = mycursor.fetchone()
    if row:
        return str(row[0])


def get_idcolor(color_name):
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (color_name))
    return get_first_id()


def get_idModel(model_name):
    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (model_name))
    return get_first_id()


def get_idBody_type(type_name):
    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (type_name))
    return get_first_id()


def get_idClients(passport_data):
    mycursor.execute("SELECT idClients FROM Clients WHERE passport_data='%s'" % (passport_data))
    return get_first_id()


def get_idform_payment(payment_name):
    mycursor.execute("SELECT idForm_of_payment FROM Form_of_payment WHERE PaymentName='%s'" % (payment_name))
    return get_first_id()


def get_colorname(id_color):
    mycursor.execute("SELECT ColorName FROM Color WHERE idColor=%d" % (id_color))
    return get_first_id()


def get_body_type(id_body_type):
    mycursor.execute("SELECT TypeName FROM Body_type WHERE idBody_type=%d" % (id_body_type))
    return get_first_id()


def get_model_name(id_model):
    mycursor.execute("SELECT ModelName FROM Models WHERE idModels=%d" % (id_model))
    return get_first_id()


def get_payment_name(id_form_payment):
    mycursor.execute("SELECT PaymentName FROM Form_of_payment WHERE idForm_of_payment=%d" % (id_form_payment))
    return get_first_id()


def get_client_firstname(id_client):
    mycursor.execute("SELECT Firstname FROM Clients WHERE idClients=%d" % (id_client))
    return get_first_id()


def get_customer_firstname(id_customer):
    mycursor.execute("SELECT Firstname FROM Customers WHERE idCustomers=%d" % (id_customer))
    return get_first_id()


def check_availability(car_data):
    sql_command = 'SELECT idOrders FROM Orders WHERE Cars_idCars=%s' % car_data[0]
    mycursor.execute(sql_command)
    return get_first_id()


def get_all_orders():
    sql_command = 'SELECT * FROM Orders'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def get_all_cars():
    sql_command = 'SELECT * FROM Cars'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def search_color_in_db(color):
    if not(color == ''):
        return get_idcolor(color)
    else:
        return ''


def search_model_in_db(model):
    if not(model == ''):
        return get_idModel(model)
    else:
        return ''


def search_body_type_in_db(body_type):
    if not(body_type == ''):
        return get_idBody_type(body_type)
    else:
        return ''


def look_for_cars(values):
    sql_command = "SELECT * FROM Cars WHERE "
    mycursor.execute(sql_command + values)
    return mycursor.fetchall()
