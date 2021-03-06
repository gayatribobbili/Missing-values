# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 18:12:19 2022

@author: gayatri
"""

import pandas as pd               #to work with dataframe
import numpy as np                #to work with numericals
import seaborn as sns             #to do visualization
import matplotlib.pyplot as plt   #to do visualization

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
print(np.unique(cars_data["Price"]))
print(np.unique(cars_data["Age"]))
print(np.unique(cars_data["KM"])) #KM IS READ AS OBJECT INSTEAD OF INTEGER SINCE IT HAS SOME SPECIAL CHRACTERS
print(np.unique(cars_data["HP"])) #HP IS READ AS OBJECT INSTEAD OF INTEGER SINCE IT HAS SOME SPECIAL  CHARACTERSLIKE "??","###"
print(np.unique(cars_data["CC"]))
print(np.unique(cars_data["Doors"])) #DOORS IS READ AS OBJECT INSTAED OF INT BEACUSE OF FIVE, FOUR, THREE AS STRINGS 
print(np.unique(cars_data["MetColor"])) 
print(np.unique(cars_data["Automatic"]))
print(np.unique(cars_data["Weight"]))

#CONVERTING VARIABLES DATA TYPES USING "ASTYPE()
cars_data["Automatic"]=cars_data["Automatic"].astype("object")
 
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
#print(cars_data.isnull().sum())

#for MetColor 
print(cars_data["MetColor"].describe())

#as mean is 0 so we will go as categorical variable
print(cars_data["MetColor"].value_counts())
print(cars_data["MetColor"].value_counts().index[0])
cars_data["MetColor"].fillna(cars_data["MetColor"].value_counts().index[0],inplace=True)

#for FuelType
print(cars_data["FuelType"].value_counts())
print(cars_data["FuelType"].value_counts().index[0])
cars_data["FuelType"].fillna(cars_data["FuelType"].value_counts().index[0],inplace=True)
print(cars_data.isnull().sum())
print(cars_data)
cars_data1=cars_data.copy(deep=True)


#Exploratory Data Analysis
#correlation 
#Exclude the columns having datatype as object
correlation=cars_data1.select_dtypes(exclude=[object])
corr_matrix=correlation.corr()

#crosstab
print(pd.crosstab(index=cars_data1["KM"], columns=cars_data1["FuelType"],dropna=True))
print(pd.crosstab(index=cars_data1["Automatic"], columns=cars_data1["FuelType"],dropna=True))
print(pd.crosstab(index=cars_data1["KM"], columns=cars_data1["HP"],dropna=True))
print(pd.crosstab(index=cars_data1["Age"], columns=cars_data1["FuelType"],dropna=True))
print(pd.crosstab(index=cars_data1["Price"], columns=cars_data1["MetColor"],dropna=True))

#Joint Probability
print(pd.crosstab(index=cars_data1["KM"], columns=cars_data1["FuelType"],normalize=True,dropna=True))
print(pd.crosstab(index=cars_data1["Automatic"], columns=cars_data1["FuelType"],normalize=True,dropna=True))
print(pd.crosstab(index=cars_data1["Age"], columns=cars_data1["FuelType"],normalize=True,dropna=True))

#Marginal Probability
print(pd.crosstab(index=cars_data1["FuelType"], columns=cars_data1["KM"],margins=True,normalize=True,dropna=True))
print(pd.crosstab(index=cars_data1["Automatic"], columns=cars_data1["FuelType"],margins=True,normalize=True,dropna=True))

#Seaborn library 
sns.pairplot(cars_data1)
sns.scatterplot(cars_data1["Age"], cars_data1["Price"])#FROM THE GRAPH THE PRICE OF THE CAR DECREASES AS AGE INCREASES
sns.scatterplot(cars_data1["FuelType"], cars_data1["KM"])
sns.scatterplot(cars_data1["KM"],cars_data1["Price"],marker="*")#price increses KM increases

sns.regplot(x="Age",y="Price",data=cars_data1,fit_reg=True)
sns.lmplot(x="KM",y="Price",data=cars_data1,hue="FuelType",fit_reg=False,legend="True",palette="Set1")
sns.lmplot(x="Age",y="Price",data=cars_data1,hue="FuelType",fit_reg=False,legend="True",palette="Set1",scatter=True)

#Histogram
sns.displot(cars_data1["Price"])
sns.histplot(cars_data1["Price"],bins=10)
sns.displot(cars_data1["Age"],kde=False,bins=5)
sns.displot(cars_data1["MetColor"],kde=False,bins=5)
sns.distplot(cars_data1["KM"],kde=False,bin=5)


#BarPlot
sns.countplot(x="FuelType",data=cars_data1)
sns.countplot(x="Automatic",data=cars_data1)
sns.boxplot(y=cars_data1["Age"])
sns.boxplot(x=cars_data1["Automatic"])
sns.boxplot(x=cars_data1["FuelType"],y=cars_data1["Price"],hue="Automatic",data=cars_data1)


#using Matplot libarary
plt.scatter(cars_data1["Age"],cars_data1["Price"],c='red')
plt.title("scatter plot of price vs age")
plt.xlabel('Age')
plt.ylabel('price')
plt.show()

plt.scatter(cars_data1["KM"],cars_data["Price"],c="green")
plt.title("scatter plot of fueltype vs price")
plt.xlabel('KM')
plt.ylabel('price')
plt.show()

#Histogram
plt.hist(cars_data1["KM"])
plt.hist(cars_data1["KM"],color="green",bins=5)
plt.title("Histogram of Kilometer")
plt.xlabel('Kilometer')
plt.ylabel('frequency')
plt.show()


#Bar plot
counts=[978,120,12]
FuelType=('Petrol','Diesel','CNG')
index=np.arange(len(FuelType))
plt.bar(index,counts,color=["red","blue","cyan"])
plt.title('Bar plots of fuel types')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.xticks(index,FuelType,rotation=90)
plt.show()



