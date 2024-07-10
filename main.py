import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import LinearSVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression


NUM_TRAIN_SAMPLES = 1300

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


def lr_predictor(X_test, y_test, regression):
    predictions = regression.predict(X_test.drop(['date'], axis=1))
    print("R2 score: ", r2_score(y_test, predictions))
    print("Mean squared error: ", mean_squared_error(y_test, predictions))
    X_test_plot = np.array(X_test['date'])
    y_test_plot = np.array(y_test)
    predictions_plot = np.array(predictions)
    plt.plot(X_test_plot, y_test_plot, color="blue", label="Actual")
    plt.rcParams["figure.figsize"] = (20, 10)
    plt.scatter(X_test_plot, y_test_plot)
    plt.plot(X_test_plot, predictions_plot, color="red", label="Predicted")
    plt.scatter(X_test_plot, predictions_plot)
    plt.title("Linear Regression")
    plt.show()


def lr_predictor_random_split(dataframe: pd.DataFrame):
    df_train = dataframe.iloc[:NUM_TRAIN_SAMPLES]
    df_test = dataframe.iloc[NUM_TRAIN_SAMPLES:]
    X_train = df_train.drop(["temp_max", "weather"], axis=1)
    X_test = df_test.drop(["temp_max", "weather"], axis=1)
    y_train = df_train.temp_max
    y_test = df_test.temp_max
    linear_regression = LinearRegression().fit(X_train.drop(['date'], axis=1), y_train)
    lr_predictor(X_test, y_test, linear_regression)


def lr_predictor_default_split(dataframe: pd.DataFrame):
    features = dataframe[["precipitation", "date", "month", "year", "wind", "temp_min"]].dropna()
    X_train, X_test, y_train, y_test = train_test_split(features, dataframe.temp_max, test_size=.2, shuffle=False)
    linear_regression = LinearRegression().fit(X_train.drop(['date'], axis=1), y_train)
    lr_predictor(X_test, y_test, linear_regression)


def svr_predictor_default_split(dataframe: pd.DataFrame):
    features = dataframe[["precipitation", "date", "month", "year", "wind", "temp_min"]].dropna()
    X_train, X_test, y_train, y_test = train_test_split(features, dataframe.temp_max, test_size=.2, shuffle=False)
    regression = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-5))
    regression.fit(X_train.drop(['date'], axis=1), y_train)
    lr_predictor(X_test, y_test, regression)


def main():
    df = pd.read_csv('seattle-weather.csv')
    print(df.head())
    df['date'] = pd.to_datetime(df['date'])
    print(df.head())
    dataset_info(df)
    temp_max_histplot(df)
    temp_max_facegrid_lineplot(df)
    precipitation_facegrid_scatterplot(df)
    weather_countplot(df)
    weather_piechart(df)
    lr_predictor_default_split(df)
    lr_predictor_random_split(df)
    svr_predictor_default_split(df)


if __name__ == '__main__':
    main()
