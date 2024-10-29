import pandas as pd

def analysis(csv_file, txt_file):
    df = pd.read_csv(csv_file)

    # Подсчёт по возрасту
    ages = df['age'].unique()
    ages_dict = {}
    for age in ages:
        df_sample = df[df['age'] == age]
        ages_dict[age] = len(df_sample)
    list_ages = [f"{key}: {ages_dict[key]}\n" for key in ages_dict.keys()]

    # Подсчёт по городу
    cities = df['city'].unique()
    cities_dict = {}
    for city in cities:
        df_sample = df[df['city'] == city]
        cities_dict[city] = len(df_sample)
    list_cities = [f"{key}: {cities_dict[key]}\n" for key in cities_dict.keys()]

    # Запись в txt
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(f"Общее количество клиентов: {len(df)}\n\n")
        file.write('Количество клиентов по возрастным группам:\n')
        file.writelines(list_ages)
        file.write('\nРаспределение клиентов по городам:\n')
        file.writelines(list_cities)

__all__ = ['analysis']