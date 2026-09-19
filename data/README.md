# data directory

This folder contains the datasets downloaded for the project.  
In this assignment, we use the following datasets from the World Bank:

- [Life expectancy at birth, total (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)
- [Life expectancy at birth, male (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN)
- [Life expectancy at birth, female (years)](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN)
- [Death rate, crude (per 1,000 people)](https://data.worldbank.org/indicator/SP.DYN.CDRT.IN)
- [Fertility rate, total (births per woman)](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN)

Each dataset was downloaded as a zipped folder.<br>
When unzipped, each folder contains three CSV files:

1. **Main data file** – yearly records for all countries  
2. **Indicator metadata** – details about the indicator  
3. **Country metadata** – information about countries and regions  

Upon inspection, the **Country metadata** file is found to be identical across all five datasets.  

To make the files easier to identify and access, the main data files were renamed as follows:

- Life expectancy at birth, total (years) → `total_life_expectancy_at_birth.csv`  
- Life expectancy at birth, male (years) → `male_life_expectancy_at_birth.csv`  
- Life expectancy at birth, female (years) → `female_life_expectancy_at_birth.csv`  
- Death rate, crude (per 1,000 people) → `death_rate_crude.csv`  
- Fertility rate, total (births per woman) → `fertility_rate_total.csv`  

Additionally, the common CSV file containing metadata about countries and regions is stored once in this directory as:  `country_metadata.csv`
