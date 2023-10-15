from flask import Flask, request, json, jsonify
from logging import INFO
import requests
import sys
import os 
from datetime import datetime
sys.path.append("/Users/sanglokkim/dev_env/WhichIsBetter_Dev")

from JDBCConnector.jdbcConnector import UserDatabase
from JDBCConnector.jdbcConnectorError import JDBCConnectionError
from Questioners.ChatGptConnector import ChatGPTQuestioner
from FileLogger.FileLogging import InfoFileLogger

app = Flask(__name__)
log_dir = f"/Users/sanglokkim/dev_env/WhichIsBetter_Dev/Dev_Log"
log_file_name = f"WhichIsBetter_{datetime.now().strftime('%Y-%m-%d')}.log"
os.makedirs(log_dir, exist_ok = True)
with open(os.path.join(log_dir, log_file_name), "a") as l:
    l.write('')
app.logger.setLevel(INFO)
InfoFileLogger(app, filename = log_dir +"/"+ log_file_name)

@app.route("/chatApp/ask", methods = ['POST'])
def chatApp_ask():
    
    try:
        params = request.get_json()
        userName = params["user_name"]
        userPass = params["user_pass"]
        question = params["question"]
        app.logger.info(json.dumps(f"EVENT_TYPE : 'Q', USERNAME : '{userName}', QUESTION : '{question}', RESPONDER : {None} , RESPONSE : {None}"))
        
        requester = ChatGPTQuestioner(userName, userPass)
        response = requester.make_request(question)
        
        app.logger.info(json.dumps(f"EVENT_TYPE : 'R', USERNAME : '{userName}', QUESTION : '{question}', RESPONDER : 'CHATGPT' , RESPONSE : {(response)}"))
        
        return jsonify({"result": response})
    except KeyError:
        app.logger.error("Invalid JSON input")
        return jsonify({"error": "Invalid JSON input"}), 400
    except JDBCConnectionError:
        app.logger.error(f"MySQL Connection Error")
        return jsonify({"error": "MySQL Connection Error"}), 500
    except ValueError:
        app.logger.error("Invalid User or Password")
        return jsonify({"error": "Invalid User or Password"}), 401
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

####
@app.route("/chatApp/user/create", methods = ['PUT'])
def chatApp_createUser():
    params = request.get_json()
    print("Got Jason Data", params)
    userName = params["user_name"]
    userPass = params["user_pass"]
    apiKey = params["chatgpt_api_key"]
    
    userdb = UserDatabase()
    
    response = {
        "result": f"{userdb.user_create(userName, userPass, apiKey)}",
    }
    return jsonify(response)

#######
@app.route("/chatApp/user/get", methods = ['GET'])
def chatApp_getUser():
    params = request.get_json()
    print("Got Jason Data", params)
    userName = params["user_name"]
    userPass = params["user_pass"]
    
    userdb = UserDatabase()
    
    response = {
        "result": f"{userdb.get_user(userName, userPass)}",
    }
    return jsonify(response)

# @app.route("/chatApp/user/update", methods = ['UPDATE'])
# @app.route("/chatApp/user/delete", methods = ['DELETE'])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)