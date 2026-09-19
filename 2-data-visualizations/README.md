# Data Visualizations

The following tasks describe the visualization work to be completed for this project. Each item states the objective and the expected output.

- Create a time-series line chart showing how life expectancy at birth has changed over the years for each income group.
- Create a world map where each country is color coded according to how high or low the life expectancy at birth is in 2023.
- For the year 1960, rank the countries by life expectancy at birth and classify them into five buckets of roughly equal size.
The buckets should be called 'Very high life expectancy', 'High life expectancy', 'Medium life expectancy', 'Low life expectancy', 'Very low life expectancy'.
Repeat this for the 2023 data. Create a Sankey diagram showing from which category in 1960 countries have moved to in 2023.

I have created the Jupyter Notebook `data-visualizations.ipynb` for performing these tasks. It contains:

- Code for data loading and preprocessing.
- Implementation of the visualizations described above.
- Markdown cells with explanatory notes and assumptions.
- Output cells that display the resulting plots.

Open `./data-visualizations.ipynb` to run the notebook and view the charts.

### Notes

- The notebook includes comments explaining key preprocessing steps (for example, how missing values are handled and how the five buckets are computed).
- Hover text and legends are included in the visualizations to improve interpretability.

