
-- Volume in ETH by Marketplace

with a as (
SELECT distinct(transactionID), amount, platform, date, collection
from Opensea_looks_x2y2
),
vol as (
select round(sum(amount),2) as ETH_Volume, platform, date
from a
group by platform, date
order by date 
),
o as (
select ETH_Volume as X2Y2_vol, date
from vol
where platform = 'X2Y2'
),
l as (
select ETH_Volume as LooksRare_vol, date
from vol
where platform = 'LooksRare'
),
x as (
select ETH_Volume as Opensea_vol, date
from vol
where platform = 'Opensea_vol'
)

select Opensea_vol, LooksRare_vol, X2Y2_vol, o.date as date
FROM o
LEFT JOIN l
on o.date = l.date
LEFT JOIN x
on o.date = x.date
order by date