set schema 'shopify';

begin transaction;

insert into pricing_plans values ('4s75255e-96a2-01r8-3j23-sg67913gj6jg', '2f07545e-45e2-40b0-8a40-ef55570cf4f9', 'Ultra Super Mega Pro Plan', 499.90);

insert into pricing_plan_features values ('4s75255e-96a2-01r8-3j23-sg67913gj6jg', '2f07545e-45e2-40b0-8a40-ef55570cf4f9', 'Ultra Super Mega Pro Plan is a celestial gateway to boundless product imports, a treasure trove of awe-inspiring features, and the key to reigning supreme across a multitude of sales realms, where your e-commerce empire ascends to mythical proportions!');

commit;
