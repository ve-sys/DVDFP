import sqlite3
import numpy as np
import Data.date as dd
databasename=dd.databasename
from Data.Users import User
from Data.Tema import tema
with sqlite3.connect(databasename) as db:
    cursor= db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS main(tema TEXT,prfl TINYINT,auth INTEGER,foll INTEGER,viewer INTEGER,dec INTEGER, dis INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS reg(ID INTEGER PRIMARY KEY,tema TEXT,auth BIGINT,foll BIGINT,dec BIGINT,dis TEXT,viewer BIGINT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS user(uid BIGINT,prfl TINYINT,status BOOL,name TEXT,mess CHAR,cash TINYINT,year TINYINT)")
def getuser(ID:int):
    db = sqlite3.connect(databasename)
    cursor = db.cursor()
    reg = cursor.execute(f"SELECT uid,prfl,status,name,mess,cash FROM user WHERE uid = ?", (ID,)).fetchone()
    Usr=User(reg[0],reg[1],reg[3],bool(reg[2]),reg[4],reg[5])
    return Usr
def gettema(Name:str):
    db = sqlite3.connect(databasename)
    cursor = db.cursor()
    Out=tema(Name)
    Out.prfl=cursor.execute(f"SELECT prfl FROM main WHERE tema = ?", (Name,)).fetchone()[0]
    ratio = np.array(cursor.execute("SELECT auth,foll,dec,dis,viewer FROM reg WHERE tema = ?", (Name,)).fetchall()).transpose()
    if len(ratio)>0:
        Out.Author= list(filter(lambda x :(x!=None), ratio[0]))
        Out.follower= list(filter(lambda x :(x!=None), ratio[1]))
        Out.Decisive= list(filter(lambda x: (x != None), ratio[2]))
        Out.Description= list(filter(lambda x: (x != None), ratio[3]))
        Out.Viewers= list(filter(lambda x: (x != None), ratio[4]))
    else:
        Out.Author=Out.follower=Out.Decisive=Out.Description=Out.Viewers=[]
    return Out
def gettemes(ID:int):
    user=getuser(ID)
    View=cursor.execute("""
    SELECT MIN(viewer) FROM main 
    WHERE prfl = ?
    """, (user.prfl,)).fetchone()[0]
    Auth=cursor.execute("""
    SELECT MAX(auth) FROM main WHERE 
    prfl = ?  AND viewer = ?
    """, (user.prfl,View)).fetchone()[0]
    Dec=cursor.execute("""
    SELECT MIN(dec) FROM main WHERE 
    prfl = ?  AND viewer = ? AND auth = ?
    """, (user.prfl,View,Auth)).fetchone()[0]
    temes=cursor.execute("""
    SELECT tema,prfl FROM main WHERE
    prfl = ?  AND viewer = ? AND auth = ? AND dec = ?
    """, (user.prfl,View,Auth,Dec)).fetchall()
    print(View, Auth, Dec)
    return temes
def getUserTemes(ID):
    Author=cursor.execute("""
    SELECT tema FROM reg WHERE auth = ?
    """,(ID,)).fetchall()
    return [Author]
def getUserDec(ID):
    dec=cursor.execute("""
    SELECT tema FROM reg WHERE dec = ?
    """,(ID,)).fetchall()
    return [dec]
def getUserFavs(ID):
    follower=cursor.execute("""
    SELECT tema FROM reg WHERE foll = ?
    """,(ID,)).fetchall()
    return [follower]

def DEBUG(Name:str):
    tema=cursor.execute("""
    SELECT tema,prfl,auth,foll,dis,dec,viewer FROM main WHERE tema = ? 
    """,(Name,)).fetchone()
    return tema




