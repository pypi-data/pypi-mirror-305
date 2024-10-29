import argparse
from . import count_rev_profit

def main():
    parser = argparse.ArgumentParser(description='Подсчет доходов и расходов')
    parser.add_argument('--input-file', required=True)
    parser.add_argument('--output-file', required=True)

    args = parser.parse_args()
    try:
        count_rev_profit(args.input_file, args.output_file)
    except Exception as error:
        print(f'Произошла ошибка: {error}')

if __name__ == '__main__':
    main()