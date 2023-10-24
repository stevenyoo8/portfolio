set schema 'shopify';

begin transaction;

delete from apps_categories where app_id in (select id from apps where rating < 2 and rating > 0);
     
delete from key_benefits where app_id in (select id from apps where rating < 2 and rating > 0);
       
delete from pricing_plan_features where app_id in (select id from apps where rating < 2 and rating > 0);
       
delete from pricing_plans where app_id in (select id from apps where rating < 2 and rating > 0);
       
delete from reviews where app_id in (select id from apps where rating < 2 and rating > 0);       
       
delete from apps where rating < 2 and rating > 0;


commit;
