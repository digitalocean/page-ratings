import os
import mysql.connector

def main(args):
    print(os.getenv('DB_HOST'))
    '''
    try:
        
        mydb = mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_DATABASE'),
            port = os.getenv('DB_PORT')
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO ratings (IPAddress, Rating, URL) VALUES ('255.255.255.255', 75, 'https://example.com')"
        mycursor.execute(sql)

        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
    except mysql.connector.Error as error:
        print("Failed to insert record: {}".format(error))
    '''