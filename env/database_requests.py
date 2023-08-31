import pyodbc;
import datetime;
import mysql.connector;


def CheckIfUserExists(username, password) -> bool:
    queryString = "SELECT * FROM accounts WHERE username = " + username + " AND password = " + password
    cursor.execute(queryString) 
    row_count = cursor.rowcount
    if row_count == 0:
        return False
    else:
        return True
    

def RegisterUserToDatabase(username, password):
    queryString = "INSERT INTO accounts (username, password) VALUES (" + username + ", " + password + ")"
    cursor.execute(queryString) 
    if cursor.rowcount != 0:
        return "Register succesfull"
    else:
        return "Register Error"

def SubmitHighscoreToDatabase(Username, Score):
    cdt = datetime.datetime.now()
    queryString = "INSERT INTO highscores (username, score, currentDateTime) VALUES (" + Username + ", " + Score + ", " + cdt + ")"
    cursor.execute(queryString)
    if cursor.rowcount != 0:
        return "Submit succesfull"
    else:
        return "Submit Error"


def GetHighscoresFromDatabase():
    queryString = "SELECT * FROM highscores ORDER BY score DESC LIMIT 10"
    cursor.execute(queryString) 
    if cursor.rowcount != 0:
        rows = cursor.fetchall()
        return rows
    else:
        return "Get Highscores Error"


def MakeDbTransaction(transaction):
    GenerateDbConnectionAndCursor()
    #try:
    returnMessage = transaction()
    dbConnection.commit()
    #except:
    returnMessage = "Couldn't commit transaction"
    dbConnection.close()
    print(returnMessage)
    return returnMessage
    
    
def GenerateDbConnectionAndCursor():
    global dbConnection 
    #dbConnection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};ENCRYPT=no;SERVER=127.0.0.1;PORT=3306;Direct=True;DATABASE=Guessing_Game;UID=root')
    dbConnection = mysql.connector.connect(host='localhost', user='root', password='')
    
    #connection = sqlite3.connect("database/db_luftwert.db")
    #pointer = connection.cursor()
    global cursor 
    cursor = dbConnection.cursor()	


def CreateDatabase():
    createDatabaseString = """CREATE DATABASE IF NOT EXISTS Guessing_Game;"""

    createAccountsTableString = """
    USE Guessing_Game;
    CREATE TABLE IF NOT EXISTS Accounts (
        user_id int(11) NOT NULL AUTO_INCREMENT,
        username varchar(64) NOT NULL,
        password varchar(255) NOT NULL,
        PRIMARY KEY (user_id)
    )
    """

    createHighscoresTableString = """
    CREATE TABLE IF NOT EXISTS Highscores (
        score int(11) NOT NULL,
        time_played int(11) NOT NULL,
        timestamp datetime NOT NULL,
        user_id varchar(64),
        FOREIGN KEY user_id REFERENCES Accounts(user_id),
        PRIMARY KEY (timestamp, user_id)
    );"""
    cursor.execute(createDatabaseString)
    cursor.execute(createAccountsTableString)
    cursor.execute(createHighscoresTableString)
    return "Database created"

MakeDbTransaction(CreateDatabase);

"""" 
#dbConnection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};ENCRYPT=no;SERVER=127.0.0.1;PORT=3306;Direct=True;DATABASE=Guessing_Game;UID=root')
dbConnection = mysql.connector.connect(host='127.0.0.1', user='root', password='', database = 'test')

#connection = sqlite3.connect("database/db_luftwert.db")
#pointer = connection.cursor()
cursor = dbConnection.cursor()	
cursor.execute('SELECT * FROM artikel')
print(cursor.fetchall())
"""