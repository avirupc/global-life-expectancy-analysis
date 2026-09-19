# Global Life Expectancy Analysis

## Project outline
In this project, we will dive into the story of how life expectancy has evolved across countries and over time, using real-world data as your foundation. Drawing from a collection of World Bank datasets—including life expectancy at birth (with gender breakdowns), death rates, and fertility rates—we will uncover patterns and insights that reveal broader global health trends.<br>
We intend to translate these raw datasets into meaningful visual narratives using Python as our primary tool for data processing, visualization, and dashboard creation.

## Data
Perform data analysis on Life expectancy at birth data from the world bank group found here: [Life Expectancy Data](https://data.worldbank.org/indicator/SP.DYN.LE00.IN). On the site you will find multiple datasets available.<br>
In this project we focus on the following datasets:
- [Life expectancy at birth, total (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)
- [Life expectancy at birth, male (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN)
- [Life expectancy at birth, female (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN)
- [Death rate, crude (per 1,000 people)](https://data.worldbank.org/indicator/SP.DYN.CDRT.IN)
- [Fertility rate, total (births per woman)](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN)

**Important note:** Unless gender is specified for life expectancy, you can assume the total life expectancy at birth is the target data.

## Exercises

### 1. Statistical Analysis
- For which income group has the difference in average life expectancy of men and women changed the most between 1960 and 2023?
- For which income group has variability in life expectancy at birth changed the most between 1960 and 2023?
- Which countries have the highest correlation between fertility rate and life expectancy at birth over the years (either positive or negative)? Which countries have the lowest correlation?

### 2. Data Visualizations
- Create a time-series line chart showing how life expectancy at birth has changed over the years for each income group.
- Create a world map where each country is color coded according to how high or low the life expectancy at birth is in 2023.
- For the year 1960, rank the countries by life expectancy at birth and classify them into five buckets of roughly equal size.
The buckets should be called 'Very high life expectancy', 'High life expectancy', 'Medium life expectancy', 'Low life expectancy', 'Very low life expectancy'.
Repeat this for the 2023 data. Create a Sankey diagram showing from which category in 1960 countries have moved to in 2023.

### 3. ML model
Build a machine learning model to forecast life expectancy at birth for each country from 2010 to 2023, using only data available up to and including 2010.

The objective is to assess how accurately future life expectancy trends can be predicted using historical information from the provided World Bank datasets.

Document how well the model performed when compared with the ground truth as well as challenges and ideas for future improvement for the model.

### 4. Dashboard
We would like to have a dashboard where we can monitor how life expectancy at birth, death rate, and fertility rate have changed over the years for every country.
For each country we want to know to which income group it belongs. For each country we also want to know how different the life expectancy at birth is between men and women in each year. 
Feel free to use a dashboard library of your choice (e.g. Shiny).

The dashboard should have filtering options, such as being able to filter by country, by income group and by region.

As a bonus the dashboard could also have the option to group by income group and region.
