from tkinter import INSERT
import mysql.connector;


global dbConnection 
global cursor 

def CheckIfUserExists(userInfo) -> bool:
    username = userInfo[0]
    password = userInfo[1]
    queryString = "SELECT * FROM accounts WHERE username = '" + username + "' AND password = '" + password + "'"
    globals()["cursor"].execute(queryString) 
    globals()["dbConnection"].commit()
    row_count = globals()["cursor"].rowcount
    if row_count == 0:
        return False
    else:
        return True
    

def RegisterUserToDatabase(userInfo):
    username = userInfo[0]
    password = userInfo[1]
    queryString = "INSERT INTO accounts (username, password) VALUES ('" + username + "', '" + password + "')"
    globals()["cursor"].execute(queryString) 
    globals()["dbConnection"].commit()
    if globals()["cursor"].rowcount != 0:
        return "Register succesfull"
    else:
        return "Register Error"

def SubmitHighscoreToDatabase(accountInfo):
    accountid = accountInfo[2]
    time = accountInfo[1]
    score = accountInfo[0]
    #cdt = datetime.datetime.now()
    queryString = "INSERT INTO Highscores (score, time_played, account_accountid) VALUES (" + str(score) + ", " + str(time) + ", " + str(accountid) + ")"
    globals()["cursor"].execute(queryString)
    globals()["dbConnection"].commit()
    if globals()["cursor"].rowcount != 0:
        return "Submit succesfull"
    else:
        return "Submit Error"


def GetHighscoresFromDatabase():
    queryString = "SELECT * FROM highscores ORDER BY score DESC LIMIT 10"
    globals()["cursor"].execute(queryString)
    globals()["dbConnection"].commit() 
    if globals()["cursor"].rowcount != 0:
        rows = globals()["cursor"].fetchall()
        return rows
    else:
        return "Get Highscores Error"


def MakeDbTransaction(transaction, *args):
    #try:
    if args:
        returnMessage = transaction(*args)
    else:
        returnMessage = transaction()
    #except:
    #globals()["dbConnection"].close()
    print(returnMessage)
    return returnMessage
    
    
def GenerateDbConnectionAndCursor():
    #dbConnection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};ENCRYPT=no;SERVER=127.0.0.1;PORT=3306;Direct=True;DATABASE=Guessing_Game;UID=root')
    globals()["dbConnection"] = mysql.connector.connect(host='localhost', user='root', password='')
    globals()["cursor"] = globals()["dbConnection"].cursor(buffered=True)

    goToDatabaseString = "USE Guessing_Game"	
    globals()["cursor"].execute(goToDatabaseString )



def CreateDatabase():
    #dbConnection = mysql.connector.connect(host='localhost', user='root', password='')
    
    #cursor = globals()["dbConnection"].cursor()
    createDatabaseString = """CREATE DATABASE IF NOT EXISTS Guessing_Game;"""

    goToDatabseString = """USE Guessing_Game"""

    createAccountsTableString = """
    CREATE TABLE IF NOT EXISTS Accounts (
        account_id int(11) NOT NULL AUTO_INCREMENT,
        username varchar(64) NOT NULL,
        password varchar(255) NOT NULL,
        PRIMARY KEY (account_id)
    )
    """

    createHighscoresTableString = """
    CREATE TABLE IF NOT EXISTS Highscores (
        score int(11) NOT NULL,
        time_played int(11) NOT NULL,
        date_time datetime DEFAULT CURRENT_TIMESTAMP,
        account_accountid int(11) NOT NULL,
        CONSTRAINT highscore_account FOREIGN KEY (account_accountid) REFERENCES Accounts(account_id),
        PRIMARY KEY (time_played, account_accountid)
    )"""

    globals()["cursor"].execute(createDatabaseString)
    globals()["cursor"].execute(goToDatabseString)
    globals()["cursor"].execute(createAccountsTableString)
    globals()["cursor"].execute(createHighscoresTableString)
    
    return "Database created"



def FillAccountTable():
    insertIntoAccountsString = """
    INSERT INTO Accounts (username, password)
    VALUES 
    ('test', 'test'),
    ('Dillon', 'Feld'),
    ('Marino', 'Ivakovic'),
    ('Levent', 'Mutlu'),
    ('Leon', 'Graf')
    """

    globals()["cursor"].execute(insertIntoAccountsString)
    globals()["dbConnection"].commit() 
    return "Accounts filled"



def FillHighscoreTable():
    
    insertIntoHighscoresString = """
    INSERT INTO Highscores (score, time_played, account_accountid)
    VALUES 
    (100, 100, 131),
    (200, 200, 132),
    (300, 300, 133),
    (400, 400, 134)
    """
    globals()["cursor"].execute(insertIntoHighscoresString)
    globals()["dbConnection"].commit() 
    return "Highscores filled"



def ClearDataHighscores():
    deleteHighscoresString = """
    DELETE FROM Highscores
    """
    globals()["cursor"].execute(deleteHighscoresString)
    globals()["dbConnection"].commit() 

    return "Highscores cleared"



def ClearDataAccounts():
    deleteAccountsString = """
    DELETE FROM Accounts
    """
    globals()["cursor"].execute(deleteAccountsString)
    globals()["dbConnection"].commit() 

    return "Accounts cleared"



def TestAccountVerification():
    assert CheckIfUserExists(("test", "test"))
    assert CheckIfUserExists(("Dillon", "Feld"))
    assert CheckIfUserExists(("Marino", "Ivakovic"))
    assert CheckIfUserExists(("Levent", "Mutlu"))
    assert CheckIfUserExists(("Leon", "Graf"))
    assert not CheckIfUserExists(("test", "test1"))
    assert not CheckIfUserExists(("test", "Feld"))
    assert not CheckIfUserExists(("test", "Dillon"))
    assert not CheckIfUserExists(("test", "Leon"))
    assert not CheckIfUserExists(("Leon", "test"))

    return "Account Verification Test Succesfull"



def TestDataAccess():
    assert MakeDbTransaction(GetHighscoresFromDatabase) != "Get Highscores Error"
    assert MakeDbTransaction(RegisterUserToDatabase, ("Hans", "Peter")) == "Register succesfull"
    assert MakeDbTransaction(SubmitHighscoreToDatabase, (5, 10, 135)) == "Submit succesfull"
    assert MakeDbTransaction(CheckIfUserExists, ("Hans", "Peter"))
    
    return "Data Access Test Succesfull"



def TestClearData():
    message = MakeDbTransaction(ClearDataHighscores)+ "\n"
    message += MakeDbTransaction(ClearDataAccounts) 
    return message



def SetupDatabase():
    
    GenerateDbConnectionAndCursor()
    #Create the Database & Tables in MySQL
    #CreateDatabase()
    TestClearData()

    #Fill the Database with some Data
    message = MakeDbTransaction(FillAccountTable) + "\n"
    message += MakeDbTransaction(FillHighscoreTable)+ "\n"

    #Check if the Account Verification works
    message += MakeDbTransaction(TestAccountVerification)+ "\n"

    #Check if the data can be accessed
    message += MakeDbTransaction(TestDataAccess)+ "\n"

    #Delete the Dummy-Data
    message += TestClearData()
    #return message
    return message

message = SetupDatabase()
print(message)