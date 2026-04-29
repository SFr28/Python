import pandas as pd

def load(path: str) -> pd.DataFrame:
    '''Loads a csv doc with a data set, \
    writes its dimensions and returns it'''

    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except FileNotFoundError:
        print("No such file or directory:", path)
    except (ValueError, TypeError) as e:
        print(e)
        return None