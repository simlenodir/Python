# Bismilah

import pyodbc

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESKTOP-7VDEBLI;'
                               'Database=f19_sql;'
                               'trusted_Connection=yes;'
                               )
print("Connected Successfully")

cursor = connection.cursor()

create_sql = """
    DROP TABLE IF EXISTS Roster;
    CREATE TABLE Roster (
        Namme VARCHAR(50),
        Species VARCHAR(50),
        Age INT
    )
"""

insert_sql = "insert into Roster values ('Benjamin Sisko','Human', 40),('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)"

update_sql = """
    update Roster
    SET Name = 'Ezri Dax'
    where Name = 'Jadzia Dax'
"""

select_sql = "select * from Roster where Species = 'Bajoran'"

cursor.execute(create_sql)
cursor.execute(insert_sql)
data=cursor.execute(select_sql)

print(data.fetchall())
connection.commit()
cursor.close()
connection.close()
