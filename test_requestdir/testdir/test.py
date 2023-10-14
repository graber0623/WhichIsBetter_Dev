import sys
sys.path.append("/Users/sanglokkim/dev_env/WhichIsBetter_Dev")

from JDBCConnector.jdbcConnector import UserDatabase
from Questioners.ChatGptConnector import ChatGPTQuestioner

requester = ChatGPTQuestioner("graber1991", "123456")
response = requester.make_request("how can i print hello in python")
print(response)