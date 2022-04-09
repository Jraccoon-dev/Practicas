import pyodbc

server = 'MONSTER\SQLEXPRESS'
bd = 'PassManager'
usr = 'userpython'
passwd = '123456789'


try:
    connectionServer = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+';DATABASE='+bd+';UID='+usr+';PWD='+passwd)
    print('connected')
except:
    print('Error connect')


cursor = connectionServer.cursor()
cursor.execute("select * from cuentas")

#primer metodo query--------------------------------

# accounts = cursor.fetchone()

# while accounts:
#     print(accounts)
#     accounts = cursor.fetchone()

#segundo metodo query--------------------------------

# accounts = cursor.fetchall()
# for account in accounts:
#    print(account)

#primer metodo insert data--------------------------

username = "Alex"
email = "alex@mail.com"
password = "123455"

# query = "Insert into cuentas(Username, Email, Passwd) values ('Alex1','alex1@gmail.com','122234');"
# cursor.execute(query)

#segundo metodo insert data-------------------------

query = "Insert into cuentas(Username, Email, Passwd) values (?,?,?);"
cursor.execute(query,'Alex2','alexmanrin@mamistaspueblas.com','haremforever')

cursor.commit() #confirmar cambios

cursor.close()
connectionServer.close()
