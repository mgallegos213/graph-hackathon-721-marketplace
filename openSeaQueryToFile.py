import requests
import json
import pandas as pd

# Do steps of 300 blocks, first 100 per that 300 as per the Graph's query limit
# Should show us most of the NFT data for the past week or so.
fileCounter = 0;
for i in range(16708664, 16658664, -300):
    salesPerThousandBlocksQuery = f"""
    {{
        trades(first: 100, where: {{ blockNumber_lte: {i}, blockNumber_gte: {i-300} }}) {{
            amount
            blockNumber
            buyer
            seller
            timestamp
            tokenId
            transactionHash
            priceETH
            collection {{
                name
            }}
        }}
    }}
    """
    # print("query: " + salesPerThousandBlocksQuery)

    urlGateway = 'https://gateway.thegraph.com/api/'
    apiKey = 'MYKEY' # REPLACE THIS WITH YOUR OWN API KEY
    urlRoute = '/subgraphs/id/G1F2huam7aLSd2JYjxnofXmqkQjT5K2fRjdfapwiik9c'
    url = urlGateway + apiKey + urlRoute
    r = requests.post(url, json={'query': salesPerThousandBlocksQuery})
    print(r.status_code)
    print(r.text)

    json_data = json.loads(r.text)
    df_data = json_data['data']
    df = pd.DataFrame(df_data)
    df.to_json(r'./openSeaData/transactions' + str(fileCounter) + '.json', orient='index', indent=2)
    fileCounter += 1