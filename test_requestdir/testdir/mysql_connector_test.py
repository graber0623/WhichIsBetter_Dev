
def userCreate_query_executor(user_name, user_pass, chatgpt_api_key):
    import mysql.connector
    mysql_con = None
    userCreateQuery = f"""
            INSERT INTO WhichIsBetter_Dev.Users (USER_NAME, USER_PASS, CHATGPT_API_KEY) 
            VALUES ('{user_name}','{user_pass}','{chatgpt_api_key}');
             """
    try:
        mysql_con = mysql.connector.connect(host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password='')                   
        mysql_cursor = mysql_con.cursor(dictionary=True)
        mysql_cursor.execute(userCreateQuery)
        mysql_con.commit()  

        if mysql_cursor.rowcount > 0:
            return "User was successfully inserted."
        else:
            return "No user was inserted."
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_con:
            mysql_con.close()
#######

def getUser_query_executor(user_name, user_pass):
    import mysql.connector
    mysql_con = None
    getUserQuery = f"""
        SELECT CHATGPT_API_KEY 
        FROM WhichIsBetter_Dev.Users 
        WHERE USER_NAME = '{user_name}' AND USER_PASS = '{user_pass}'
        """
    
    try:
        mysql_con = mysql.connector.connect(host='localhost', port='3306', database='WhichIsBetter_Dev', user='root', password='')
        mysql_cursor = mysql_con.cursor(dictionary=True)
        mysql_cursor.execute(getUserQuery)
        result = mysql_cursor.fetchall()

        if result:
            return result[0]['CHATGPT_API_KEY']
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_con:
            mysql_con.close()
        
# print(userCreate_query_executor("sanglok", "111", "se-dd22"))
print(getUser_query_executor("sanglok", "111"))