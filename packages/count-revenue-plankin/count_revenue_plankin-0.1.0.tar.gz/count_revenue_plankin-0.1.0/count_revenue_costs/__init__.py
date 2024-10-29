import pandas as pd

def count_rev_profit(path_file_on, path_file_off):
    df = pd.read_csv(path_file_on)
    revenue = df[df['category'] == 'Доход']['amount'].sum()
    costs = df[df['category'] == 'Расход']['amount'].sum()
    with open(path_file_off, 'w', encoding='utf-8') as file:
        file.write(f'Доход: {revenue} руб.\n')
        file.write(f'Расходы: {costs} руб.')