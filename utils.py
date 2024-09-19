import pandas as pd

def get_operations_from_report(report):
    file_path = f"files/reports/{report}"
    df = pd.read_excel(file_path)
    opperations = []
    for index, row in df.iterrows():
        data = row.to_dict()
        opperations.append([index, data["Дата операции"], data["Сумма платежа"],
                            data["Валюта платежа"], data["Описание"], data["Категория"],])
    return opperations



if __name__ == "__main__":
    report = "operations Sun Sep 01 11_20_12 MSK 2024-Thu Sep 05 11_06_50 MSK 2024.xls"
    print(get_operations_from_report(report=report), sep="\n")
