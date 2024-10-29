import pandas as pd


def generate_report(input_file, output_file):
    df = pd.read_csv(input_file)
    age_bins = [18, 25, 35, 45, 60, 100]
    age_labels = ['18-25', '26-35', '36-45', '46-60', '60+']
    df['age group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    age_distribution = df['age group'].value_counts()

    city_distribution = df['city'].value_counts()

    report = f"Общее количество клиентов: {len(df)}\n\n"

    report += "Количество клиентов по возрастным группам:\n"
    for age_group, count in age_distribution.items():
        report += f"{age_group}: {count}\n"

    report += "\nРаспределение клиентов по городам:\n"
    for city, count in city_distribution.items():
        report += f"{city}: {count}\n"

    with open(output_file, 'w') as f:
        f.write(report)
