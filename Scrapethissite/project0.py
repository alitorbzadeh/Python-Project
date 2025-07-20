import numpy as np
from bs4 import BeautifulSoup
import mysql.connector as sql
import requests as req
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import os  

# Change the paths below to exactly where your Python installation is located  
os.environ['TCL_LIBRARY'] = r'C:\Users\Ali\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'  
os.environ['TK_LIBRARY'] = r'C:\Users\Ali\AppData\Local\Programs\Python\Python313\tcl\tk8.6'  
import matplotlib.pyplot as plt

#Connect to Sql Server
server=sql.connect(
    host="127.0.0.1",
    database='pythontest',
    user="root",
    password="9112330013",
    port=3306,
    autocommit=True
)

# Web Scraping and Data Entry
sql_rule_CreateTable="CREATE TABLE IF NOT EXISTS dataset(name varchar(255), population varchar(255), area varchar(255))"
with server.cursor() as SQL:
    SQL.execute(operation=sql_rule_CreateTable)
    data=req.get(url="https://www.scrapethissite.com/pages/simple/")
    soup=BeautifulSoup(data.text, "html.parser")
    Country_names=soup.find_all(name="h3", attrs={"class":"country-name"})
    Populations=soup.find_all(name="span", attrs={"class":"country-population"})
    Areas=soup.find_all(name="span",attrs={"class":"country-area"})
    length=len(Country_names)
    for i in range(length):
        Country=Country_names[i]
        Country=Country.text
        Country=Country.strip()
        Population=Populations[i]
        Population=Population.text
        Population=Population.strip()
        Area=Areas[i]
        Area=Area.text
        Area=Area.strip()
        sql_rule_DataEntry="INSERT INTO dataset(name, population, area) VALUES(%s, %s, %s)"
        values=(Country,Population,Area)
        SQL.execute(sql_rule_DataEntry,values)
    SQL.close()


# Machine Learning
sql_rule_ForQuery="SELECT * FROM pythontest.dataset"
with server.cursor() as SQL:
    SQL.execute(operation=sql_rule_ForQuery)
    Query_result=SQL.fetchall()
    Dataset=np.zeros(shape=(len(Query_result),3))
    Dataset=Dataset.astype(str)
    i=0
    for item in Query_result:
        Dataset[i,0]=item[0]
        Dataset[i,1]=item[1]
        Dataset[i,2]=item[2]
        i+=1
    SQL.close()


X=np.zeros(shape=(len(Dataset),1))
Y=np.zeros(shape=(len(Dataset),))
X=Dataset[:,1]
Y=Dataset[:,2]

X_Train, X_Test, Y_Train, Y_Test=train_test_split(X,Y,test_size=0.2,random_state=4)
X_Train=np.reshape(X_Train,shape=(len(X_Train),1))
X_Test=np.reshape(X_Test,shape=(len(X_Test),1))
Regressor0=DecisionTreeRegressor(max_depth=5)
Regressor1=DecisionTreeRegressor(max_depth=10)
Regressor2=DecisionTreeRegressor(max_depth=12)
Regressor0.fit(X_Train,Y_Train)
Regressor1.fit(X_Train,Y_Train)
Regressor2.fit(X_Train,Y_Train)
Y_Predicted_0=Regressor0.predict(X_Test)
Y_Predicted_1=Regressor1.predict(X_Test)
Y_Predicted_2=Regressor2.predict(X_Test)


plt.figure()
X_Train=X_Train.astype(float).flatten()
Y_Train=Y_Train.astype(float).flatten() 
X_Test=X_Test.astype(float).flatten() 
Y_Test=Y_Test.astype(float).flatten() 
Y_Predicted_0=Y_Predicted_0.astype(float).flatten() 
Y_Predicted_1=Y_Predicted_1.astype(float).flatten() 
Y_Predicted_2=Y_Predicted_2.astype(float).flatten() 
plt.scatter(X_Train, Y_Train, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_Test, Y_Predicted_0, color="blue", label="max_depth=5", linewidth=2)
plt.plot(X_Test, Y_Predicted_1, color="green", label="max_depth=10", linewidth=2)
plt.plot(X_Test, Y_Predicted_2, color="yellow", label="max_depth=12", linewidth=2)
plt.plot(X_Test, Y_Test, color="red", label="Validation", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()







