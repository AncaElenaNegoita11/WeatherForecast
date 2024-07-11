# Weather-Forecast

## Task 1 - Dataset

The table needs to be analysed in order to verify values and understand the logic.

### _dataframe.info()_
`Shows more information about each column of the table, including the total number of entries in
the table, and the number of non-null values.`

RangeIndex: 1461 entries, 0 to 1460

| NO. | Column        | Non-Null Count | Dtype   |
|-----|---------------|----------------|---------|
| 0   | date          | 1461 non-null  | object  |
| 1   | precipitation | 1461 non-null  | float64 |
| 2   | temp_max      | 1461 non-null  | float64 |
| 3   | temp_min      | 1461 non-null  | float64 |
| 4   | wind          | 1461 non-null  | float64 |
| 5   | weather       | 1461 non-null  | object  |

### _dataframe.duplicated().sum()_
`Calculates the total number of entries that are duplicated in the table. In this case, the entries
are unique. `

Number of duplicated entries in the table:  0

### _dataframe.max() and dataframe.min()_
`Calculates the maximum and minimum values on a column. The maximum and minimum values of a column
can be found by using dataframe.name_column.max() and dataframe.name_column.min(). ` 

Maximum temperature reached:  35.6
Minimum temperature reached:  -7.1

### _dataframe.value_counts().idxmax()_
`value_counts() calculates the number of appearances of different entries in a table, while idxmax()
selects the attribute with the biggest number.`

Most common weather:  rain

## Task 2 - Plots
### Maximum temperature shown using simple Histplot
The approximate average temperature reached through the years is between 10 and 15 degrees.
![max_temp_histplot.png](images/max_temp_histplot.png)

### Maximum temperature shown using simple FaceGrid Lineplot
The temperatures through the years tend to have the same maximum value and concave curve.

![max_temp_facegrid_lineplot.png](images/max_temp_facegrid_lineplot.png)

### Precipitation shown using simple FaceGrid Scatterplot
In 2015, there are more values that tend to reach the maximum number of precipitations.

![precipitation_facegrid_scatterplot.png](images/precipitation_facegrid_scatterplot.png)

### Weather conditions shown using countplot
By analysing the plot, it is remarked that it has rained the most throughout the years. The sunny
days are also tending to reach maximum value.
![weather_countplot.png](images/weather_countplot.png)

### Weather conditions shown using pieplot
All the values are calculated using percentages.
![weather_pieplot.png](images/weather_pieplot.png)

## Task 3 - Weather Prediciton
In the following graphs, the blue line represents the actual data that was provided(test data),
while the red line represents the prediction made by using different approaches in linear regression
algorithms.

### Linear Regression - Default
The predictions of the provided data are generated using Machine Learning.
In the first method, the dataset is divided using standard split(80% train, 20% test) and 
test_and_split function.

![lr_default.png](images/lr_default.png)

R2 score:  0.7936850590036182
Mean squared error:  11.297832171916607

### Linear Regression - Random
This method uses a defined part of the dataset as train data(1300 entries), and the rest as tests.

![lr_random.png](images/lr_random.png)

R2 score:  0.8334768729365956
Mean squared error:  9.57073469668931

### Linear SVR
![svr.png](images/svr.png)

R2 score:  0.7770169202956801
Mean squared error:  12.210581548336291

