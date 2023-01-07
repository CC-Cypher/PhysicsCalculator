import numpy as np
import pandas as pd


class phyMath:
    def __init__(self):
        pass

    def simpleAdd(self, x: int, y: int) -> int:
        return x + y

    def cal1(self, filePath: str) -> pd.DataFrame:
        dataset = pd.read_csv(filePath)
        return dataset
