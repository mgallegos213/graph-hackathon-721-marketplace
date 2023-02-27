
--A query outline for our ClickHouse DB used to visualize data

--Transaction Count

with a as (
SELECT uniq(transactionID) as tx_id, platform, date
FROM "Opensea_looks_x2y2"
GROUP BY platform, date
ORDER BY date 
),

o as (
SELECT tx_id as opensea, date
from a
where platform = 'OpenSea'
),

l as (
SELECT tx_id as looksrare, date
from a
where platform = 'LooksRare'
),

x as (
SELECT tx_id as x2y2, date
from a
where platform = 'X2Y2'
)

select opensea, looksrare, x2y2, o.date as date
FROM o
LEFT JOIN l
on o.date = l.date
LEFT JOIN x
on o.date = x.date