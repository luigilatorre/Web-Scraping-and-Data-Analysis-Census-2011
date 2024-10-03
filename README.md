# Web Scraping Project
This repository contains a web scraping exercise performed to extract city data from the 2011 Census of India.

### Project Overview
The goal of this project is to scrape data from [Census 2011](https://www.census2011.co.in/city.php) and perform various data analysis tasks.

### Instructions
1. **Web Scraping**: Extract the first table containing city data and create a DataFrame named `cities`.
2. **Data Analysis**: Answer the following questions:
   - Which city has the highest levels of literacy?
   - Merge the `cities` DataFrame with `sps_fnd_loc`, identify and fix any missing city data.
   - Create a scatterplot to analyze the relationship between literacy and average salary, and identify any anomalies.

### Installation
Make sure to install the required libraries:
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
