# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyqtgraph as pg
from array import *
#importing the dataset 
dataset=pd.read_csv('rain.csv') 
dataset.info()  #information about dataset column wise
dataset.describe()
dataset.dropna(how='any',inplace =True)
            
sd=dataset.SUBDIVISION.unique()
subs={}
for i in range (36):
 subs[i]=sd[i]

subs1={}
for i in range (36):
 subs1[sd[i]]=i;
                        
sub_data={}         
for i in range (36):
  sub_data[i]=pd.DataFrame(dataset.loc[ dataset['SUBDIVISION'] == subs[i]])


dictmp={}
i=0
for x in range (36):
    if(x==29 or x==27 or x==25 or x==23 or  x==18 or x==14 or x==10 or x==5 or x==0):
        continue;
    else: 
        dictmp[i]=subs[x];
        i=i+1;

dictmp1={}
for i in range (27):
    dictmp1[dictmp[i]]=i;


def pred(x):
    mptrain(sub_data[x].iloc[:,17:18],sub_data[x].iloc[:,14:15],x)
    return


def pred22(x):
    mptest(sub_data[x].iloc[:,17:18],sub_data[x].iloc[:,14:15],x)
    return


def mpred(x,val):
    
    str1 = mp1(sub_data[x].iloc[:,17:18],sub_data[x].iloc[:,14:15],val)
    return (str1)


def mp1(X,y,value):
    # Splitting the dataset into the Training set and Test set  
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 3)

    # Fitting Simple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = regressor.predict(value)
  
    str1= "Predicted annual rainfall is = " + str(y_pred[0])
    return(str1)
  
def mptrain(X,y,i):
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 3)

    # Fitting Simple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    
    # Visualising the Training set results
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title(subs[i])
    plt.xlabel('Rainy Season total rainfall in (mm)')
    plt.ylabel('Annual rainfall in (mm)')
    plt.show()
    return()
    
def mptest(X,y,i):
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 3)

    # Fitting Simple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    
    # Visualising the Test set results
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title(subs[i])
    plt.xlabel('Rainy Season total rainfall in (mm)')
    plt.ylabel('Annual rainfall in (mm)')
    plt.show()
    return()

def plotannual(num):
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    ax.title.set_fontsize(45)
    ax.xaxis.label.set_fontsize(15)
    ax.title.set_fontsize(25)
    plt.title(subs[num])
    ax.yaxis.label.set_fontsize(15)
    plt.xlabel('YEARS')
    plt.ylabel('Annual rainfall in (mm )')
    plt.plot(sub_data[num].YEAR,sub_data[num].ANNUAL,'b',sub_data[num].YEAR,sub_data[num].ANNUAL,'ro')
    plt.show()
    return()

def annual_subdivision():
    #Subdivsion vs annual rainfall
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    dataset.groupby('SUBDIVISION').mean().sort_values(by='ANNUAL',ascending=True)['ANNUAL'].plot('bar',color=['red','orange','yellow'],width=0.7,title='SUBDIVISION WISE ANNUAL RAINFALL',fontsize=10)
    plt.xticks(rotation=90) #Get or set the x-limits of the current tick locations and labels.
    plt.ylabel('Average annual rainfall in mm ')
    ax.title.set_fontsize(25)
    ax.xaxis.label.set_fontsize(15)
    ax.yaxis.label.set_fontsize(15)
    plt.show()
    return()
    
def yearly_subdivision():
    #yearly subdivision wise
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    dataset.groupby('YEAR').sum()['ANNUAL'].plot('line',fontsize=15,color='red')
    plt.xticks(rotation=90) #Get or set the x-limits of the current tick locations and labels.
    plt.ylabel('Total annual rainfall (mm) ')
    plt.title('Total Annual Rainfall of India VS Years')
    ax.title.set_fontsize(25)
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)
    plt.show()
    return()

def monthly_subdivision():
    #subdivision wise montly
    months=dataset.columns[15:19]
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    xlbls=dataset['SUBDIVISION'].unique()
    xlbls.sort()
    ark=dataset.groupby('SUBDIVISION').mean()[months]
    ark.plot.line(title='Overall rainfall in each season of year',ax=ax,fontsize=10)
    plt.xticks(np.linspace(0,35,36,endpoint=True),xlbls)
    plt.xticks(rotation=90) #Get or set the x-limits of the current tick locations and labels.
    plt.ylabel('Total rainfall in mm ')
    plt.legend(loc='upper right',fontsize='large')  
    ax.title.set_fontsize(25)
    ax.xaxis.label.set_fontsize(18)
    ax.yaxis.label.set_fontsize(20)
    plt.show()
    return()

def plotrainy(num):
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    ax.title.set_fontsize(35)            
    plt.title(subs[num])    
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)
    ax.title.set_fontsize(25)
    plt.xlabel('YEARS')
    plt.ylabel('Rainfall in rainy season (mm )')
    plt.plot(sub_data[num].YEAR,sub_data[num].JJAS,'b',sub_data[num].YEAR,sub_data[num].JJAS,'ro')
    plt.show()
    return()
    
def plotseason_wise(num):
    x=array('f',[sub_data[num].OND.mean(),sub_data[num].JJAS.mean(),sub_data[num].MAM.mean(),sub_data[num].JF.mean()])
    labels=['WINTER','RAINY','SUMMER','AUTUMN']
    plt.title(subs[num])
    plt.pie(x,labels=labels,colors=('r','b','yellow','green'))
    plt.show()
    return()

def plotseason_wise1(num):
    fig=plt.figure(figsize=(15,7))  #width, height in inches. If not provided, defaults to rc figure.figsize.
    ax=fig.add_subplot(111)
    ax.title.set_fontsize(25)    
    plt.title(subs[num])    
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)
    sub_data[num].OND.plot()
    sub_data[num].JJAS.plot()
    sub_data[num].MAM.plot()
    sub_data[num].JF.plot()
    plt.show()
    return()

def monthlysub(num):
    fig=plt.figure(figsize=(10,7))  #width, height in inches. If not provided, defaults to rc figure.figsize
    ax=fig.add_subplot(111)
    plt.title(subs[num])
    plt.ylabel('Monthly mean rainfall (mm)')
    plt.xlabel('Months')
    ax.title.set_fontsize(25)    
    ax.xaxis.label.set_fontsize(20)
    ax.yaxis.label.set_fontsize(20)    
    months=sub_data[num].iloc[:,2:14].mean()    
    months.plot('bar',color=('r','r','y','y','y','b','b','b','b','orange','orange','orange'))
    plt.show()
    return()
 
def hbar():
    dataset[['SUBDIVISION', 'JF', 'MAM','JJAS', 'OND']].groupby("SUBDIVISION").sum().plot.barh(stacked=True,figsize=(16,8));
    plt.show()
    return()      