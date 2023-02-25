import requests
import json
import pandas as pd

# transactionsPerPlatformQuery = """
# {
#     transactions {
#         sales(first: 10) {
#             platform
#             currency {
#                 name
#             }
#             transaction {
#                 id
#             }
#             timestamp
#         }
#     }
# }
# """

# Do steps of 1000 blocks, first 100 per that thousand as per the Graph's query limit
# Should hit 50 times, meaning about a week of
fileCounter = 0;
for i in range(10000000, 9950000, -1000):
    salesPerThousandBlocksQuery = f"""
    {{
        sales(first: 100, where: {{ blockNumber_lte: {i}, blockNumber_gte: {i-1000} }}) {{
            transaction {{
                id
                transfers {{
                    senderAddress {{
                        id
                    }}
                    receiverAddress {{
                        id
                    }}
                    amount
                    token {{
                        collection {{
                            symbol
                            name
                        }}
                    }}
                }}
                transactionFrom
            }}
            platform
            amount
            currency {{
                name
                symbol
            }}
            timestamp
            blockNumber
        }}
    }}
    """
    # print("query: " + salesPerThousandBlocksQuery)

    urlGateway = 'https://gateway.thegraph.com/api/'
    apiKey = '51d7a63c993112346960cd6c837faa11' # REPLACE THIS WITH YOUR OWN API KEY
    urlRoute = '/subgraphs/id/B333F7Ra4kuVBSwHFDfH9x9N1341GYHvdfpV94KY8Gmv'
    url = urlGateway + apiKey + urlRoute
    r = requests.post(url, json={'query': salesPerThousandBlocksQuery})
    print(r.status_code)
    print(r.text)

    json_data = json.loads(r.text)
    df_data = json_data['data']
    df = pd.DataFrame(df_data)
    df.to_json(r'./data/transactionSalesData' + str(fileCounter) + '.json', orient='index', indent=2)
    fileCounter += 1