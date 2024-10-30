import argparse
import pandas as pd


def load_clients(input_file):
    df = pd.read_csv(input_file)
    return df


def calculate_statistics(df):
    total_clients = len(df)

    age_groups = {
        '18-25': ((df['age'] >= 18) & (df['age'] <= 25)).sum(),
        '26-35': ((df['age'] >= 26) & (df['age'] <= 35)).sum(),
        '36-45': ((df['age'] >= 36) & (df['age'] <= 45)).sum(),
        '46-60': ((df['age'] >= 46) & (df['age'] <= 60)).sum(),
    }

    cities_distribution = df['city'].value_counts().to_dict()

    return total_clients, age_groups, cities_distribution


def generate_report(output_file, total_clients, age_groups, cities_distribution):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Общее количество клиентов: {total_clients}\n\n")
        f.write("Количество клиентов по возрастным группам:\n")
        for group, count in age_groups.items():
            f.write(f"{group}: {count}\n")

        f.write("\nРаспределение клиентов по городам:\n")
        for city, count in cities_distribution.items():
            f.write(f"{city}: {count}\n")


def main():
    parser = argparse.ArgumentParser(description="Анализ данных о клиентах")
    parser.add_argument('--input-file', type=str, required=True, help='Путь к входному CSV-файлу с данными о клиентах')
    parser.add_argument('--output-file', type=str, required=True, help='Путь к выходному файлу для отчета')

    args = parser.parse_args()

    clients_data = load_clients(args.input_file)

    total_clients, age_groups, cities_distribution = calculate_statistics(clients_data)

    generate_report(args.output_file, total_clients, age_groups, cities_distribution)


if __name__ == "__main__":
    main()