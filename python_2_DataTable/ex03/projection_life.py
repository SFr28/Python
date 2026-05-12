from load_csv import load
import matplotlib as mlp
import matplotlib.pyplot as plt


def projection_life(dataIncome, dataLife):
    '''
        Function to create a scatter plot representing \
        life expectancy in relation to the gross national product
    '''

    dataIncome = dataIncome.set_index("country")
    dataLife = dataLife.set_index("country")
    dataIncome.rename(columns=dataIncome.iloc[0])
    dataLife.rename(columns=dataLife.iloc[0])

    xpoints = dataIncome["1900"]
    ypoints = dataLife["1900"]

    plt.scatter(xpoints, ypoints)
    plt.ylabel('Life Expectancy')
    plt.xlabel('Gross domestic product')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], labels=['300', '1k', '10k'])
    norm = mlp.colors.Normalize(vmin=300, vmax=10000, clip=True)
    norm(xpoints)
    plt.title('1900')

    plt.show()


def main():
    '''
        Program that loads the files "life_expectancy_years.csv" \
        and "income_per_person_gdppercapita_ppp_inflation_adjusted.csv," \
        and displays projection of life expectancy in relation to the \
        gross national product of the year 1900 for each country.
    '''

    incomePath = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    dataIncome = load(incomePath)
    dataLife = load("life_expectancy_years.csv")

    if dataIncome is None or dataLife is None:
        print('Failed to load dataset')
        return

    try:
        projection_life(dataIncome, dataLife)
    except TypeError as e:
        print(f"Invalid value: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")


if __name__ == "__main__":
    main()
