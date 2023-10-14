# from flask import Flask, request, json, jsonify

# app = Flask(__name__)

# @app.route("/chatApp/ask", methods = ['POST'])
# def chatApp_ask():
#     params = request.get_json()
#     print("Got Jason Data", params["question"])
#     q = params["question"]
    
#     response = {
#         "result": f"{chatgpt_api_request(q)}",
#     }
#     return jsonify(response)

# def chatgpt_api_request(question): ## MAKING REQUEST TO CHATGPT
#     import requests
#     import json
#     API_URL = "https://api.openai.com/v1/chat/completions"
#     API_KEY = 'sk-'

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "model": "gpt-4",
#         "messages": [{"role": "user", "content": f"{question}"}],
#         "temperature": 0.7
#     }

#     response = requests.post(API_URL, headers=headers, data=json.dumps(data))
#     response_json = response.json()
#     return response_json['choices'][0]['message']['content']
# ####
# @app.route("/chatApp/user/create", methods = ['PUT'])
# def chatApp_createUser():
#     params = request.get_json()
#     print("Got Jason Data", params)
#     userName = params["user_name"]
#     userPass = params["user_pass"]
#     apiKey = params["chatgpt_api_key"] 
    
#     response = {
#         "result": f"{userCreate_query_executor(userName, userPass, apiKey)}",
#     }
#     return jsonify(response)

# def userCreate_query_executor(user_name, user_pass, chatgpt_api_key):
#     import mysql.connector
#     mysql_con = None
#     userCreateQuery = f"""
#             INSERT INTO WhichIsBetter_Dev.Users (USER_NAME, USER_PASS, CHATGPT_API_KEY) 
#             VALUES ('{user_name}','{user_pass}','{chatgpt_api_key}');
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
# #######
# @app.route("/chatApp/user/get", methods = ['GET'])
# def chatApp_getUser():
#     params = request.get_json()
#     print("Got Jason Data", params)
#     userName = params["user_name"]
#     userPass = params["user_pass"]
    
#     response = {
#         "result": f"{getUser_query_executor(userName, userPass)}",
#     }
#     return jsonify(response)

# def getUser_query_executor(user_name, user_pass):
#     import mysql.connector
#     mysql_con = None
#     getUserQuery = f"""
#         SELECT CHATGPT_API_KEY 
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
#             return "Wrong User or Password"
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None
    
#     finally:
#         if mysql_cursor:
#             mysql_cursor.close()
#         if mysql_con:
#             mysql_con.close()
# # @app.route("/chatApp/user/update", methods = ['UPDATE'])
# # @app.route("/chatApp/user/delete", methods = ['DELETE'])


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8080)