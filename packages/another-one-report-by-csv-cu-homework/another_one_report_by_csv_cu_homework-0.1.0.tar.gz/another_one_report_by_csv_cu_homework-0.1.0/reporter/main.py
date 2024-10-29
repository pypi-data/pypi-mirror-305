import pandas as pd


def get_report(input_file):
    df = pd.read_csv(input_file)
    report = df.groupby("category").agg({"sales": "sum", "quantity": "sum"})
    return report.reset_index()


def save_report(report, output_file):
    report.to_csv(output_file, index=False)
