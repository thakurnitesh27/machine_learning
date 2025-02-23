import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from sklearn.impute import SimpleImputer

data_set_new:DataFrame=pd.read_csv("https://raw.githubusercontent.com/thakurnitesh27/machine_learning/refs/heads/main/pima-indians-diabetes.csv")

X1:DataFrame= data_set_new.iloc[:,:-1]
Y1:Series=data_set_new.iloc[:,-1]
#print("Independent variable :\n",DataFrame(X1))
#print(f"Dependent variable:\n{Series(Y1)}")

#X2=X1[X1[0]]

#for i in range(0,len(data_set_new.columns)-1):
 #print(X1[ ~ (X1.iloc[:, i])].iloc[:,i])

print(X1[X1.iloc[:,0]!=0])
imputer=SimpleImputer(missing_values=0,strategy="mean")
X2=imputer.fit_transform(X1)

print(X1)
data_set_final=pd.DataFrame(X2, columns=X1.columns)

print(data_set_final)

data_set_final.to_csv("~/Downloads/output.csv",index=False)




