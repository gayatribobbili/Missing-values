# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:12:19 2022

@author: gayatri
"""

import pandas as pd #to work with dataframe
import numpy as np #to work with numerical 
#importing data into spyder
data_csv=pd.read_csv("C:\\Users\\91939\\OneDrive\\Desktop\\spyder\\Toyota.csv")
print(data_csv)

#to remove the unnamed column
data_csv=pd.read_csv("C:\\Users\\91939\\OneDrive\\Desktop\\spyder\\Toyota.csv",index_col=0)
print(data_csv)

#to convert the junk values into nan values
data_csv=pd.read_csv("C:\\Users\\91939\\OneDrive\\Desktop\\spyder\\Toyota.csv",index_col=0,na_values=["??","###","????"])
print(data_csv)

#to copy the data into otherfile such that watever changes  are made into copy obejct
#deepcopy is used as whtaever changes are made are not reflected into original object
#shallow copy the data manupilated will refleect into original object
cars_data=data_csv.copy(deep="True")
print(cars_data)
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])
print(cars_data.info())
                    

#dataframe atttributes
print(cars_data.dtypes)
print(cars_data.dtypes.value_counts())
print(cars_data.columns)
print(cars_data.size)
print(cars_data.shape)
print(cars_data.memory_usage())
print(cars_data.ndim)
print(cars_data.head(15))
print(cars_data.tail(10))

#ACCESING THE DATA
print(cars_data.at[100,"KM"])
print(cars_data.at[1319,"MetColor"])
print(cars_data.iat[1400,9])
print(cars_data.iat[200,5])
print(cars_data.loc[1150:1245,"FuelType"])
print(cars_data.info())

#TO FIND UNIQUE ELEMENTS OF A COLUMN
print(np.unique(cars_data["KM"])) #KM IS READ AS OBJECT INSTEAD OF INTEGER SINCE IT HAS SOME SPECIAL CHRACTERS
print(np.unique(cars_data["HP"])) #HP IS READ AS OBJECT INSTEAD OF INTEGER SINCE IT HAS SOME SPECIAL  CHARACTERSLIKE "??","###"
print(np.unique(cars_data["Doors"])) #DOORS IS READ AS OBJECT INSTAED OF INT BEACUSE OF FIVE, FOUR, THREE AS STRINGS 
print(np.unique(cars_data["MetColor"])) 
print(np.unique(cars_data["Automatic"]))

#CONVERTING VARIABLES DATA TYPES USING "ASTYPE()
#cars_data["Automatic"]=cars_data["Automatic"].astype("object")
 
#cleaning column doors
cars_data["Doors"].replace("three",3,inplace=True)
cars_data["Doors"].replace("four",4,inplace=True)
cars_data["Doors"].replace("five",5,inplace=True)
cars_data["Doors"]=cars_data["Doors"].astype("int64")

#to get total bytes consumed by the element of column
print(cars_data["FuelType"].nbytes)
print(cars_data.info())
 
print(cars_data.isnull().sum())

#subsetting the rows that have onr or more missing values
missing = cars_data[cars_data.isnull().any(axis=1)]
print(missing)

#missing values can be filled in 2 ways 
#in case of numerical values fill it by mean/median (km,age)
#in case of categorical variables fill the missing values with 
#the class which has maximum count
#describe method gives us the description whether mean/median to be used
print(cars_data.describe()) 
 
#from the above data we got mean = 55.67 and median = 60 so we will go with mean
print(cars_data["Age"].mean())

#fillna() is used to fill the missing values for age
cars_data['Age'].fillna(cars_data["Age"].mean(),inplace=True)

#For KM 
print(cars_data["KM"].describe())
#we got mean=68647.23 whereas median= 63634.0 so we will go with median
cars_data["KM"].fillna(cars_data["KM"].median(),inplace=True)

#For HP 
print(cars_data["HP"].describe())
#we got mean=101.47 whereas median=110 so, we will go with mean
cars_data["HP"].fillna(cars_data["HP"].mean(),inplace=True)
print(cars_data.isnull().sum())

#for MetColor 
print(cars_data["MetColor"].describe())

#as mean is 0 so we will go as categorical variable
#series.value_counts() gives the most frequent occuring element
print(cars_data["MetColor"].value_counts())
print(cars_data["MetColor"].value_counts().index[0])
cars_data["MetColor"].fillna(cars_data["MetColor"].index[0],inplace=True)

#for FuelType
print(cars_data["FuelType"].value_counts())
print(cars_data["FuelType"].value_counts().index[0])
cars_data["FuelType"].fillna(cars_data["FuelType"].index[0],inplace=True)
print(cars_data.isnull().sum())
