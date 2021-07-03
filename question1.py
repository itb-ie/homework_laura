# this question asks what percentage of applications were before 1st dec 2010 and what percentage after dec 1st.
# in the database the application date is a number around 14000. this is the days after epoch (1st Jan 1970).
# the date of dec 1st 2010 in this format is 14945. So I use this to compare and select each application
dec_1_date = 14945 # i used a converted to convert the dec 1st date

import sqlite3

# we need to connect to the database
db = sqlite3.connect("bi-database.sqlite")
cur = db.cursor()

# do a query for all applications that have Application_Date < dec 1st
cur.execute("SELECT * FROM application WHERE Application_Date<?", (dec_1_date,))
rows = cur.fetchall()
first_wave = len(rows)

# do a query for all applications that have Application_Date > dec 1st
cur.execute("SELECT * FROM application WHERE Application_Date>=?", (dec_1_date,))
rows = cur.fetchall()
second_wave = len(rows)

# print the results
print(f"first wave applications {first_wave}, second wave applications {second_wave}")