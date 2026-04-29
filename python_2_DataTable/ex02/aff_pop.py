from load_csv import load
import matplotlib.pyplot as plt


def convert_pop(value):
    '''
        Function to convert k, M or B in data with correct value
    '''

    if isinstance(value, str):
        if 'B' in value:
            return float(value.replace('B', '')) * 1_000_000_000
        elif 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
        elif 'k' in value:
            return float(value.replace('k', '')) * 1_000
        else:
            try:
                return float(value)
            except ValueError:
                return None

    return value


def aff_pop(data):
    '''
        Function to get perninent data from the given database regarding \
        population in France and another country (here, Madagascar)
    '''

    cols = data.columns[1:]
    data[cols] = data[cols].map(convert_pop)
    data = data.set_index("country")

    dataFr = data.loc['France', :'2050']
    dataMg = data.loc['Madagascar', :'2050']

    dataFr.plot(legend=True, label='France', c='b')
    dataMg.plot(legend=True, label='Madagascar', c='r')

    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')

    plt.yticks([20000000, 40000000, 60000000],
                labels=['20M', '40M', '60M'])

    plt.show()


def main():
    '''
        Program that loads the file "population_total.csv," and displays \
        France information about population projections versus another country.
    '''

    data = load("population_total.csv")

    if data is None:
        print('Failed to load dataset')
        return

    try:
        aff_pop(data)
    except TypeError as e:
        print(f"Invalid value: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")


if __name__ == "__main__":
    main()
