import numpy as np
import pandas as pd


class Bin2CSV:
    def __init__(self, filePath):
        self.path = filePath

    def transform(self, outPath):
        data = np.fromfile(self.path, dtype=np.float32)
        # np.savetxt(outPath, data, delimiter=',')
        np.savetxt(outPath, data)

    def cal1(self, filePath: str) -> pd.DataFrame:
        dataset = pd.read_csv(filePath)
        return dataset
