
-- Buyers vs Sellers by Marketplace
with a as (
SELECT uniq(senderAddress) as seller, uniq(receiverAddress) as buyer, platform, date
From Opensea_looks_x2y2
group by date, platform 
order by date 
),

o as (
select seller, buyer, platform, date
from a
where platform = 'OpenSea'
),

l as (
select seller, buyer, platform, date
from a
where platform = 'LooksRare'
),

x as (
select seller, buyer, platform, date
from a
where platform = 'X2Y2'
)

select o.seller as OpenSea_Seller, o.buyer as OpenSea_Buyer, 
    l.seller as LooksRare_Seller, l.buyer as LooksRare_Buyer,
    x.seller as X2Y2_Seller, x.buyer as X2Y2_Buyer,
    o.date as date
FROM o
LEFT JOIN l
on o.date = l.date
LEFT JOIN x
on o.date = x.date