import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Loads a csv doc with a data set and returns its data in DataFrame'''

    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("No such file or directory:", path)
    except (ValueError, TypeError) as e:
        print(e)
        return None
