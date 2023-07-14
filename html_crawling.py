# import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

# define function to get data from a soup with pre-defined header
def get_data(soup, header):
    # get row by row data
    data = []
    for i in soup.find_all("tr", {"class":"ant-table-row ant-table-row-level-0"}):
        row = []
        for j in i.find_all("td", {"class":"ant-table-cell ant-table-cell-ellipsis"}):
            row.append(j.get("title"))
        data.append(row)

    # create dataframe with tuple
    df = pd.DataFrame(tuple(data), columns=header)

    # return the dataframe
    return df

# define service
service = Service(executable_path="path-to-your-chrome-driver")

# open chrome
driver = webdriver.Chrome(service=service)

# get http://example.com/user/login
driver.get('http://example.com/user/login')

# send username and password
login = driver.find_element("xpath", "//input").send_keys('username')
password = driver.find_element("xpath", "//*[@id='formLogin']/div[2]/div[2]/div/div/span/input").send_keys('password')

# click login botton
submit = driver.find_element("xpath", "//*[@id='formLogin']/div[5]/div/div/div/div/button").click()

# navigate to customer page
driver.get('http://example.com/user/customer')

# wait for 10s to ensure all data was loaded
time.sleep(10)

# get html source
html=driver.page_source

# parser with BeautifulSoup
soup=BeautifulSoup(html,'html.parser')

# get header for dataframe
header = []
for i in soup.find_all("th", {"class":"ant-table-cell ant-table-cell-ellipsis"}):
    header.append(i.get("title"))

# get data of the first page
df = get_data(soup=soup, header=header)

# get all data from 729 remaining pages
for k in range(729):
    # click next page botton
    submit = driver.find_element("xpath", "//*[@id='basic-layout--content']/div[4]/div[2]/div/div/div/ul/li[10]").click()
    
    # wait for 10s to ensure all data was loaded
    time.sleep(10)

    # get html source
    html=driver.page_source

    # parser with BeautifulSoup
    soup=BeautifulSoup(html,'html.parser')
    
    # get data of the current page
    temp = get_data(soup=soup, header=header)

    # append data to the main dataframe
    df = pd.concat([df, temp], ignore_index=True)

# write dataframe to csv
df.to_csv("customer.csv", index=False)