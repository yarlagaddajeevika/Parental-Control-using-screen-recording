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

#Authenticate User
def authenticateUser(username):
  try:
    cur.execute(f"""select * from UserDetails""")
    for i in cur:
        if(i[2] == username):
          return i[2]
  except Exception as e:
    print("Unable to login, database connection error")
    return ''

#Create new user
def CreateUser(username,password):
  try:
    cur.execute(f"""INSERT INTO UserDetails VALUES ('{username}','{password}')""")
    cur.commit()
    return True
  except Exception as e:
    return False

#Return user id
def returnUserId(username):
  try:
    cur.execute(f"""select userId from UserDetails where username={username}""")
    for i in cur:
      return i[0]
  except Exception as e:
    print("Unable to retrieve user id, database connection error")
    return False

#Store youtube histiry id  view count
def storeIdsCount(userid, counts):
  for key, value in counts.items():
    try:
      cur.execute(f"""INSERT INTO StatisticsData VALUES({userid},{key},{value})""")
      cur.commit()
      return True
    except Exception as e:
      print("Unable to update statistics, database connection error")
      return False
