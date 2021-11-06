import numpy as np
import pandas as pd

from profit_structure.model.dataset import Dataset


class FinancialStatements(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        return pd.read_csv(f"/data/{payload}.csv")
