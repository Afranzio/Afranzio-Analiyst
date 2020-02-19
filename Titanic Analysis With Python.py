#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
data=[1,2,3,4,5]
ser1=pd.Series(data)
ser1


# In[6]:


type(ser1)


# In[7]:


ser1=pd.Series(data, index=['a','b','c','d','e'])


# In[8]:


ser1


# In[9]:


#How TO Datafram


# In[15]:


import pandas as pd
data=[1,2,3,4]
df=pd.DataFrame(data)
df


# In[16]:


type(df)


# In[18]:


dictionary={'Name':['Mani','Jhon','Arun'],'Age':[10,12,24]}
df=pd.DataFrame(dictionary)
df


# In[25]:


#Merge and Concodination


# In[78]:


import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
df=pd.read_csv(r"C:\Users\Mani\Downloads\titanic.csv")
df


# In[79]:


df.info()


# In[80]:


df.describe()


# In[81]:


sns.countplot(x="survived",hue="sex",data=df);


# In[82]:


df["age"].plot.hist();


# In[83]:


df.drop(columns="name",inplace=True)


# In[84]:


df.drop(columns="cabin",inplace=True)


# In[85]:


df


# In[86]:


sns.countplot(x="survived",hue="pclass",data=df);


# In[87]:


df["fare"].plot.hist();


# In[88]:


df["sibsp"].plot.hist();


# In[89]:


df["parch"].plot.hist();


# In[90]:


sns.boxplot(x="pclass",y="age",data=df);


# In[91]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False);


# In[92]:


print("#Pessanger in the train::" +str(len(df.index.isnull())))


# In[93]:


sns.boxenplot(x="embarked",y="body",hue="sex",data=df);


# In[94]:


sns.stripplot(x="embarked", y="body", data=df,size=4, color="gray");


# In[96]:


sns.catplot(x="age", y="body", data=df,size=4, color="gray");


# In[102]:


plot.bar(x="parch",height="age",data=df);




