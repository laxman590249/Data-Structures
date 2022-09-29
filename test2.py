data = """account_reps
axs_event_mapping
axs_venue_mapping
customer_fields
customer_phone
customer_address
customers
event_category
events
inventory_snapshot
inventory
method_of_delivery
offer_group_products
offer_groups
offer_method_of_delivery
order_fee_comp_tax_comp
order_price_components
order_price_comp_tax_comp
offer_outlets
offers
order_fees
order_refunds
orders
order_tags
order_tickets
payment_distributions
payments
price_chart
price_codes
price_components
price_levels
products
reservations_sold
scans
seat_groups
seats
status_codes
venues
customer_field_lists
price_code_attributes
zone_glcodes
zones"""


data_snowflake = """account_reps
customer_address
customer_field_lists
customer_fields
customers
event_category
events
inventory_snapshot
method_of_delivery
offer_group_products
offer_groups
offer_method_of_delivery
offer_outlets
offers
order_fee_comp_tax_comp
order_fee_components
order_fees
order_price_comp_tax_comp
order_price_components
order_refunds
order_tags
order_tickets
orders
payment_distributions
payments
price_chart
price_code_attributes
price_codes
price_components
price_levels
products
reservations_sold
scans
seat_groups
seats
status_codes
venues
zone_glcodes
zones
"""

data_not_today = """axs_event_mapping
axs_venue_mapping
customer_phone
inventory
order_tickets"""

set_data = list(set(data.split('\n')))
set_snowflake = data_snowflake.split('\n')
set_not_today = data_not_today.split('\n')
set_result= []

for table in set_data:
    if table not in set_not_today:
        set_result.append(table)

print('INSERT INTO "DATAPLATFORM"."CONFIG_US"."VERITIX_COLLECTOR_DETAILS" VALUES ')
for table in set_data:
    if table not in set_snowflake:
        print(f"(707871657, 'opryentgrp', '{table}', '1900-01-01 00:00:00.000', TRUE),")
        print(f"(489512047, 'timberwolves', '{table}', '1900-01-01 00:00:00.000', TRUE),")

for table in set_data:
    print(f'DELETE FROM "ANALYTICS"."TICKETING_US"."{table.upper()}" where  CONTEXT_ID in( 489512047, 707871657);')


print(len(set_result))
print(','.join(set_result))
