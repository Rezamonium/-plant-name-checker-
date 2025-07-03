import pandas as pd
import requests
import time

# Load your Excel file
df = pd.read_excel("Scientific Name.xlsx")  # Ensure this is in the same folder
df.columns = ['Sci_name']  # Rename to standard column

# Function to query POWO API
def query_powo(name):
    url = "https://powo.science.kew.org/api/2/search"
    params = {"q": name, "f": "accepted_names"}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                accepted_name = results[0].get("name", "")
                author = results[0].get("author", "")
                return accepted_name, author
    except Exception as e:
        print(f"Error checking '{name}': {e}")
    return None, None

# Process each scientific name with progress
accepted_names = []
authors = []

for idx, row in df.iterrows():
    original_name = row['Sci_name']
    print(f"Checking {idx+1}/{len(df)}: {original_name}")
    accepted, author = query_powo(original_name)
    accepted_names.append(accepted)
    authors.append(author)
    time.sleep(0.5)  # Sleep to avoid overloading server

# Add results to DataFrame
df['Accepted Name'] = accepted_names
df['Author'] = authors

# Save output
df.to_excel("POWO_Accepted_Names_Output.xlsx", index=False)
print("✅ Done! Saved as 'POWO_Accepted_Names_Output.xlsx'")
