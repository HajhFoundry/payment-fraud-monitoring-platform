import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


CSV_PATH = "data/kaggle/PS_20174392719_1491204439457_log.csv"


def prepare_features(limit: int = 100000):
    df = pd.read_csv(CSV_PATH, nrows=limit)

    df["type_encoded"] = df["type"].astype("category").cat.codes
    df["balance_drained"] = ((df["oldbalanceOrg"] > 0) & (df["newbalanceOrig"] == 0)).astype(int)
    df["amount_to_balance_ratio"] = df.apply(
        lambda row: row["amount"] / row["oldbalanceOrg"] if row["oldbalanceOrg"] > 0 else 0,
        axis=1
    )
    df["destination_balance_change"] = df["newbalanceDest"] - df["oldbalanceDest"]

    features = [
        "type_encoded",
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest",
        "balance_drained",
        "amount_to_balance_ratio",
        "destination_balance_change"
    ]

    X = df[features]
    y = df["isFraud"].astype(int)

    return X, y


def train_model():
    X, y = prepare_features(limit=500000)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = round(accuracy_score(y_test, predictions) * 100, 2)
    precision = round(precision_score(y_test, predictions, zero_division=0) * 100, 2)
    recall = round(recall_score(y_test, predictions, zero_division=0) * 100, 2)
    f1 = round(f1_score(y_test, predictions, zero_division=0) * 100, 2)

    tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()

    print("Random Forest Fraud Model")
    print("-------------------------")
    print(f"Rows Used: {len(X)}")
    print(f"Accuracy: {accuracy}%")
    print(f"Precision: {precision}%")
    print(f"Recall: {recall}%")
    print(f"F1 Score: {f1}%")
    print(f"True Positives: {tp}")
    print(f"False Positives: {fp}")
    print(f"True Negatives: {tn}")
    print(f"False Negatives: {fn}")


if __name__ == "__main__":
    train_model()