# Web Scraping Project

## Final Assignment - Part 3

This repository contains a web scraping exercise performed to extract city data from the 2011 Census of India.

### Project Overview
The goal of this project is to scrape data from [Census 2011](https://www.census2011.co.in/city.php) and perform various data analysis tasks.

### Instructions
1. **Web Scraping**: Extract the first table containing city data and create a DataFrame named `cities`.
2. **Data Analysis**: Answer the following questions:
   - Which city has the highest levels of literacy?
   - Merge the `cities` DataFrame with [`sps_fnd_loc.xlsx`](/data/sps_fnd_loc.xlsx), identify and fix any missing city data.
   - Create a scatterplot to analyze the relationship between literacy and average salary, and identify any anomalies.

### Fix for Correct Merging
While merging the `cities` DataFrame with the `sps_fnd_loc` DataFrame, I encountered an issue where "Delhi" and "New Delhi" were treated as separate entities, leading to missing data in the merged DataFrame. 

To resolve this:
- I checked for the presence of both "Delhi" in the `cities` DataFrame and "New Delhi" in the `sps_fnd_loc` DataFrame.
- Since "New Delhi" should be considered equivalent to "Delhi" for the purposes of this analysis, I replaced all occurrences of "New Delhi" in the `sps_fnd_loc` DataFrame with "Delhi". 

This adjustment allowed for a successful merge, ensuring that all relevant city data was included.

### Calculations
The file containing all calculations and the Python code used for this project can be found in the `/data` directory. Please refer to [`web_scraping_code.py`](/data/web_scraping_code.py) for detailed implementation.

### Installation
Make sure to install the required libraries:
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
