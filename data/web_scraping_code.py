import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL to scrape
url = 'https://www.census2011.co.in/city.php'
response = requests.get(url)
html = response.content

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Extract the main table containing city data
table = soup.find('table', {'class': 'table table2 filter table-striped table-hover'})

# Extract headers from the table
headers = [th.text.strip() for th in table.find('thead').find_all('th')]

# Extract rows from the table
rows = [[cell.text.strip() for cell in tr.find_all('td')] for tr in table.find('tbody').find_all('tr')]

# Create DataFrame from the extracted data
cities = pd.DataFrame(rows, columns=headers)

# Convert numeric columns to appropriate data types
cities['Population'] = cities['Population'].str.replace(',', '').astype(int)
cities['Literacy'] = cities['Literacy'].str.replace('%', '').astype(float)
cities['Metropolitan'] = cities['Metropolitan'].str.replace(',', '').astype(int)

# 1. Which City has the highest levels of Literacy in the country?
cities.sort_values('Literacy', ascending=False, inplace=True)
highest_city = cities.iloc[0]['City']
highest_literacy = cities.iloc[0]['Literacy']
print(f"La città con il più alto livello di alfabetizzazione è : {highest_city} con valore {highest_literacy}")

# 2. Merge the `cities` table with the `sps_fnd_loc`
sps_fnd_loc = pd.read_excel(r"C:\Program Files\Python312\python-homework\myspace\homework\final-assignment-ML-webscr\data\sps_fnd_loc.xlsx")
sps_fnd_loc_lit = pd.merge(sps_fnd_loc, cities, on='City', how='left')

# Identify missing cities
missing_cities = sps_fnd_loc[~sps_fnd_loc['City'].isin(sps_fnd_loc_lit['City'])]['City'].values
if len(missing_cities) > 0:
    for city in missing_cities:
        print(city)
else:
    print("Non ci sono città mancanti")

# Check for "Delhi" in cities and "New Delhi" in sps_fnd_loc
if "Delhi" in cities['City'].values:
    print("Delhi è presente in cities")
else:
    print("Delhi non è presente in cities")

if "New Delhi" in sps_fnd_loc['City'].values:
    print("New Delhi è presente in sps_fnd_loc")
else:
    print("New Delhi non è presente in sps_fnd_loc")

# Replace "New Delhi" with "Delhi" to fix the merge issue
sps_fnd_loc['City'] = sps_fnd_loc['City'].replace("New Delhi", "Delhi")

# 3. Create a scatterplot
plt.figure(figsize=(10, 5))
scatter = plt.scatter(
    sps_fnd_loc_lit['Literacy'],
    sps_fnd_loc_lit['Avg. Salary'],
    s=sps_fnd_loc_lit['Population'] / 10000,  # Resize population for better visualization
    color='green',
    alpha=0.5
)

plt.xlabel('Alfabetizzazione')
plt.ylabel('Stipendio Medio')
plt.title('Alfabetizzazione vs Stipendio Medio con Popolazione come dimensione dei cerchi')
plt.show()

# Identify the city with the lowest literacy
lowest_literacy_city = sps_fnd_loc_lit.loc[sps_fnd_loc_lit['Literacy'].idxmin()]

plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    sps_fnd_loc_lit['Literacy'],
    sps_fnd_loc_lit['Avg. Salary'],
    s=sps_fnd_loc_lit['Population'] / 10000,  # Resize population for better visualization
    color='green',
    alpha=0.5
)

plt.annotate(
    f'{lowest_literacy_city["City"]}',
    (lowest_literacy_city['Literacy'], lowest_literacy_city['Avg. Salary']),
    xytext=(20, -20),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5', color='blue'),
    bbox=dict(boxstyle='round,pad=0.3', fc='blue', alpha=0.2)
)

plt.xlabel('Alfabetizzazione')
plt.ylabel('Stipendio Medio')
plt.title('Alfabetizzazione vs Stipendio Medio con Popolazione come dimensione dei cerchi')
plt.show()

# CONSIDERAZIONI
# Un tasso di alfabetizzazione basso con uno stipendio medio alto è atipico,
# suggerendo che ci potrebbero essere fattori unici che influenzano Sambhal.
# Potrebbe essere che l'economia locale è basata su settori che non richiedono alti livelli di istruzione, ma che pagano bene,
# come l'industria manifatturiera, l'estrazione di risorse, o settori artigianali specifici.
