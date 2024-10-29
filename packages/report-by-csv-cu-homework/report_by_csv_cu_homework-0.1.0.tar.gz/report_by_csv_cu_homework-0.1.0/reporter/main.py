import pandas as pd


def get_report(input_file):
    df = pd.read_csv(input_file)
    report = df.groupby("category")["amount"].sum()
    return report


def save_report(report, output_file):
    with open(output_file, "w") as f:
        for category, amount in report.items():
            f.write(f"{category}: {amount} руб.\n")
