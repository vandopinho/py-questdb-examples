import psycopg as pg
import random
import time
from datetime import datetime
# Connect to an existing QuestDB instance


conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'
with pg.connect(conn_str, autocommit=True) as connection:
    
    # Open a cursor to perform database operations

    with connection.cursor() as cur:

        # Execute a command: this creates a new table

        cur.execute('''
          CREATE TABLE IF NOT EXISTS dados (
              Datetime STRING,
              PeriodStart TIMESTAMP,
              Name STRING,
              Flow FLOAT,
              FlowSetpoint FLOAT,
              Pressure FLOAT,
              PressureSetpoint FLOAT,
              OverloadValue FLOAT,
              OperationStatus INT,
              OperationType INT,
              OperationMode INT
          ) timestamp(PeriodStart);
          ''')
        
        #print('Table created.')

        # Insert data into the table.
        
        
        while(True):
            for x in range(1000):

                # Converting datetime into millisecond for QuestDB
                name = ["ER151K01", "RP152K02", "RP152K03", "EP151K03", "EP1510KN06", "RP1520KN04", "EP5010KN02", "EP5010KN01", "EP1510KN05", "EP149K01" ,"RP1520KN01", "RP1520KN05" ,"EP151K04"]
                timestamp = time.time_ns() // 1000
                currentDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
                currentMonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                day = random.randint(0, 29)
                i = random.randint(1, 10000)
                press = random.randint(1, 1000)
                o = random.randint(0, 11)
                yn = random.randint(1, 2)
                addDia = str(currentDay[day])+"/"+str(currentMonth[o])
                cur.execute('''
                    INSERT INTO dados
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    ''',
                    (addDia, timestamp, name[o], i, i, press, press, i, yn, yn, yn))
                 

            #print('Rows inserted.')

            #Query the database and obtain data as Python objects.

            # cur.execute('SELECT * FROM dados;')
            # records = cur.fetchall()
            # for row in records:
            #     print(row)

# the connection is now closed

