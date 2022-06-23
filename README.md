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

# How to run it ?

We can clone this projet like so :

```bash
git clone https://github.com/tlentali/car_market.git
```

Then I would recommand to build a python3 virtual environement for this project, installing only the needed library found in the `requirement.txt`.  
For this project I choose `python3.7`.  

Then by launching `jupyter notebook`, we can execute the code via the `notebook/pipeline.ipynb`.  
The actual code used is in `src/`.


Also a drafted EDA can be visible on `notebook/eda.ipynb`.  
A more detailed EDA is visible [here](https://tlentali.github.io/car_market/).  

# EDA

<p align="center";
    font-family: Georgia, sans-serif;
    text-decoration: none;
    background: #ffbdfb;
    padding: 3px 6px;
    color: #000;
    font-size: 28px;>
    <a href="#"><img src="./misc/most_expensive_car_ever.png"  alt="car_market_logo" width="350"/>
    </a>
</p>

<p align="center">
  <b>The Xsara Micro Red1. <br>In Bulgary, you can have it for 449 907 euro.
</p>


The dataset weighs 48Mo.
It contains 196112 rows and 15 [columns](./data/data_columns.md) including 4 numeric, 2 boolean, 3 datetime and 7 categorical columns.  
Overall the raw data is quite clean as their is no duplicate rows and we can find `Nan` values only on columns `CONTACT_DATE` and `CONTACT_TYPE_DETAILS` as expected and indicated in the instruction.  
The strongest correlation are find between columns `PRICE` and `PRICE_NEW` and between columns `DEFECTIVE` and `has_contact`.  
None of the columns seems to contain random values.

However, we have to filter the rows where the price is not realistic : even if the Xsara is a magnificiant car, I hardly believe that it costs half a million euros for the simple pleasure to drive this red piece of art...  
A work on the price has to be made.  
The detailed EDA is available on a data sample [here](https://tlentali.github.io/car_market/).



## Target

Every defective product is associated with a contact date.  
We are going to filter on :

> `DATE_ORDER` - `CONTACT_DATE` <= 30

We obtain a loss of defective item :

| | before filter | after filter |
|---|---|---|
| False | 164529 | 164523 |
| True  | 31583 | 15611 |

## Feature

First thing first, we should clean the price repartition.
From this [notebook](./notebook/eda.ipynb), we can see the different distribution of several price related columns showing clearly the long tail and the noise we can cut off in our data.  
From this EDA, two decision has been made :

- the `PRICE` can't be 100% higher than the `PRICE_NEW`
- the `PRICE` can't be higher than 60_000 euro

By doing so, their is the defective distribution evol :

| | before filter | after filter |
|---|---|---|
| False | 164523 | 162714 |
| True | 15611 | 15457 |

Then, we can work on the other features :
- remove `CONTACT_DATE` and `CONTACT_TYPE_DETAILS` features, as it helps us to define the taget
- add `PRICE_FROM_NEW_PERC` (= (`PRICE_NEW` - `PRICE`) * 100 / `PRICE_NEW`)
- add `DAYS_SINCE_PRODUCT_RELEASE_DATE`

## Training

In order to evaluate our model, we are going to split our dataset in train (80%) and test (20%).  
We generate dummies features from the following categorial columns :
  - `PRODUCT_CATEGORY`
  - `BRAND`
  - `MODEL`
  - `STATE`
  - `CUSTOMER_COUNTRY`
  - `MERCHANT_COUNTRY`

As the classes are highly unbalanced, we will use an oversampling method ([SMOTE](https://github.com/scikit-learn-contrib/imbalanced-learn)) to balance the binary classes (only 16% of True defective products on raw data).  
To start simply, I decided to consider this problem as a binary class one.  
I trained a unoptimized (I haven't use a [Gridsearch](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) to test several parameters) [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) classifier as it doesn't need to scale the data to perform and is easy to visualize the feature importance via a [decision tree explainer](https://github.com/slundberg/shap).

## Metrics

The score obtained using a simple [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) classifier :

| | precision | recall | f1-score | support |
|---|---|---|---|---|
False |	0.946368  | 0.873494 |	0.908472 |	32544.000000 |
True 	| 0.264427 	| 0.478809 |	0.340700 |	3091.000000 |
accuracy | 	0.839259 |	0.839259 |	0.839259 |	0.839259 |
macro avg |	0.605398 |	0.676152 |	0.624586 |	35635.000000 |
weighted avg |	0.887216 |	0.839259 |	0.859223 |	35635.000000 |

This first modelisation might help as a first step to rise a red flag on potentialy defective items.  
However it does not revolutionalize the game as the precision and recall on True defective item are quite low.  
By working more on the feature engineering and by a deeper data cleaning, we can expect to improve our metrics.  
Even the usage of an optimized classifier might help a little here as we did someting really basic today.  
A feature importance graph is visible in the [pipeline notebook](/notebook/pipeline.ipynb).
                                    
# Future improvement

In another hand, we could approach this problem differently by using time series and instead of having to classify defecting product on 30 days, we could get a score depending of the timeframe you are looking for.

Also, it would be interesting if we could add more data focus on the seller and the customer, as I think that we can have a defective rate higher or lower depending of those two, based on their history on the app.  
Having the milage of the car might be the killer feature here.

A work can also be done directly (after a cleaning prossess of course) on the very reason of the defective product, transforming this binary problem in a multiclass one.  
Leading to be (very) good on certain classes and putting aside the more random defective reasons.

In a more code quality point of view, a great improvement would be to add unittest to the script and more docstrings.

Thank Pola and the BackBox team for this dataset, I enjoyed playing with it.

Made with 🎶 and 🍷 with my beloved refurbished Thinkpad T420 from BackMarket.
