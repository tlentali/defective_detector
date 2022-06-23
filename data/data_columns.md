| column name | Description | Type |
|---|---|---|
| DEFECTIVE | whether there was a Technical customer service request linked with the order | Boolean |
| DATE_ORDER | date of the order | Date |
| CONTACT_DATE | date the customer contacted customer service. Is NaN if no contact has been made | Date |
| CONTACT_TYPE_DETAILS | details about the problem that was reported (e.g. ‘Steering Wheel Shaking’, ‘Faulty Ignition Coil’) | Categorical |
| PRODUCT_CATEGORY | product category (e.g. car, motorcycle, . . . ) | Categorical |
| BRAND | product brand (e.g. ‘Ford’) | Categorical |
| MODEL | product model (e.g. ‘Mustang diesel’). | Categorical |
| STATE | aesthetic grade of the car, A, B, C and D (where A is the closest to a new product, and D the worst) | Categorical |
| PRICE | price the merchant is selling the vehicle | Numeric |
| PRICE_NEW | MSRP of the vehicle | Numeric |
| MERCHANT_ID | unique ID for each merchant at CarMarket | Numeric |
| CUSTOMER_COUNTRY | customer’s country | Categorical |
| MERCHANT_COUNTRY | merchant’s headquarters’ country | Categorical |
| PRODUCT_RELEASE_DATE | year the model was released (e.g. 1982 for Nissan Micra), note that this is not the date the vehicle was built (which would be between the release date and today) | Date |
| has_contact | Boolean indicating if contact has been made between customer and constomer service (not indicated in the instruction) | Boolean |