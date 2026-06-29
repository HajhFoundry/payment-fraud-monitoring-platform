import pandas as pd


CSV_PATH = "data/kaggle/PS_20174392719_1491204439457_log.csv"


def rule_based_prediction(row):
    amount = float(row["amount"])
    transaction_type = str(row["type"])
    old_balance = float(row["oldbalanceOrg"])
    new_balance = float(row["newbalanceOrig"])

    if transaction_type in ["TRANSFER", "CASH_OUT"]:
        if old_balance > 0 and new_balance == 0 and amount >= old_balance * 0.8:
            return 1

    return 0


def evaluate_rule_engine(limit: int = 10000):
    df = pd.read_csv(CSV_PATH, nrows=limit)

    df["actual_fraud"] = df["isFraud"].astype(int)
    df["predicted_fraud"] = df.apply(rule_based_prediction, axis=1)

    true_positive = len(df[(df["actual_fraud"] == 1) & (df["predicted_fraud"] == 1)])
    false_positive = len(df[(df["actual_fraud"] == 0) & (df["predicted_fraud"] == 1)])
    true_negative = len(df[(df["actual_fraud"] == 0) & (df["predicted_fraud"] == 0)])
    false_negative = len(df[(df["actual_fraud"] == 1) & (df["predicted_fraud"] == 0)])

    total = len(df)

    accuracy = round((true_positive + true_negative) / total * 100, 2) if total else 0
    precision = round(true_positive / (true_positive + false_positive) * 100, 2) if (true_positive + false_positive) else 0
    recall = round(true_positive / (true_positive + false_negative) * 100, 2) if (true_positive + false_negative) else 0
    f1_score = round(
        2 * (precision * recall) / (precision + recall),
        2
    ) if (precision + recall) else 0

    print("Rule Engine Evaluation")
    print("----------------------")
    print(f"Rows Evaluated: {total}")
    print(f"True Positives: {true_positive}")
    print(f"False Positives: {false_positive}")
    print(f"True Negatives: {true_negative}")
    print(f"False Negatives: {false_negative}")
    print(f"Accuracy: {accuracy}%")
    print(f"Precision: {precision}%")
    print(f"Recall: {recall}%")
    print(f"F1 Score: {f1_score}")

    return {
        "rows_evaluated": total,
        "true_positive": true_positive,
        "false_positive": false_positive,
        "true_negative": true_negative,
        "false_negative": false_negative,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }


if __name__ == "__main__":
    evaluate_rule_engine(limit=10000)