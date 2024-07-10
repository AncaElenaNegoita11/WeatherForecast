import pandas as pd


def dataset_info(dataframe: pd.DataFrame):
    print("Information about non-null values, memory and data types:\n")
    dataframe.info()
    print("Number of duplicated entries in the table: ", dataframe.duplicated().sum())
    print("Maximum temperature reached: ", dataframe.temp_max.max())
    print("Minimum temperature reached: ", dataframe.temp_min.min())
    print("Most common weather: ", dataframe.weather.value_counts().idxmax())


def temp_max_histplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def temp_max_facegrid_lineplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def precipitation_facegrid_scatterplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def weather_countplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def weather_piechart(dataframe: pd.DataFrame):
    """ TODO:
    """


def lr_predictor_random_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def lr_predictor_default_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def svr_predictor_default_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def main():
    df = pd.read_csv('seattle-weather.csv')
    dataset_info(df)


if __name__ == '__main__':
    main()
