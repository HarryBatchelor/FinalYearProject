import csv
import sqlite3
import pandas as pd



#24 inputs every one second
def PoleHitLEFT():
    dbname="sensorsdata.db"
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    TIMEstatment = '''SELECT timestamp FROM ACC_data ORDER BY timestamp DESC limit 140;'''
    curs.execute(TIMEstatment)
    output1 = curs.fetchall()

    Xstatment = '''SELECT x FROM ACC_data ORDER BY timestamp DESC limit 140;'''
    curs.execute(Xstatment)
    output2 = curs.fetchall()

    Ystatment = '''SELECT Y FROM ACC_data ORDER BY timestamp DESC limit 140 ;'''
    curs.execute(Ystatment)
    output3 = curs.fetchall()

    Zstatment = '''SELECT Z FROM ACC_data ORDER BY timestamp DESC limit 140;'''
    curs.execute(Zstatment)
    output4 = curs.fetchall()
    
    dictionary = {'TIME': output1, 'X': output2, 'Y': output3, 'Z': output4}
    dataframe = pd.DataFrame(dictionary) 
    dataframe.to_csv('HitsLEFT.csv', index=False, mode='a')

def PoleHitRIGHT():
    dbname="sensorsdata.db"
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    TIMEstatment = '''SELECT timestamp FROM ACC_data ORDER BY timestamp DESC limit 140;'''
    curs.execute(TIMEstatment)
    output1 = curs.fetchall()

    X2statment = '''SELECT X2 FROM ACC_data ORDER BY timestamp DESC Limit 140 ;'''
    curs.execute(X2statment)
    output5 = curs.fetchall()

    Y2statment = '''SELECT Y2 FROM ACC_data ORDER BY timestamp DESC Limit 140 ;'''
    curs.execute(Y2statment)
    output6 = curs.fetchall()

    Z2statment = '''SELECT Z2 FROM ACC_data ORDER BY timestamp DESC Limit 140 ;'''
    curs.execute(Z2statment)
    output7 = curs.fetchall()

    
    dictionary = {'TIME': output1,'X2': output5, 'Y2': output6, 'Z2': output7}
    dataframe = pd.DataFrame(dictionary)
    dataframe.to_csv('HitsRIGHT.csv', index=False, mode='a')
PoleHitRIGHT()
PoleHitLEFT()
