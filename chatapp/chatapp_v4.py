from flask import Flask, request, json, jsonify
import requests
import sys
sys.path.append("/Users/sanglokkim/dev_env/WhichIsBetter_Dev")

from JDBCConnector.jdbcConnector import UserDatabase
from Questioners.ChatGptConnector import ChatGPTQuestioner

app = Flask(__name__)

@app.route("/chatApp/ask", methods = ['POST'])
def chatApp_ask():
    try:
        params = request.get_json()
        userName = params["user_name"]
        userPass = params["user_pass"]
        question = params["question"]
        app.logger.info(f"Got JSON Data: {params}")
        
        requester = ChatGPTQuestioner(userName, userPass)
        response = requester.make_request(question)
        
        app.logger.info(f"Answer: {response}")
        
        return jsonify({"result": response})
    except KeyError:
        app.logger.error("Invalid JSON input")
        return jsonify({"error": "Invalid JSON input"}), 400
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