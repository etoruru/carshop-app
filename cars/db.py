# coding=utf-8

import cars.config as config
import mysql.connector


mydb = mysql.connector.connect(
    host=config.db_host,
    port=config.db_port,
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


def get_idcolor(value):
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (value))
    return get_first_id()


def get_idModel(value):
    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (value))
    return get_first_id()


def get_idBody_type(value):
    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (value))
    return get_first_id()


def get_idClients(value):
    mycursor.execute("SELECT idClients FROM Clients WHERE passport_data='%s'" % (value))
    return get_first_id()


def get_idform_payment(value):
    mycursor.execute("SELECT idForm_of_payment FROM Form_of_payment WHERE PaymentName='%s'" % (value))
    return get_first_id()


def get_colorname(value):
    mycursor.execute("SELECT ColorName FROM Color WHERE idColor=%d" % (value))
    return get_first_id()


def get_body_type(value):
    mycursor.execute("SELECT TypeName FROM Body_type WHERE idBody_type=%d" % (value))
    return get_first_id()


def get_model_name(value):
    mycursor.execute("SELECT ModelName FROM Models WHERE idModels=%d" % (value))
    return get_first_id()


def get_payment_name(value):
    mycursor.execute("SELECT PaymentName FROM Form_of_payment WHERE idForm_of_payment=%d" % (value))
    return get_first_id()


def get_client_firstname(value):
    mycursor.execute("SELECT Firstname FROM Clients WHERE idClients=%d" % (value))
    return get_first_id()


def get_customer_firstname(value):
    return get_first_id()


def check_availability(car_data):
    sql_command = 'SELECT idOrders FROM Orders WHERE Cars_idCars=%s' % car_data[0]
    mycursor.execute(sql_command)
    return get_first_id()


def get_all_orders():
    sql_command = 'SELECT * FROM Orders'
    mycursor.execute(sql_command)
    mycursor.fetchall()


def get_all_cars():
    sql_command = 'SELECT * FROM Cars'
    mycursor.execute(sql_command)
    mycursor.fetchall()
