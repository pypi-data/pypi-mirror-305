import argparse
from roi_count import calc

def main():
    parser = argparse.ArgumentParser(description='Поиск ROI и чистой прибыли')
    parser.add_argument('--r', required=True)
    parser.add_argument('--c', required=True)

    args = parser.parse_args()

    try:
        print(calc(args.r, args.c))
    except Exception as error:
        print(f'Произошла ошибка: {error}')

if __name__ == '__main__':
    main()