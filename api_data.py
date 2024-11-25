import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_population_data(url):
    """
    Get population data from Worldometer and return as a df.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")    # Parse the data.
        table = soup.find("table", {"id": "example2"})
        headers = [header.text.strip() for header in table.find_all("th")]    # Get headers, they will become column names.

        rows = []
        for row in table.find("tbody").find_all("tr"):
            cols = [col.text.strip() for col in row.find_all("td")]     # Get column rows from the table
            rows.append(cols)

        df = pd.DataFrame(rows, columns=headers)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error with getting data: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.worldometers.info/world-population/population-by-country/"
    print("Fetching population data from Worldometer...")
    
    # Get population data
    df = get_population_data(url)
    # Print the DataFrame
    print("Population Data:")
    print(df)

    # Save DataFrame to a csv file
    df.to_csv("Population.csv", index=False)

