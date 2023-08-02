#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import numpy as np


# In[2]:


path=r'C:\Users\Abdur rahim nishad\Mastercourse\chromedriver.exe'


# In[3]:


browser=webdriver.Chrome(path)
browser.get("https://data.baltimorecity.gov/datasets/baltimore::part-1-crime-data/explore")
sleep(20)
CrimeDateTime=[]
Weapon=[]
CrimeCode=[]
Location=[]
Description=[]
Gender=[]
Age=[]
Race=[]
District=[]
for i in range(1,3001):
    CrimeDateTime.append(browser.find_element(By.XPATH, "//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[2]").text)
    Weapon.append(browser.find_element(By.XPATH, "//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[7]").text)
    CrimeCode.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[3]").text)
    Location.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[4]").text)
    Description.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[5]").text)
    Gender.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[9]").text)
    Age.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[10]").text)
    Race.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[11]").text)
    District.append(browser.find_element(By.XPATH,"//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[13]").text)
#     try:
#         date = browser.find_element(By.XPATH, "//*[@id='main-region']/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[2]").text
#         CrimeDateTime.append(date)
#     except:
#         CrimeDateTime.append(np.nan)


# In[4]:


len(Weapon)


# In[5]:


data={'CrimeDateTime':CrimeDateTime,"CrimeCode":CrimeCode,"Location":Location,"Description":Description,"Weapon":Weapon,"Victim_Gender":Gender,"Victim_Age":Age,"Victim_Race":Race,'District':District}


# In[6]:


df=pd.DataFrame(data)


# In[7]:


df


# In[8]:


df.to_csv("Crime_data.csv",index=False)


# In[9]:


df.head()


# In[ ]:




