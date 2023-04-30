""" This file have all queries to run on database TITANENROLLDB"""
""" All functions will be called and run the query"""

# pyodbc is the module to connect to sql server
import pyodbc as connector
#connection string with needed information

connection_string=(r"Driver={SQL Server};"
               r"Server=CSUF-BJG6303;" # please change this to your server--> run 'select @@SERVERNAME' in sql studio to find your server
               r"Database=PARENTALCONTROL;"
               r"Trusted_Connection=yes;")

#connect to the server and database under that server
conn= connector.connect(connection_string)

#create a cursor to work on the database
cur=conn.cursor()

# 
def authenticateUser(username):
  try:
    cur.execute(f"""select * from UserDetails""")
    for i in cur:
        return i[2]
  except Exception as e:
    print("Unable to login, database connection error")
    return ''

def CreateUser(username,password):
  try:
    cur.execute("INSERT INTO UserDetails (username, upassword) VALUES('x','a')")
    cur.commit()
    return True
  except Exception as e:
    print("Unable to create User, database connection error")
    return False