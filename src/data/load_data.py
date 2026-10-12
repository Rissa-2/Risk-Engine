#This code loads the data from the ARFF datasets. You need to make sure everything from the
# requirements.txt file is downloaded for this part,
#since the ARFF datasets require the scipy library to load the data, and this is currently in a virtual environment.
# src/data/load_data.py
from pathlib import Path
import pandas as pd
from scipy.io import arff
import io

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw" / "NSL-KDD_Datasets"  
# project_root/data
print(DATA_DIR.exists()) #Making sure the file exists

#This section loads the dataset and converts them into pandas DataFrames (The pandas tables). It also decodes the nominal attributes from bytes to strings, and creates a binary target variable "y" indicating whether the connection is malicious or not (0 = normal, 1 = malicious).
def load_arff(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    fixed = [
        line.replace(", ", ",") if line.lower().startswith("@attribute") else line
        for line in lines 
        #Working on adding this part in so that the program doesn't read the spaces after the commas, because that causes an error while loading the data (scipy rejecting)
    ]
    data, _ = arff.loadarff(io.StringIO("\n".join(fixed)))
    df = pd.DataFrame(data)
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].str.decode("utf-8")   # ARFF nominals load as bytes
    return df

# This section is only a test to make sure that the tables have loaded correctly.
# We still have to code the model into the program to get the results that we want, which is to predict whether the score we put in for a certain attribute is malicious or not.
#So lmk if yall still want to keep this
def load_nsl_kdd():
    train = load_arff(DATA_DIR / "KDDTrain+.arff")
    test = load_arff(DATA_DIR / "KDDTest+.arff")
    for d in (train, test):
        d["y"] = (d["class"] != "normal").astype(int)   # 1 = malicious
    return train, test

if __name__ == "__main__":
    train, test = load_nsl_kdd()
    print(train.shape, test.shape)
    print(train["y"].mean())

#This part incorporates all the attirbutes we will be using. It's just filler data from now, it will be replaced with that ones
#We're using after updates
numeric = ["duration", "src_bytes", "dst_bytes", "count", "srv_count",
           "serror_rate", "same_srv_rate", "dst_host_count",
           "dst_host_srv_count", "logged_in"]
categorical = ["protocol_type", "service", "flag"]