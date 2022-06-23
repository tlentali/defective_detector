from src.names import Names


class Parameters:
    def __init__(self):
        self.names = Names()
        self.RANDOM_SEED: int = 42
        self.TRAIN_TEST_SPLIT: int = 0.20
        self.DEFECTIVE_NB_DAYS: int = 30
        self.PRICE_FILTER: float = 60_000
        self.PRICE_FROM_NEW_PERC_FILTER: float = 100
        self.TARGET = self.names.DEFECTIVE
        self.COLUMNS_TO_KEEP: list = [
            self.names.PRODUCT_CATEGORY,
            self.names.BRAND,
            self.names.MODEL,
            self.names.STATE,
            self.names.PRICE,
            self.names.PRICE_NEW,
            self.names.CUSTOMER_COUNTRY,
            self.names.MERCHANT_COUNTRY,
            self.names.PRICE_FROM_NEW_PERC,
            self.names.DAYS_SINCE_PRODUCT_RELEASE_DATE,
        ]
        self.COLUMNS_TO_DUMMIES: list = [
            self.names.PRODUCT_CATEGORY,
            self.names.BRAND,
            self.names.MODEL,
            self.names.STATE,
            self.names.CUSTOMER_COUNTRY,
            self.names.MERCHANT_COUNTRY,
        ]
        self.FEATURE_TO_DATETIME: list = [
            self.names.DATE_ORDER,
            self.names.CONTACT_DATE,
            self.names.PRODUCT_RELEASE_DATE,
        ]
        self.LOG_PATH: str = "../data/logs/"
