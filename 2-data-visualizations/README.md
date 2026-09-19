# Data Visualizations

The following tasks describe the visualization work to be completed for this project.

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

## Note about interactive Plotly outputs on GitHub

**Why interactive Plotly plots may not appear on GitHub**  
GitHub’s notebook renderer does not execute the JavaScript that Plotly uses for interactivity. As a result, interactive charts (hover, zoom, pan, tooltips) will not work in the static notebook preview even if the notebook was executed locally.

**Workaround included in this repository**  
To make the visualizations accessible to everyone, each Plotly figure is provided in two forms:

- **Interactive HTML** — a standalone HTML file you can open in any web browser to get full interactivity.  
- **Static image** — a high‑resolution PNG embedded in the notebook so GitHub shows a preview.

### How to view the interactive HTML and static images

There are two HTML files - [world-map.html](./world-map.html), [Sankey.html](./Sankey.html) and two PNG files - [world-map.png](./world-map.png), [Sankey.png](./Sankey.png) stored in this repo.<br>Viewers can do any of the following:
- Clone the repository:

    ```bash
    git clone https://github.com/avirupc/global-life-expectancy-analysis.git 
    cd 2-data-visualizations
    ```
    and open the HTML and PNG files

- Download from GitHub:<br>
  Open the file in the repo, click **Raw** (for HTML) or the image preview, then save the page/image to your computer. 




