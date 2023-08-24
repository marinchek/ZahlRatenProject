import pyodbc 
import datetime;

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
    try:
        returnMessage = transaction()
        dbConnection.commit()
    except:
        returnMessage = "Couldn't commit transaction"
    dbConnection.close()
    return returnMessage
    
    
def GenerateDbConnectionAndCursor():
    global dbConnection 
    dbConnection = pyodbc.connect('DRIVER={Devart ODBC Driver for SQLite};Server=127.0.0.1;Port=3306;Direct=True;Database=Guessing_game;String Types= Unicode')
    global cursor 
    cursor = dbConnection.cursor()	
