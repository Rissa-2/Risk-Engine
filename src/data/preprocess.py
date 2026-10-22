# Preprocess.py transforms the NSL-KDD data into the format expected by the model.
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.pipeline import Pipeline

# Keep a conservative fallback list for cases where a DataFrame is not passed in.
FALLBACK_NUMERIC = [
    "wrong_fragment",
    "num_failed_logins",
    "num_compromised",
    "num_shells",
    "srv_count",
    "serror_rate",
    "rerror_rate",
    "same_srv_rate",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
]
FALLBACK_CATEGORICAL = ["flag", "land", "is_host_login"]

# Infer the numeric and categorical feature columns from a DataFrame.
def _infer_feature_columns(df):
    exclude = {"y", "class"}
    columns = [column for column in df.columns if column not in exclude]

    categorical = [
        column
        for column in columns
        if pd.api.types.is_object_dtype(df[column])
        or pd.api.types.is_string_dtype(df[column])
        or pd.api.types.is_categorical_dtype(df[column])
    ]
    numeric = [column for column in columns if column not in categorical]
    return numeric, categorical

# Preprocess the DataFrame into a format suitable for model training.
def prep(df=None):
    if df is not None:
        numeric, categorical = _infer_feature_columns(df)
    else:
        numeric = FALLBACK_NUMERIC
        categorical = FALLBACK_CATEGORICAL

    skewed = [
        column
        for column in numeric
        if column in {"num_compromised", "num_shells", "wrong_fragment", "num_failed_logins", "srv_count"}
    ]
    other = [column for column in numeric if column not in skewed]

    transformers = []
    if skewed:
        transformers.append(
            (
                "skew",
                Pipeline([
                    ("log", FunctionTransformer(np.log1p)),
                    ("sc", StandardScaler()),
                ]),
                skewed,
            )
        )
    if other:
        transformers.append(("num", StandardScaler(), other))
    if categorical:
        transformers.append(("cat", OneHotEncoder(handle_unknown="ignore"), categorical))

    if not transformers:
        raise ValueError("No valid feature columns were found to preprocess.")

    return ColumnTransformer(transformers=transformers, remainder="drop")

