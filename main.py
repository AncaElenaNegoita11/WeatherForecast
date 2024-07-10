import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def dataset_info(dataframe: pd.DataFrame):
    print("Information about non-null values, memory and data types:\n")
    dataframe.info()
    print("Number of duplicated entries in the table: ", dataframe.duplicated().sum())
    print("Maximum temperature reached: ", dataframe.temp_max.max())
    print("Minimum temperature reached: ", dataframe.temp_min.min())
    print("Most common weather: ", dataframe.weather.value_counts().idxmax())


def temp_max_histplot(dataframe: pd.DataFrame):
    graph = sns.histplot(dataframe.temp_max)
    graph.set_title('Maximum temperature')
    for p in graph.patches:
        graph.annotate(f'\n{p.get_height()}', (p.get_x() + 0.2, p.get_height()), ha='center', va='top',
                       color='black', size=12)
    plt.show()


def facegrid_plotter(dataframe, type_plot, criteria):
    dataframe["month"] = pd.DatetimeIndex(dataframe["date"]).month
    dataframe["year"] = pd.DatetimeIndex(dataframe["date"]).year
    sns.FacetGrid(data=dataframe, col="year").map_dataframe(type_plot, x="month", y=criteria)
    plt.show()


def temp_max_facegrid_lineplot(dataframe: pd.DataFrame):
    facegrid_plotter(dataframe, sns.lineplot, "temp_max")


def precipitation_facegrid_scatterplot(dataframe: pd.DataFrame):
    facegrid_plotter(dataframe, sns.scatterplot, "precipitation")


def weather_countplot(dataframe: pd.DataFrame):
    graph = sns.countplot(data=dataframe, x="weather")
    graph.set_title('Weather')
    for p in graph.patches:
        graph.annotate(f'\n{p.get_height()}', (p.get_x()+0.2, p.get_height() + 30), ha='center', va='top', color='black', size=12)
    plt.show()


def weather_piechart(dataframe: pd.DataFrame):
    weather_count = dataframe.weather.value_counts()
    plt.pie(weather_count, labels=weather_count.index, autopct='%1.1f%%')
    plt.title("Weather")
    plt.show()


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
    temp_max_histplot(df)
    temp_max_facegrid_lineplot(df)
    precipitation_facegrid_scatterplot(df)
    weather_countplot(df)
    weather_piechart(df)


if __name__ == '__main__':
    main()
