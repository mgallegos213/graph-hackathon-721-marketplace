import json, os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# All of our data lives in the transactionSalesDataUpdatedBlockNumbers<1-166>.json files
# This includes all of the ERC-721 NFT transaction data for OpenSea, LooksRare, and X2Y2
# PROBLEM: OpenSea moved to the SeaPort contract recently and this subgraph is not yet updated

# Now that we have this information queried from the Subgraph:
# https://thegraph.com/explorer/subgraphs/B333F7Ra4kuVBSwHFDfH9x9N1341GYHvdfpV94KY8Gmv

# We can now visualize the information and perform an NFT analysis across marketplaces

# List of studies:
# REACH - How many users (buying/selling) on each marketplace
# + Transaction Count
# + Buyer vs Sellers (unique buyers vs unique sellers)
# REVENUE - Sales analysis
# + Sales volume and growth rate
# + Fee Revenue and Growth %
# COLLECTION ACTIVITY
# + Sales volume by NFT collection
# + Wash trading by NFT collection

# First let's parse the queried stored data into a data frame
# create an empty list to store cleaned data
cleaned_data = []

# loop through each file in the directory
for filename in os.listdir('data/'):
    if filename.endswith('.json'):
        # open the JSON file
        with open(os.path.join('data/', filename), 'r') as f:
            json_data = json.load(f)
        
        # loop through each item in the JSON file
        for item_key in json_data.keys():
            item = json_data[item_key]
            
            # extract the relevant data from the nested structure
            transaction_id = item['sales']['transaction']['id']
            sender_address = item['sales']['transaction']['transfers'][0]['senderAddress']['id']
            receiver_address = item['sales']['transaction']['transfers'][0]['receiverAddress']['id']
            collection_symbol = item['sales']['transaction']['transfers'][0]['token']['collection']['symbol']
            platform = item['sales']['platform']
            currency_symbol = item['sales']['currency']['symbol']
            amount = item['sales']['amount']
            timestamp = item['sales']['timestamp']
            
            date = datetime.fromtimestamp(timestamp).date()
            
            # create a dictionary with the extracted data and append it to the cleaned data list
            cleaned_data.append({
                'transactionID': transaction_id,
                'senderAddress': sender_address,
                'receiverAddress': receiver_address,
                'collection': collection_symbol,
                'platform': platform,
                'currency symbol': currency_symbol,
                'amount': amount,
                'timestamp': timestamp,
                'date': date
            })

# Now do the same with the OpenSea Seaport contract data
for filename in os.listdir('openSeaData/'):
    if filename.endswith('.json'):
        # open the JSON file
        with open(os.path.join('openSeaData/', filename), 'r') as f:
            json_data = json.load(f)
        
        # loop through each item in the JSON file
        for item_key in json_data.keys():
            item = json_data[item_key]
            
            # extract the relevant data from the nested structure
            transaction_id = item['trades']['transactionHash']
            sender_address = item['trades']['seller']
            receiver_address = item['trades']['buyer']
            collection_symbol = item['trades']['collection']['name']
            platform = 'OpenSea'
            currency_symbol = 'ETH'
            amount = item['trades']['priceETH']
            timestamp = int(item['trades']['timestamp'])
            
            date = datetime.fromtimestamp(timestamp).date()
            
            # create a dictionary with the extracted data and append it to the cleaned data list
            cleaned_data.append({
                'transactionID': transaction_id,
                'senderAddress': sender_address,
                'receiverAddress': receiver_address,
                'collection': collection_symbol,
                'platform': platform,
                'currency symbol': currency_symbol,
                'amount': amount,
                'timestamp': timestamp,
                'date': date
            })

# create a DataFrame from the cleaned data list
df = pd.DataFrame(cleaned_data)

df.to_csv('output.csv', index=False)