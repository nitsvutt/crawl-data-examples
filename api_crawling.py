# import libraries
import pandas as pd
import requests

# define url
url = "http:example.com/app/customer/load-list"

# define headers
headers = {}

# define pageInfo
json = {"pageInfo":{"currentPage":1,"pageSize":100}}

# get response from the post request
response = requests.post(url, headers=headers, json=json)

# create dataframe with header only
data = pd.DataFrame.from_dict(data={}, columns=response.json()["body"]["result"][0], orient="index")

# loop all pages to get all data
for i in range(1,80):
    # define pageInfo
    json = {"pageInfo":{"currentPage":i,"pageSize":100}}

    # get response from the post request
    response = requests.post(url, headers=headers, json=json)
    
    # transform the response to dict
    dict_list = response.json()["body"]["result"]
    
    # append data to the dataframe
    data = pd.concat([data, pd.DataFrame.from_dict(dict_list)], ignore_index=True)

# write dataframe to csv
data.to_csv("customer.csv", index=False)
