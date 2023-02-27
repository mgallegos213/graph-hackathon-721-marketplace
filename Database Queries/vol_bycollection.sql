
-- Weekly Volume by Collection in ETH All 3 mktplaces

with a as (
SELECT distinct(transactionID), amount, platform, date, collection
from Opensea_looks_x2y2
)
Select round(sum(amount),0) as ETH_vol, collection
from a
group by collection
order by ETH_vol desc
limit 10