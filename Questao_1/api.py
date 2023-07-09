import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('package_data.csv')

# Endpoint to retrieve packages
@app.route('/packages', methods=['GET'])
def get_packages():
    # Define the columns to sort by
    sort_columns = ['Package Name', 'Release Date', 'Python Version', 'Downloads (Last Month)']

    # Sort the DataFrame based on the specified columns
    df_sorted = df.sort_values(by=sort_columns)

    # Convert the sorted DataFrame to a list of dictionaries
    packages = df_sorted.to_dict('records')

    return jsonify(packages), 200

# Endpoint for searching packages by name and/or python_version
@app.route('/packages/search', methods=['GET'])
def search_packages():
    name = request.args.get('name')
    python_version = request.args.get('python_version')

    # Filter the DataFrame based on the search criteria
    mask = (df['Package Name'].str.contains(name, case=False, na=False) if name else True) & \
           (df['Python Version'] == python_version if python_version else True)
    df_filtered = df[mask]

    # Convert the filtered DataFrame to a list of dictionaries
    packages = df_filtered.to_dict('records')

    return jsonify(packages), 200

app.run(port=5000, host='localhost', debug=True) 