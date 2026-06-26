from load_csv import load
import matplotlib.pyplot as plt


def aff_life(data):
    '''
        Fonction to get the correct country's data and to create a graph.
    '''

    try:
        xpoints = data.columns[1:].astype(int)
        if not (data["country"] == "France").any():
            raise IndexError("No value for France")
        ypoints = data[data["country"] == "France"].values[0][1:]

        plt.plot(xpoints, ypoints)

        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')

        plt.xticks(range(1800, 2081, 40))

        plt.show()

    except IndexError as e:
        print("Index error:", e)


def main():
    '''
        Program that loads the file "life_expectancy_years.csv" and displays \
        France information about life expectancy since the 1800s.
    '''

    data = load("life_expectancy_years.csv")

    if data is None:
        print('Failed to load dataset')
        return

    aff_life(data)


if __name__ == "__main__":
    main()
