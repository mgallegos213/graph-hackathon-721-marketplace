# NFT Analysis across ETH marketplaces
## The purpose of this project is for education and awareness.

### Background
- NFTs are a hot topic with much talk about rugpulls and scams
- We want to showcase an analysis of collections across marketplaces
- By aggregating data over time, we can help users build confidence in exploring NFTs to buy or invest in
    - Higher volume collections indicates more stability in investment, but can also indicate more wash sales (thus artificial price increase)
- The Graph will help us with this to ensure we are always getting fresh and accurate data regarding NFT transactions on Ethereum
    - This can be implemented with other chains as well, see improvements section below.

### Implementation
#### Subgraphs
- [Marketplace 721 for ERC-721 transactions](https://thegraph.com/explorer/subgraphs/B333F7Ra4kuVBSwHFDfH9x9N1341GYHvdfpV94KY8Gmv?)
    - Problem: OpenSea not currently supported due to their [migration to Seaport contract](https://cointelegraph.com/news/opensea-announces-migration-to-seaport-protocol)
    - Solution: Onboard separate OpenSea Subgraph to same data table/format
- [OpenSea Seaport by Messari](https://thegraph.com/explorer/subgraphs/G1F2huam7aLSd2JYjxnofXmqkQjT5K2fRjdfapwiik9c?view=Overview&chain=mainnet)

#### Queries
- For loop to iterate over 300 blocks at a time in subgraph data
    - Done this way to work with the 100 data item response limit from The Graph API
- [Marketplace 721 Queries](/queryToFile.py)
    - [Query data files](/data/)
- [OpenSea Seaport Queries](/openSeaQueryToFile.py)
    - [Query data files](/openSeaData/)
- [NFT Marketplace Analysis data cleaned into one DataFrame](/NFTMarketplaceAnalysis.py)
    - [output.csv](/output.csv)


### Future Improvements
If we had more time and more Graph queries available:
- Frontend UI
    - Blockchain explorer for individual NFTs/collections
    - Live data feed over longer periods of time
    - Estimate which collections harbor more risk (wash sales)
- Support more subgraphs/chains
    - Polygon
    - Avalanche
    - Solana
    - Arbitrum
    - And more