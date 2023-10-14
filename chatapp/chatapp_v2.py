# from flask import Flask, request, json, jsonify
# import requests

# app = Flask(__name__)

# @app.route("/chatApp/ask", methods = ['POST'])
# def chatApp_ask():
#     try:
#         params = request.get_json()
#         print("Got Jason Data", params)
#         userName = params["user_name"]
#         userPass = params["user_pass"]
#         question = params["question"]
#         print("Got Jason Data", question)
        
#         response_content = chatgpt_api_request(userName, userPass, question)
#         return jsonify({"result": response_content})
#     except KeyError:
#         return jsonify({"error": "Invalid JSON input"}), 400
#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# def chatgpt_api_request(userName, userPass, question):
#     API_URL = "https://api.openai.com/v1/chat/completions"
#     ## API KEY FETCH
#     try:
#         API_KEY = getUser_query_executor(userName, userPass)
#         if API_KEY == "Invalid Credential":
#             raise KeyError
        
#     except ValueError as ve:
#         raise ValueError(f"Error in fetching API Key: {str(ve)}")
#     ## REQUEST TO CHAT GPT
#     try:
#         headers = {
#             "Authorization": f"Bearer {API_KEY}",
#             "Content-Type": "application/json"
#         }
        
#         data = {
#             "model": "gpt-4",
#             "messages": [{"role": "user", "content": f"{question}"}],
#             "temperature": 0.7
#         }
    
#         response = requests.post(API_URL, headers=headers, json=data)
#         response.raise_for_status()  # Raise an exception if the request returned an HTTP error
#         response_json = response.json()
#         return response_json['choices'][0]['message']['content']
#     except requests.RequestException as e:
#         raise ValueError(f"Error in making request to GPT-4 API: {str(e)}")
#     except KeyError:
#         raise ValueError("Unexpected response structure from GPT-4 API")

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
# # @app.route("/chatApp/user/update", methods = ['UPDATE'])
# # @app.route("/chatApp/user/delete", methods = ['DELETE'])



# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8080)