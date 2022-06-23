import pandas as pd
import shap
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

from src.names import Names
from src.parameters import Parameters
import logging


logging.basicConfig(level=logging.INFO)


class Train:
    """
    Select the right features, process the train test split, build and evaluate the model
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.names = Names()
        self.params = Parameters()
        self.X, self.y = self.get_X_y()

    def compute(self) -> None:
        self.split_train_test()
        self.generate_dummies()
        self.get_smote()
        self.build_model()
        self.model_evaluation()

    def get_X_y(self):
        logging.info("Get X and y.")
        return (self.df[self.params.COLUMNS_TO_KEEP], self.df[self.params.TARGET])

    def split_train_test(self) -> None:
        logging.info("Split train test.")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X,
            self.y,
            test_size=self.params.TRAIN_TEST_SPLIT,
            stratify=self.y,
            random_state=self.params.RANDOM_SEED,
        )

    def generate_dummies(self) -> None:
        logging.info("Generate dummies from categorial columns.")
        self.X_train = pd.get_dummies(
            self.X_train, columns=self.params.COLUMNS_TO_DUMMIES
        )
        self.X_test = pd.get_dummies(
            self.X_test, columns=self.params.COLUMNS_TO_DUMMIES
        )

    def get_smote(self) -> None:
        logging.info("Rebalance binary classification using oversampling.")
        sm = SMOTE(random_state=self.params.RANDOM_SEED)
        self.X_res, self.y_res = sm.fit_resample(self.X_train, self.y_train)

    def build_model(self) -> None:
        logging.info("Train Random Forest model.")
        self.clf = RandomForestClassifier(
            max_depth=5, random_state=self.params.RANDOM_SEED
        ).fit(self.X_res, self.y_res)

    def prediction(self, X) -> pd.DataFrame:
        return self.clf.predict_proba(X)

    def model_evaluation(self) -> pd.DataFrame:
        report = classification_report(
            self.y_test, self.clf.predict(self.X_test), output_dict=True
        )
        return pd.DataFrame(report).transpose()

    def confusion_matrix(self):
        return ConfusionMatrixDisplay.from_predictions(
            self.y_test, self.clf.predict(self.X_test)
        )

    def get_feature_importance(self):
        explainer = shap.TreeExplainer(self.clf)
        shap_values = explainer.shap_values(self.X_test)
        return shap.summary_plot(shap_values, self.X_test)
