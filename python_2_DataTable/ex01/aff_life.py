from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff(data: pd.DataFrame):
    '''
        Fonction to get the correct country's data and to create a graph.
    '''

    xpoints = data.columns[1:].astype(int)
    ypoints = data[data["country"] == "France"].values[0][1:]

    plt.plot(xpoints, ypoints)

    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')

    plt.xticks(range(1800, 2081, 40))

    plt.show()


def main():
    '''
        Program that loads the file "life_expectancy_years.csv" and displays \
        the France information about life expectancy since the 1800s.
    '''

    data = load("life_expectancy_years.csv")

    if data is None:
        print('Failed to load dataset')
        return

    aff(data)

if __name__ == "__main__":
    main()
