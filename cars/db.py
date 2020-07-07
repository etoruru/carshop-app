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


def get_idcolor(value):
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (value))
    for x in mycursor:
        idColor = ''.join([str(i) for i in list(x)])
    return idColor

def get_idModel(value):
    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (value))
    for x in mycursor:
        idModel = ''.join([str(i) for i in list(x)])
    return idModel


def get_idBody_type(value):
    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (value))
    for x in mycursor:
        idBody_type = ''.join([str(i) for i in list(x)])
    return idBody_type


def get_idClients(value):
    idClient = None
    mycursor.execute("SELECT idClients FROM Clients WHERE passport_data='%s'" % (value))
    for x in mycursor:
        idClient = ''.join([str(i) for i in list(x)])
    return idClient


def get_idform_payment(value):
    mycursor.execute("SELECT idForm_of_payment FROM Form_of_payment WHERE PaymentName='%s'" % (value))
    for x in mycursor:
        idform_payment = ''.join([str(i) for i in list(x)])
    return idform_payment


def get_colorname(value):
    mycursor.execute("SELECT ColorName FROM Color WHERE idColor=%d" % (value))
    for x in mycursor:
        NameColor = ''.join([str(i) for i in list(x)])
    return NameColor


def get_body_type(value):
    mycursor.execute("SELECT TypeName FROM Body_type WHERE idBody_type=%d" % (value))
    for x in mycursor:
        Body_type = ''.join([str(i) for i in list(x)])
    return Body_type


def get_model_name(value):
    mycursor.execute("SELECT ModelName FROM Models WHERE idModels=%d" % (value))
    for x in mycursor:
        model_name = ''.join([str(i) for i in list(x)])
    return model_name


def get_payment_name(value):
    mycursor.execute("SELECT PaymentName FROM Form_of_payment WHERE idForm_of_payment=%d" % (value))
    for x in mycursor:
        payment_name = ''.join([str(i) for i in list(x)])
    return payment_name


def get_client_firstname(value):
    mycursor.execute("SELECT Firstname FROM Clients WHERE idClients=%d" % (value))
    for x in mycursor:
        client_firstname = ''.join([str(i) for i in list(x)])
    return client_firstname


def get_customer_firstname(value):
    mycursor.execute("SELECT Firstname FROM Customers WHERE idCustomers=%d" % (value))
    for x in mycursor:
        customer_firstname = ''.join([str(i) for i in list(x)])
    return customer_firstname


def check_availability(car_data):
    idOrders = None
    sql_command = 'SELECT idOrders FROM Orders WHERE Cars_idCars=%s' % car_data[0]
    mycursor.execute(sql_command)
    for x in mycursor:
        idOrders = ''.join([str(i) for i in list(x)])
    return idOrders


def get_all_orders():
    sql_command = 'SELECT * FROM Orders'
    mycursor.execute(sql_command)
    return [i for i in mycursor]


def get_all_cars():
    sql_command = 'SELECT * FROM Cars'
    mycursor.execute(sql_command)
    return [i for i in mycursor]
