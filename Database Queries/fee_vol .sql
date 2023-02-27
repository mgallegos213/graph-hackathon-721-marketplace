
-- Fee Volume by Marketplace

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
select round(ETH_Volume*0.05,2) as X2Y2_fee, date
from vol
where platform = 'X2Y2'
GROUP BY X2Y2_fee, date
),
l as (
select round(ETH_Volume*0.02,2) as LooksRare_fee, date
from vol
where platform = 'LooksRare'
group by LooksRare_fee, date
),
x as (
select round(ETH_Volume*0.025,2) as Opensea_fee, date
from vol
where platform = 'OpenSea'
group by Opensea_fee, date
)

select Opensea_fee, LooksRare_fee, X2Y2_fee, o.date as date
FROM o
LEFT JOIN l
on o.date = l.date
LEFT JOIN x
on o.date = x.date
order by date