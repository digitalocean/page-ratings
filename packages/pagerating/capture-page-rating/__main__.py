import os
import mysql.connector

def main(args):
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
        mycursor.close()
        return {
            'body': {
                'response_type': 'in_channel',
                'text': str(mycursor.rowcount) + "record inserted into " + str(os.getenv('DB_HOST')) + ":" + str(os.getenv('DB_DATABASE'))
            }
        }
    except mysql.connector.Error as error:
        return {
            'body': {
                'response_type': 'in_channel',
                'text': "Failed to insert record into " + str(os.getenv('DB_HOST')) + ":" + str(os.getenv('DB_DATABASE')) + ": " + str(error)
            }
        }
