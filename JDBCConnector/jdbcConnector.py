import mysql.connector
from JDBCConnector.jdbcConnectorError import JDBCConnectionError

class UserDatabase:
    def __init__(self, host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password=''):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = self.connect()

    def connect(self):
        try:
            return mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except mysql.connector.Error as err:
            raise JDBCConnectionError(str(err))

    def user_create(self, user_name, user_pass, chatgpt_api_key):
        mysql_con = self.connection
        mysql_cursor = None
        checkUserQuery = f"""
            SELECT COUNT(*) AS count FROM WhichIsBetter_Dev.Users WHERE USER_NAME = '{user_name}';
                """
        userCreateQuery = f"""
                INSERT INTO WhichIsBetter_Dev.Users (USER_NAME, USER_PASS, CHATGPT_API_KEY) 
                VALUES ('{user_name}','{user_pass}',hex(aes_encrypt('{chatgpt_api_key}', 'a')));
                """
        try:
            mysql_cursor = mysql_con.cursor(dictionary=True)
            mysql_cursor.execute(checkUserQuery)
            qresult = mysql_cursor.fetchone()
            
            if qresult["count"] > 0:
                return "User Already Exists"
            else:
                mysql_cursor.execute(userCreateQuery)
                mysql_con.commit()
                if mysql_cursor.rowcount > 0:
                    return "User Was Successfully Created."
                else:
                    return "No User was Created."
        except JDBCConnectionError as err:
            raise JDBCConnectionError(str(err))
        finally:
            if mysql_cursor:
                mysql_cursor.close()
            if mysql_con:
                mysql_con.close()

    def get_user(self, user_name, user_pass):
        mysql_con = self.connection
        mysql_cursor = None
        getUserQuery = f"""
            SELECT CAST(AES_DECRYPT(unhex(CHATGPT_API_KEY), 'a') AS CHAR) as CHATGPT_API_KEY
            FROM WhichIsBetter_Dev.Users 
            WHERE USER_NAME = '{user_name}' AND USER_PASS = '{user_pass}'
            """

        try:
            mysql_cursor = mysql_con.cursor(dictionary=True)
            mysql_cursor.execute(getUserQuery)
            result = mysql_cursor.fetchall()

            if result:
                return result[0]['CHATGPT_API_KEY']
            else:
                return "Invalid User or Password"
        except JDBCConnectionError as err:
            raise JDBCConnectionError(str(err))
        finally:
            if mysql_cursor:
                mysql_cursor.close()
            if mysql_con:
                mysql_con.close()




