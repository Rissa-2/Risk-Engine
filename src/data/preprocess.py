# Preprocess.py transforms it into the format expected by the model.
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.pipeline import Pipeline
from src.data.load_data import numeric, categorical

skewed = ["duration", "src_bytes", "dst_bytes", "count", "srv_count"]
other  = [c for c in numeric if c not in skewed]

prep = ColumnTransformer([
    ("skew", Pipeline([("log", FunctionTransformer(np.log1p)),
                       ("sc", StandardScaler())]), skewed),
    ("num",  StandardScaler(), other),
    ("cat",  OneHotEncoder(handle_unknown="ignore"), categorical),
])