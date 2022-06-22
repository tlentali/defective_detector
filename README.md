<p align="center";
    font-family: Georgia, sans-serif;
    text-decoration: none;
    background: #ffbdfb;
    padding: 3px 6px;
    color: #000;
    font-size: 28px;>
    <a href="#"><img src="./misc/car_market_logo.png"  alt="car_market_logo" width="350"/>
    </a>
</p>


<p align="center">
  <b>Defective rate detector.
</p>

# Data

| column name | description |
|---|---|
| DEFECTIVE | whether there was a Technical customer service request linked with the order |
| DATE_ORDER | date of the order |
| CONTACT_DATE | date the customer contacted customer service. Is NaN if no contact has been made |
| CONTACT_TYPE_DETAILS | details about the problem that was reported (e.g. ‘Steering Wheel Shaking’, ‘Faulty Ignition Coil’) |
| PRODUCT_CATEGORY | product category (e.g. car, motorcycle, . . . ) |
| BRAND | product brand (e.g. ‘Ford’) |
| MODEL | product model (e.g. ‘Mustang diesel’). |
| STATE | aesthetic grade of the car, A, B, C and D (where A is the closest to a new product, and D the worst) |
| PRICE | price the merchant is selling the vehicle |
| PRICE_NEW | MSRP of the vehicle |
| MERCHANT_ID | unique ID for each merchant at CarMarket |
| CUSTOMER_COUNTRY | customer’s country |
| MERCHANT_COUNTRY | merchant’s headquarters’ country |
| PRODUCT_RELEASE_DATE | year the model was released (e.g. 1982 for Nissan Micra), note that this is not the date the vehicle was built (which would be between the release date and today) |

    
## EDA
    
The dataset weigth 48Mo. It contains 196113 rows and 15 columns including c categorical and n numrical columns.  
Their is Nan values on columns c and d and the columns x seems to contain random values.  
Their is a strong correlation between column a and b.  

## Target
    
Every defective product is associated with a contact date.  
We can filter on : `DATE_ORDER` - `CONTACT_DATE` <= 30
    
## Feature
    
- remove `CONTACT_DATE` and `CONTACT_TYPE_DETAILS` features as it helps us to define the taget
- add `PRICE_FROM_NEW_PERC` : `PRICE` * 100 / `PRICE_NEW`  

