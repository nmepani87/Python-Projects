import sqlite3

# connecting to database, if doesn't exist, this with created in same working directory
conn = sqlite3.connect('test2.db')
#with open connection 
with conn:
    cur = conn.cursor()
    # creating and naming table if it doesn't exist, adding primary key and naming
    # 2nd column, whilst also stating its datatype
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename VARCHAR(50) \
        )")
    # getting python to use instructions above
    conn.commit()
# closing connection to database
conn.close()

#connecting to database
conn = sqlite3.connect('test2.db')

#tuple of 'files' to be used to add to database
fileList = ('information.docx', 'Hello.txt', 'myImage.png' \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# getting python to loop through fileList
for x in fileList:
    # if certain parameter met, here it is that is sees a .txt file
    if x.endswith('.txt'):
        # getting python to insert in the table the results of the loop check and print the results in the console too
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
            print(x)
            
#closing database connection          
conn.close()
