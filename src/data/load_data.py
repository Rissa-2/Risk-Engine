# src/data/load_data.py
from pathlib import Path
import pandas as pd
from scipy.io import arff

DATA_DIR = Path(__file__).resolve().parents[2] / "data"   # project_root/data

def load_arff(path):
    data, _ = arff.loadarff(path)
    df = pd.DataFrame(data)
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].str.decode("utf-8")   # ARFF nominals load as bytes
    return df

def load_nsl_kdd():
    train = load_arff(DATA_DIR / "KDDTrain+.arff")
    test = load_arff(DATA_DIR / "KDDTest+.arff")
    for d in (train, test):
        d["y"] = (d["class"] != "normal").astype(int)   # 1 = malicious
    return train, test

if __name__ == "__main__":
    train, test = load_nsl_kdd()
    print(train.shape, test.shape)
    print(train["y"].mean(), test["y"].mean())