import pandas as pd
import logging

from src.names import Names
from src.parameters import Parameters


logging.basicConfig(level=logging.INFO)


class Preparator:
    """
    From raw data to clean and tidy data
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.names = Names()
        self.params = Parameters()

    def compute(self) -> pd.DataFrame:
        self.convert_string_to_datetime(self.params.FEATURE_TO_DATETIME)
        self.defective_days_filter()
        self.get_price_from_new_perc()
        self.price_filter()
        self.price_from_new_perc_filter()
        self.get_days_since_product_release_date()
        return self.df.reset_index(drop=True)

    def convert_string_to_datetime(self, col_list: list) -> None:
        logging.info("Convert string to datetime format.")
        for col_name in col_list:
            self.df[col_name] = pd.to_datetime(self.df[col_name], format="%Y-%m-%d")

    def defective_days_filter(self) -> None:
        logging.info(f"Filter data on {self.params.DEFECTIVE_NB_DAYS} defective days.")
        self.df[self.names.NB_DAYS_PROBLEM_START] = (
            self.df[self.names.CONTACT_DATE] - self.df[self.names.DATE_ORDER]
        ).dt.days
        self.df = self.df[
            (self.df[self.names.NB_DAYS_PROBLEM_START] <= self.params.DEFECTIVE_NB_DAYS)
            | (self.df[self.names.NB_DAYS_PROBLEM_START].isna())
        ]

    def get_price_from_new_perc(self) -> None:
        logging.info("Compute the difference in percent from PRICE_NEW to PRICE.")
        self.df = self.df.copy()
        self.df[self.names.PRICE_FROM_NEW_PERC] = (
            (self.df[self.names.PRICE] - self.df[self.names.PRICE_NEW])
            * 100
            / self.df[self.names.PRICE_NEW]
        )

    def price_filter(self) -> None:
        logging.info("Filter noisy PRICE signal.")
        self.df = self.df[self.df[self.names.PRICE] <= self.params.PRICE_FILTER]

    def price_from_new_perc_filter(self) -> None:
        logging.info(
            "Filter noisy difference in percent from PRICE_NEW to PRICE signal."
        )
        self.df = self.df[
            self.df[self.names.PRICE_FROM_NEW_PERC]
            <= self.params.PRICE_FROM_NEW_PERC_FILTER
        ]

    def get_days_since_product_release_date(self) -> None:
        logging.info(f"Build {self.names.DAYS_SINCE_PRODUCT_RELEASE_DATE} feature.")
        self.df[self.names.DAYS_SINCE_PRODUCT_RELEASE_DATE] = (
            self.df[self.names.DATE_ORDER] - self.df[self.names.PRODUCT_RELEASE_DATE]
        ).dt.days
