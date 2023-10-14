import os
import sys
import jaydebeapi as jp
import jpype
jar_path = "/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home/jre/lib/mysql-connector-j-8.1.0.jar"
jdbc_url = "jdbc:mysql://localhost:3306/WhichIsBetter_Dev"
driver_class = "com.mysql.jdbc.Driver"
username = "root"
password = ""
args = '-Djava.class.path=%s' % jar_path
if not jpype.isJVMStarted():
    jpype.startJVM(jpype.getDefaultJVMPath(), args)



conn = jp.connect(driver_class, jdbc_url, [username, password], jar_path)
curs = conn.cursor()

curs.execute("""
             CREATE TABLE WhichIsBetter_Dev.test_table (
                 id INT Null,
                 name VARCHAR(255) NULL,
             )
             """)

curs.close()
conn.close()

