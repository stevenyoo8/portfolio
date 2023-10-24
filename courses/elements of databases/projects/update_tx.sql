set schema 'shopify';

begin transaction;

update pricing_plans set price = price * 2 where title like '% Half Price%';
update pricing_plans set title = substring(title, 1, length(title)-11) where title like '% Half Price%';

commit;