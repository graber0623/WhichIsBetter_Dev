import mysql.connector

class UserDatabase:
    def __init__(self, host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password=''):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def _connect(self):
        try:
            return mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except mysql.connector.Error as err:
            raise Exception(f"Database Connection Error: {err}")

    def user_create(self, user_name, user_pass, chatgpt_api_key):
        mysql_con = None
        mysql_cursor = None
        userCreateQuery = f"""
                INSERT INTO WhichIsBetter_Dev.Users (USER_NAME, USER_PASS, CHATGPT_API_KEY) 
                VALUES ('{user_name}','{user_pass}',hex(aes_encrypt('{chatgpt_api_key}', 'a')));
                 """
        try:
            mysql_con = self._connect()
            mysql_cursor = mysql_con.cursor(dictionary=True)
            mysql_cursor.execute(userCreateQuery)
            mysql_con.commit()

            if mysql_cursor.rowcount > 0:
                return "User was successfully Created."
            else:
                return "No user was Created."
        except Exception as err:
            return str(err)
        finally:
            if mysql_cursor:
                mysql_cursor.close()
            if mysql_con:
                mysql_con.close()

    def get_user(self, user_name, user_pass):
        mysql_con = None
        mysql_cursor = None
        getUserQuery = f"""
            SELECT CAST(AES_DECRYPT(unhex(CHATGPT_API_KEY), 'a') AS CHAR) as CHATGPT_API_KEY
            FROM WhichIsBetter_Dev.Users 
            WHERE USER_NAME = '{user_name}' AND USER_PASS = '{user_pass}'
            """

        try:
            mysql_con = self._connect()
            mysql_cursor = mysql_con.cursor(dictionary=True)
            mysql_cursor.execute(getUserQuery)
            result = mysql_cursor.fetchall()

            if result:
                return result[0]['CHATGPT_API_KEY']
            else:
                return "Invalid User or Password"
        except Exception as err:
            return str(err)
        finally:
            if mysql_cursor:
                mysql_cursor.close()
            if mysql_con:
                mysql_con.close()





# import mysql.connector

# def userCreate_query_executor(user_name, user_pass, chatgpt_api_key):
#     mysql_con = None
#     userCreateQuery = f"""
#             INSERT INTO WhichIsBetter_Dev.Users (USER_NAME, USER_PASS, CHATGPT_API_KEY) 
#             VALUES ('{user_name}','{user_pass}',hex(aes_encrypt('{chatgpt_api_key}', 'a')));
#              """
#     try:
#         mysql_con = mysql.connector.connect(host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password='')                   
#         mysql_cursor = mysql_con.cursor(dictionary=True)
#         mysql_cursor.execute(userCreateQuery)
#         mysql_con.commit()  

#         if mysql_cursor.rowcount > 0:
#             return "User was successfully inserted."
#         else:
#             return "No user was inserted."
#     except mysql.connector.Error as err:
#         return f"Error: {err}"
#     finally:
#         if mysql_cursor:
#             mysql_cursor.close()
#         if mysql_con:
#             mysql_con.close()
            
# def getUser_query_executor(user_name, user_pass):
#     mysql_con = None
#     getUserQuery = f"""
#         SELECT CAST(AES_DECRYPT(unhex(CHATGPT_API_KEY), 'a') AS CHAR) as CHATGPT_API_KEY
#         FROM WhichIsBetter_Dev.Users 
#         WHERE USER_NAME = '{user_name}' AND USER_PASS = '{user_pass}'
#         """
    
#     try:
#         mysql_con = mysql.connector.connect(host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password='')
#         mysql_cursor = mysql_con.cursor(dictionary=True)
#         mysql_cursor.execute(getUserQuery)
#         result = mysql_cursor.fetchall()

#         if result:
#             return result[0]['CHATGPT_API_KEY']
#         else:
#             return "Invalid Credential"
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None
    
#     finally:
#         if mysql_cursor:
#             mysql_cursor.close()
#         if mysql_con:
#             mysql_con.close()