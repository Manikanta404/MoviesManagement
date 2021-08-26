import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('sqlite.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from MovieDataSotre_movie  ''')

#Fetching 1st row from the table
result = cursor.fetchall();
for i in list(result):
    print(i)
    
print("==================================================")
#Query to search movie names based on actor name
print("Enter the name of the Actor:",end="")
x=input()

for i in result:
    if(i[2]==x):
        print(i[1])

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


