import mysql.connector
from mysql.connector import errorcode
# import * from ..config

connection = {
        'user':'root','password':'abhishek@12345','host':'127.0.0.1','auth_plugin':'mysql_native_password'
    }

DB_NAME = ''

TABLES = {}
TABLES['contacts'] = (
    "CREATE TABLE `contacts` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `name` varchar(255) NOT NULL,"
    "   `address` text,"
    "   `phone_number` text,"
    "   PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
    )

def make_connection():
    try:
        cnx = mysql.connector.connect(
            user = connection['user'],
            password = connection['password'],
            host = connection['host'],
            auth_plugin = connection['auth_plugin']
        )
    except mysql.connector.Error as error:
        print('Error Occured: '+error.msg)
    else:
        print('DB Connection Established')
        return cnx

def take_user_name():
    username = str(input('Enter your name:'))
    return username

def create_db(cn):
    db_name = take_user_name() + '_contacts'
    try:
        cursor = cn.cursor()
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print('Error Occured:'+err.msg)
    else:
        cn.database = db_name
        print("{} datbase created successfully".format(db_name))
        print('Creating Tables')
        create_tables(cn)

def create_tables(connection):
	cursor = connection.cursor()
	for table in TABLES:
		tb = TABLES[table]
		try:
			print('Creating table {}'.format(table))
			cursor.execute(tb)
		except mysql.connector.Error as err:
			print('Error Occured:'+err.msg)
		else:
			print("{} table created successfully".format(table))
	print('All tables created!')

def choose_databse(connection):
    cursor = connection.cursor()
    db_name = take_user_name() + '_contacts'
    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print('Database does not exist')
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_db(connection)
            connection.database = db_name
    else:
        connection.database = db_name
        do_operations_on_phonebook(connection)


def do_operations_on_phonebook(connection):
    
    print('Welcome to Phonebook:{} \n'.format(connection.database))
    print('Choose options:\n')
    print('1.Read you contacts')
    print('2.Enter new contact')
    print('3.Exit Contact Book')
    x=0
    while x not in [1,2]:
        x = int(input('Enter choice:'))
        if x == 1:
            read_contacts(connection)
        elif x == 2:
            enter_contact(connection)
        elif x == 3:
            main()

def enter_contact(connection):
    cursor = connection.cursor()
    name = str(input('Enter contact name:'))
    address = str(input('Enter contact address:'))
    phone = str(input('Enter contact number:'))
    query = ('INSERT INTO contacts (name, address, phone_number) VALUES (%(name)s, %(address)s, %(phone)s)')
    data_query = {
        'name':name,
        'address':address,
        'phone':phone
    }
    cursor.execute(query,data_query)
    connection.commit()
    print('Contact Inserted successfully!')
    do_operations_on_phonebook(connection)



def read_contacts(connection):
    cursor = connection.cursor()
    query = ("Select * from contacts")
    cursor.execute(query)
    for (id, name, address, phone_number) in cursor:
        print('-----ID - {}----'.format(id))
        print('Name - {}\n'.format(name))
        print('Address - {}\n'.format(address))
        print('Phone - {}\n'.format(phone_number))
    print('----End of Contacts----')
    do_operations_on_phonebook(connection)


def take_user_input():
    print('Below operations you can do:\n')
    print('1.Create your new Phone Book')
    print('2.Choose already created Phone Book')
    x = 0
    while x not in [1,2]:
        x = int(input('Enter your choice:'))
    return x
def main():
    print('Welcome to Users Phone Book\n')
    userInput = take_user_input()
    cn = make_connection()
    if type(cn).__name__ == 'MySQLConnection':
            if userInput == 1:
                create_db(cn)
            elif userInput == 2:
                choose_databse(cn)
    else:
	    print('Connection Not Established!')
    
        
        
    


main()
